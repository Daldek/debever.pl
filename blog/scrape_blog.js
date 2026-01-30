const https = require('https');
const cheerio = require('cheerio');
const fs = require('fs');
const path = require('path');

const BASE_URL = 'https://debever.pl';
const BLOG_DIR = __dirname;

const MAPPING = [
  ['2021-03-21-hello-world.html', '/uncategorized/hello-world/'],
  ['2021-09-06-its-alive.html', '/uncategorized/its-alive/'],
  ['2021-10-27-cisnienie-hydrostatyczne.html', '/hydro/hydrostatic-pressure/'],
  ['2022-01-02-co-sie-dzieje-z-jeziorem-biezdruchowo.html', '/hydro/co-sie-dzieje-z-jeziorem-biezdruchowo/'],
  ['2022-01-10-plyn-doskonaly-i-ciaglosc-strugi.html', '/hydro/plyn-doskonaly-i-ciaglosc-strugi/'],
  ['2022-02-05-hotstart-mike21.html', '/hydro/hotstart-czyli-jak-uratowac-przerwana-symulacje-w-mike21/'],
  ['2022-11-21-hec-ras-crash-course-1.html', '/hydro/hydraulics/hec-ras/hec-ras-crash-course-1/'],
  ['2022-12-08-hec-ras-crash-course-2.html', '/hydro/hydraulics/hec-ras/hec-ras-crash-course-2/'],
  ['2023-08-07-problem-niezrozumienia.html', '/uncategorized/problem-niezrozumienia/'],
  ['2023-08-13-krotko-o-suszy.html', '/uncategorized/krotko-o-suszy/'],
  ['2024-01-03-rzeka-glowna-i-jej-zlewnia.html', '/gis/rzeka-glowna-i-jej-zlewnia/'],
  ['2024-04-04-czy-to-ptak-nie-to-hydroni.html', '/uncategorized/czy-to-ptak-czy-to-samolot-nie-to-hydroni/'],
  ['2024-05-07-spoleczny-monitoring-wod-wwf-polska.html', '/hydro/spoleczny-monitoring-wod-wwf-polska/'],
  ['2024-09-14-rola-zbiornikow-w-ochronie-przeciwpowodziowej.html', '/hydro/rola-zbiornikow-w-ochronie-przeciwpowodziowej/'],
  ['2024-10-03-zupelnie-nowy-hec-ras-2025.html', '/hydro/hydraulics/hec-ras/zupelnie-nowy-hec-ras-2025/'],
  ['2024-10-07-wprowadzenie-do-gis.html', '/gis/wprowadzenie-do-gis/'],
  ['2024-10-17-automatyzacja-pobierania-danych-imgw.html', '/programming/o-tym-jak-probowalem-zautomatyzowac-pobieranie-danych-z-imgw/'],
  ['2025-03-20-transfer-plikow-w-sieci-domowej.html', '/programming/transfer-plikow-w-sieci-domowej/'],
  ['2025-03-29-skad-brac-dane-do-projektow.html', '/climate/skad-brac-dane-do-projektow/'],
  ['2025-04-03-tworzenie-siatki-w-bluekenue.html', '/hydro/hydraulics/bluekenue/tworzenie-siatki-w-bluekenue/'],
  ['2025-09-02-czym-jest-zlewnia.html', '/hydro/hydrology/czym-jest-zlewnia/'],
  ['2025-09-03-hec-ras-od-zera-wstep.html', '/hydro/hydraulics/hec-ras/hec-ras-od-zera/hec-ras-od-zera/'],
  ['2025-09-05-hec-ras-od-zera-podstawy-modelowania.html', '/hydro/hydraulics/hec-ras/hec-ras-od-zera/hec-ras-od-zera-podstawy-modelowania-ruchu-wody/'],
  ['2025-09-08-hec-ras-od-zera-interfejs-uzytkownika.html', '/hydro/hydraulics/hec-ras/hec-ras-od-zera/hec-ras-od-zera-interfejs-uzytkownika/'],
  ['2025-09-28-hec-ras-od-zera-tworzenie-geometrii-modelu.html', '/hydro/hydraulics/hec-ras/hec-ras-od-zera/hec-ras-od-zera-tworzenie-geometrii-modelu/'],
  ['2026-01-12-windows-debian-macos.html', '/programming/windows-debian-macos/'],
];

function fetchPage(url) {
  return new Promise((resolve, reject) => {
    https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0 (debever-migration-script)' } }, (res) => {
      if (res.statusCode >= 300 && res.statusCode < 400 && res.headers.location) {
        const redirectUrl = res.headers.location.startsWith('http')
          ? res.headers.location
          : BASE_URL + res.headers.location;
        return fetchPage(redirectUrl).then(resolve).catch(reject);
      }
      if (res.statusCode !== 200) {
        reject(new Error(`HTTP ${res.statusCode} for ${url}`));
        res.resume();
        return;
      }
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => resolve(data));
      res.on('error', reject);
    }).on('error', reject);
  });
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function processPost(localFile, wpPath) {
  const wpUrl = BASE_URL + wpPath;
  const localPath = path.join(BLOG_DIR, localFile);

  // Check local file exists
  if (!fs.existsSync(localPath)) {
    console.error(`  SKIP: Local file not found: ${localFile}`);
    return false;
  }

  // Fetch WordPress page
  console.log(`  Fetching: ${wpUrl}`);
  let wpHtml;
  try {
    wpHtml = await fetchPage(wpUrl);
  } catch (err) {
    console.error(`  ERROR fetching ${wpUrl}: ${err.message}`);
    return false;
  }

  // Extract article content from WordPress
  const $wp = cheerio.load(wpHtml);
  const entryContent = $wp('.entry-content.clr');

  if (entryContent.length === 0) {
    console.error(`  ERROR: No .entry-content found on ${wpUrl}`);
    return false;
  }

  // Get the inner HTML of the entry-content div
  const articleHtml = entryContent.html().trim();

  // Read local file
  let localHtml = fs.readFileSync(localPath, 'utf-8');

  // Replace content inside <div class="blog-post__content">...</div>
  const contentRegex = /(<div class="blog-post__content">)([\s\S]*?)(<\/div>\s*\n\s*<!-- Post Navigation -->)/;
  const match = localHtml.match(contentRegex);

  if (!match) {
    // Try a more lenient regex
    const contentRegex2 = /(<div class="blog-post__content">)([\s\S]*?)(\n\s*<\/div>\s*\n)/;
    const match2 = localHtml.match(contentRegex2);
    if (!match2) {
      console.error(`  ERROR: Cannot find blog-post__content div in ${localFile}`);
      return false;
    }
    localHtml = localHtml.replace(contentRegex2, `$1\n          ${articleHtml}\n        $3`);
  } else {
    localHtml = localHtml.replace(contentRegex, `$1\n          ${articleHtml}\n        $3`);
  }

  // Write back
  fs.writeFileSync(localPath, localHtml, 'utf-8');
  console.log(`  OK: ${localFile} updated`);
  return true;
}

async function main() {
  console.log(`Processing ${MAPPING.length} posts...\n`);

  let success = 0;
  let failed = 0;

  for (let i = 0; i < MAPPING.length; i++) {
    const [localFile, wpPath] = MAPPING[i];
    console.log(`[${i + 1}/${MAPPING.length}] ${localFile}`);

    const ok = await processPost(localFile, wpPath);
    if (ok) success++;
    else failed++;

    // Delay between requests (1.5s)
    if (i < MAPPING.length - 1) {
      await sleep(1500);
    }
  }

  console.log(`\nDone! Success: ${success}, Failed: ${failed}`);
}

main().catch(console.error);
