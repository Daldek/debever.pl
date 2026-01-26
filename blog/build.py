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
TEMPLATE_FILE = BLOG_DIR / "template.html"
INDEX_TEMPLATE_FILE = BLOG_DIR / "index-template.html"

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

    # Build tags HTML
    tags_html = ""
    if post.tags:
        tags_list = ", ".join(f'<span class="blog-post__tag">{tag}</span>' for tag in post.tags)
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


def render_index(posts: list[Post], template: str) -> str:
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

    return html


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

    # Generate index page
    print("\nGenerating index page...")
    try:
        index_template = load_template(INDEX_TEMPLATE_FILE)
    except FileNotFoundError:
        # Use a default index template if none exists
        index_template = create_default_index_template()

    index_html = render_index(posts, index_template)
    index_path = OUTPUT_DIR / "index.html"
    index_path.write_text(index_html, encoding="utf-8")
    print(f"  Generated: index.html")

    print(f"\nBuild complete! {len(posts)} posts generated.")


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


if __name__ == "__main__":
    build()
