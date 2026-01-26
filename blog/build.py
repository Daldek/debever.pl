#!/usr/bin/env python3
"""
Blog Build Script for debever.pl

Converts Markdown files with YAML frontmatter to static HTML pages.
Generates blog/index.html with a list of all posts.

Usage:
    python blog/build.py

Requirements:
    pip install markdown2 pyyaml
"""

import os
import re
import yaml
import markdown2
from pathlib import Path
from datetime import datetime
from typing import Optional


# Configuration
BLOG_DIR = Path(__file__).parent
POSTS_DIR = BLOG_DIR / "posts"
OUTPUT_DIR = BLOG_DIR
TAGS_DIR = BLOG_DIR / "tag"
TEMPLATE_FILE = BLOG_DIR / "template.html"
INDEX_TEMPLATE_FILE = BLOG_DIR / "index-template.html"
TAG_TEMPLATE_FILE = BLOG_DIR / "tag-template.html"

# Markdown extensions for code highlighting and extras
MARKDOWN_EXTRAS = [
    "fenced-code-blocks",
    "code-friendly",
    "tables",
    "header-ids",
    "strike",
    "task_list",
    "cuddled-lists",
]


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    # Convert to lowercase
    slug = text.lower()
    # Replace Polish characters
    polish_chars = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'
    }
    for pl, en in polish_chars.items():
        slug = slug.replace(pl, en)
    # Replace spaces and special chars with hyphens
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    return slug


class Post:
    """Represents a blog post with metadata and content."""

    def __init__(self, filepath: Path):
        self.filepath = filepath
        self.slug = filepath.stem
        self.raw_content = filepath.read_text(encoding="utf-8")
        self._parse()

    def _parse(self):
        """Parse frontmatter and content from markdown file."""
        # Match YAML frontmatter between ---
        pattern = r"^---\s*\n(.*?)\n---\s*\n(.*)$"
        match = re.match(pattern, self.raw_content, re.DOTALL)

        if match:
            frontmatter_str = match.group(1)
            self.content_md = match.group(2).strip()
            try:
                self.frontmatter = yaml.safe_load(frontmatter_str) or {}
            except yaml.YAMLError as e:
                print(f"Warning: Failed to parse frontmatter in {self.filepath}: {e}")
                self.frontmatter = {}
        else:
            self.frontmatter = {}
            self.content_md = self.raw_content

        # Extract metadata with defaults
        self.title = self.frontmatter.get("title", self.slug.replace("-", " ").title())
        self.date = self._parse_date(self.frontmatter.get("date"))
        self.category = self.frontmatter.get("category", "Bez kategorii")
        self.tags = self.frontmatter.get("tags", [])
        self.excerpt = self.frontmatter.get("excerpt", self._generate_excerpt())
        self.image = self.frontmatter.get("image", None)

    def _parse_date(self, date_value) -> datetime:
        """Parse date from various formats."""
        if isinstance(date_value, datetime):
            return date_value
        if isinstance(date_value, str):
            try:
                return datetime.strptime(date_value, "%Y-%m-%d")
            except ValueError:
                pass
        # Fallback: try to extract date from filename (YYYY-MM-DD-slug.md)
        match = re.match(r"^(\d{4}-\d{2}-\d{2})", self.slug)
        if match:
            return datetime.strptime(match.group(1), "%Y-%m-%d")
        return datetime.now()

    def _generate_excerpt(self, max_length: int = 160) -> str:
        """Generate excerpt from content if not provided."""
        # Strip markdown formatting for excerpt
        text = re.sub(r"[#*_`\[\]()]", "", self.content_md)
        text = re.sub(r"\n+", " ", text).strip()
        if len(text) > max_length:
            text = text[:max_length].rsplit(" ", 1)[0] + "..."
        return text

    @property
    def content_html(self) -> str:
        """Convert markdown content to HTML."""
        return markdown2.markdown(self.content_md, extras=MARKDOWN_EXTRAS)

    @property
    def date_iso(self) -> str:
        """Return date in ISO format."""
        return self.date.strftime("%Y-%m-%d")

    @property
    def date_display(self) -> str:
        """Return date in human-readable format (Polish)."""
        months_pl = [
            "", "stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca",
            "lipca", "sierpnia", "września", "października", "listopada", "grudnia"
        ]
        return f"{self.date.day} {months_pl[self.date.month]} {self.date.year}"

    @property
    def url(self) -> str:
        """Return relative URL to the post."""
        return f"{self.slug}.html"

    def __repr__(self):
        return f"Post({self.slug}, {self.date_iso})"


def load_template(template_path: Path) -> str:
    """Load HTML template from file."""
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    return template_path.read_text(encoding="utf-8")


def render_post(post: Post, template: str, prev_post: Optional[Post], next_post: Optional[Post]) -> str:
    """Render a single post using the template."""
    # Build navigation links
    nav_prev = ""
    nav_next = ""

    if prev_post:
        nav_prev = f'<a href="{prev_post.url}" class="blog-nav__link blog-nav__link--prev">&larr; {prev_post.title}</a>'

    if next_post:
        nav_next = f'<a href="{next_post.url}" class="blog-nav__link blog-nav__link--next">{next_post.title} &rarr;</a>'

    # Build tags HTML with links
    tags_html = ""
    if post.tags:
        tags_list = ", ".join(
            f'<a href="/blog/tag/{slugify(tag)}.html" class="blog-post__tag">{tag}</a>'
            for tag in post.tags
        )
        tags_html = f'<div class="blog-post__tags">{tags_list}</div>'

    # Replace placeholders in template
    html = template
    replacements = {
        "{{title}}": post.title,
        "{{date}}": post.date_display,
        "{{date_iso}}": post.date_iso,
        "{{category}}": post.category,
        "{{tags}}": tags_html,
        "{{content}}": post.content_html,
        "{{excerpt}}": post.excerpt,
        "{{url}}": post.url,
        "{{nav_prev}}": nav_prev,
        "{{nav_next}}": nav_next,
    }

    for placeholder, value in replacements.items():
        html = html.replace(placeholder, value)

    return html


def render_index(posts: list[Post], template: str, tags: dict[str, list[Post]] = None) -> str:
    """Render the blog index page."""
    posts_html = []

    for post in posts:
        post_item = f'''
        <article class="blog-list__item">
          <time class="blog-list__date" datetime="{post.date_iso}">{post.date_display}</time>
          <h2 class="blog-list__title"><a href="{post.url}">{post.title}</a></h2>
          <p class="blog-list__excerpt">{post.excerpt}</p>
          <span class="blog-list__category">{post.category}</span>
        </article>'''
        posts_html.append(post_item)

    html = template.replace("{{posts}}", "\n".join(posts_html))
    html = html.replace("{{post_count}}", str(len(posts)))

    # Generate tags cloud if tags provided
    if tags:
        tags_cloud_html = generate_tags_cloud(tags)
        html = html.replace("{{tags_cloud}}", tags_cloud_html)
    else:
        html = html.replace("{{tags_cloud}}", "")

    return html


def render_tag_page(tag: str, posts: list[Post], template: str) -> str:
    """Render a tag page with all posts for that tag."""
    posts_html = []

    for post in posts:
        post_item = f'''
        <article class="blog-list__item">
          <time class="blog-list__date" datetime="{post.date_iso}">{post.date_display}</time>
          <h2 class="blog-list__title"><a href="/blog/{post.url}">{post.title}</a></h2>
          <p class="blog-list__excerpt">{post.excerpt}</p>
          <span class="blog-list__category">{post.category}</span>
        </article>'''
        posts_html.append(post_item)

    html = template.replace("{{tag}}", tag)
    html = html.replace("{{tag_slug}}", slugify(tag))
    html = html.replace("{{posts}}", "\n".join(posts_html))
    html = html.replace("{{post_count}}", str(len(posts)))

    return html


def collect_tags(posts: list[Post]) -> dict[str, list[Post]]:
    """Collect all tags and their associated posts."""
    tags = {}
    for post in posts:
        for tag in post.tags:
            if tag not in tags:
                tags[tag] = []
            tags[tag].append(post)
    return tags


# Thematic tag categories
TAG_CATEGORIES = {
    "Hydraulika i modelowanie": [
        "hydraulika", "hec-ras", "modelowanie", "modelowanie-hydrauliczne",
        "mike21", "telemac", "bluekenue", "2d", "hotstart", "symulacja",
        "geometria", "interfejs", "ras2025", "mesh", "siatka", "hydraulics",
        "teoria", "cisnienie-hydrostatyczne", "hydrostatyka", "plyn-doskonaly",
        "rownanie-ciaglosci", "dynamika-plynow"
    ],
    "Hydrologia": [
        "hydrologia", "hydrology", "zlewnia", "basin", "catchment", "wododział",
        "susza", "powodz", "ochrona-przeciwpowodziowa", "zbiorniki-retencyjne",
        "gospodarka-wodna", "jezioro-biezdruchowo", "limnologia", "pobiedziska"
    ],
    "GIS i dane przestrzenne": [
        "gis", "qgis", "arcgis", "dane-przestrzenne", "analiza-przestrzenna"
    ],
    "Klimat i środowisko": [
        "klimat", "ochrona-srodowiska", "citizen-science", "smw", "wwf",
        "monitoring-wod", "jakosc-wody", "hydroni", "fundacja"
    ],
    "Programowanie": [
        "python", "api", "imgw", "opendata", "dane", "http-server",
        "transfer", "sieć", "pyenv", "ssh", "vnc", "windows", "debian", "macos"
    ],
    "Źródła danych": [
        "API", "IMGW", "SMHI", "DMI", "meteorology", "oceanography"
    ],
    "Inne": [
        "tutorial", "wprowadzenie", "blog", "powitanie", "edukacja",
        "media-spolecznosciowe"
    ]
}


def generate_tags_cloud(tags: dict[str, list[Post]]) -> str:
    """Generate HTML for thematic tags cloud."""
    html_parts = []
    used_tags = set()

    for category, category_tags in TAG_CATEGORIES.items():
        # Find tags that exist in this category
        existing_tags = []
        for tag in category_tags:
            # Case-insensitive matching
            for actual_tag in tags.keys():
                if actual_tag.lower() == tag.lower() and actual_tag not in used_tags:
                    existing_tags.append((actual_tag, len(tags[actual_tag])))
                    used_tags.add(actual_tag)
                    break

        if existing_tags:
            # Sort by count descending
            existing_tags.sort(key=lambda x: x[1], reverse=True)
            tags_html = " ".join(
                f'<a href="/blog/tag/{slugify(tag)}.html" class="tags-cloud__tag">{tag} <span class="tags-cloud__count">({count})</span></a>'
                for tag, count in existing_tags
            )
            html_parts.append(f'''
        <div class="tags-cloud__category">
          <h3 class="tags-cloud__category-title">{category}</h3>
          <div class="tags-cloud__tags">{tags_html}</div>
        </div>''')

    # Add any remaining uncategorized tags
    remaining_tags = [(tag, len(posts)) for tag, posts in tags.items() if tag not in used_tags]
    if remaining_tags:
        remaining_tags.sort(key=lambda x: x[1], reverse=True)
        tags_html = " ".join(
            f'<a href="/blog/tag/{slugify(tag)}.html" class="tags-cloud__tag">{tag} <span class="tags-cloud__count">({count})</span></a>'
            for tag, count in remaining_tags
        )
        html_parts.append(f'''
        <div class="tags-cloud__category">
          <h3 class="tags-cloud__category-title">Pozostałe</h3>
          <div class="tags-cloud__tags">{tags_html}</div>
        </div>''')

    return "\n".join(html_parts)


def build():
    """Main build function."""
    print("Building blog...")

    # Find all markdown files
    md_files = sorted(POSTS_DIR.glob("*.md"), reverse=True)

    if not md_files:
        print("No markdown files found in posts/")
        return

    print(f"Found {len(md_files)} posts")

    # Parse all posts
    posts = []
    for md_file in md_files:
        try:
            post = Post(md_file)
            posts.append(post)
            print(f"  Parsed: {post.slug}")
        except Exception as e:
            print(f"  Error parsing {md_file}: {e}")

    # Sort by date (newest first)
    posts.sort(key=lambda p: p.date, reverse=True)

    # Load templates
    try:
        post_template = load_template(TEMPLATE_FILE)
    except FileNotFoundError:
        print(f"Error: Template file not found: {TEMPLATE_FILE}")
        return

    # Generate individual post pages
    print("\nGenerating post pages...")
    for i, post in enumerate(posts):
        prev_post = posts[i + 1] if i + 1 < len(posts) else None
        next_post = posts[i - 1] if i > 0 else None

        html = render_post(post, post_template, prev_post, next_post)
        output_path = OUTPUT_DIR / post.url
        output_path.write_text(html, encoding="utf-8")
        print(f"  Generated: {post.url}")

    # Collect tags first (needed for index and tag pages)
    tags = collect_tags(posts)

    # Generate index page
    print("\nGenerating index page...")
    try:
        index_template = load_template(INDEX_TEMPLATE_FILE)
    except FileNotFoundError:
        # Use a default index template if none exists
        index_template = create_default_index_template()

    index_html = render_index(posts, index_template, tags)
    index_path = OUTPUT_DIR / "index.html"
    index_path.write_text(index_html, encoding="utf-8")
    print(f"  Generated: index.html")

    # Generate tag pages
    print("\nGenerating tag pages...")

    # Create tags directory if it doesn't exist
    TAGS_DIR.mkdir(exist_ok=True)

    try:
        tag_template = load_template(TAG_TEMPLATE_FILE)
    except FileNotFoundError:
        tag_template = create_default_tag_template()

    for tag, tag_posts in sorted(tags.items()):
        tag_html = render_tag_page(tag, tag_posts, tag_template)
        tag_slug = slugify(tag)
        tag_path = TAGS_DIR / f"{tag_slug}.html"
        tag_path.write_text(tag_html, encoding="utf-8")
        print(f"  Generated: tag/{tag_slug}.html ({len(tag_posts)} posts)")

    # Generate tags list file
    tags_list_path = BLOG_DIR / "TAGS.md"
    tags_sorted = sorted(tags.items(), key=lambda x: len(x[1]), reverse=True)
    tags_content = "# Lista tagów\n\n"
    tags_content += "| Tag | Liczba wpisów |\n"
    tags_content += "|-----|---------------|\n"
    for tag, tag_posts in tags_sorted:
        tags_content += f"| {tag} | {len(tag_posts)} |\n"
    tags_list_path.write_text(tags_content, encoding="utf-8")

    print(f"\nBuild complete! {len(posts)} posts, {len(tags)} tags generated.")
    print(f"\n--- Lista tagów (posortowana wg popularności) ---")
    for tag, tag_posts in tags_sorted:
        print(f"  {tag}: {len(tag_posts)} wpisów")


def create_default_index_template() -> str:
    """Create a default index template if none exists."""
    return '''<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Blog Piotra de Bevera - artykuły o hydrologii, modelowaniu hydraulicznym i GIS">
  <title>Blog | Piotr de Bever</title>
  <link rel="canonical" href="https://debever.pl/blog/">
  <link rel="icon" href="/assets/images/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
  <header class="header">
    <div class="container">
      <a href="/" class="logo">Piotr de Bever</a>
      <nav class="nav">
        <button class="nav__toggle" aria-label="Menu" aria-expanded="false">
          <span class="nav__hamburger"></span>
        </button>
        <ul class="nav__list">
          <li><a href="/#uslugi" class="nav__link">Usługi</a></li>
          <li><a href="/#portfolio" class="nav__link">Portfolio</a></li>
          <li><a href="/#o-mnie" class="nav__link">O mnie</a></li>
          <li><a href="/#kontakt" class="nav__link">Kontakt</a></li>
          <li><a href="/blog/" class="nav__link nav__link--active">Blog</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="blog-index">
    <div class="container">
      <header class="blog-index__header">
        <h1 class="blog-index__title">Blog</h1>
        <p class="blog-index__subtitle">Artykuły o hydrologii, modelowaniu hydraulicznym i programowaniu</p>
      </header>

      <div class="blog-list">
        {{posts}}
      </div>
    </div>
  </main>

  <footer class="footer">
    <div class="container">
      <p>&copy; 2026 Piotr de Bever. Wszelkie prawa zastrzeżone.</p>
      <nav class="footer__nav">
        <a href="/">Strona główna</a>
      </nav>
    </div>
  </footer>

  <script src="/assets/js/main.js"></script>
</body>
</html>'''


def create_default_tag_template() -> str:
    """Create a default tag template if none exists."""
    return '''<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Wpisy z tagiem {{tag}} - Blog Piotra de Bevera">
  <title>Tag: {{tag}} | Piotr de Bever</title>
  <link rel="canonical" href="https://debever.pl/blog/tag/{{tag_slug}}.html">
  <link rel="icon" href="/assets/images/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
  <header class="header">
    <div class="container">
      <a href="/" class="logo">Piotr de Bever</a>
      <nav class="nav">
        <button class="nav__toggle" aria-label="Menu" aria-expanded="false">
          <span class="nav__hamburger"></span>
        </button>
        <ul class="nav__list">
          <li><a href="/#uslugi" class="nav__link">Usługi</a></li>
          <li><a href="/#portfolio" class="nav__link">Portfolio</a></li>
          <li><a href="/#o-mnie" class="nav__link">O mnie</a></li>
          <li><a href="/#kontakt" class="nav__link">Kontakt</a></li>
          <li><a href="/blog/" class="nav__link nav__link--active">Blog</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="blog-index">
    <div class="container">
      <header class="blog-index__header">
        <p class="blog-index__breadcrumb"><a href="/blog/">Blog</a> / Tag</p>
        <h1 class="blog-index__title">#{{tag}}</h1>
        <p class="blog-index__count">{{post_count}} wpisów</p>
      </header>

      <div class="blog-list">
        {{posts}}
      </div>

      <div class="blog-post__back">
        <a href="/blog/" class="btn btn--secondary">&larr; Wszystkie wpisy</a>
      </div>
    </div>
  </main>

  <footer class="footer">
    <div class="container">
      <p>&copy; 2026 Piotr de Bever. Wszelkie prawa zastrzeżone.</p>
      <nav class="footer__nav">
        <a href="/">Strona główna</a>
      </nav>
    </div>
  </footer>

  <script src="/assets/js/main.js"></script>
</body>
</html>'''


if __name__ == "__main__":
    build()
