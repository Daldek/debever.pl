# Progress projektu debever.pl

## Ostatnia aktualizacja: 2026-01-26 (sesja 5 — grafiki portfolio + tło hero)

## Aktualny status
- [x] Phase 1: Wizytówka — UKONCZONE
- [x] Phase 2: Blog — UKONCZONE

## Co zostalo zrobione
- [x] 2026-01-26: Inicjalizacja repozytorium Git
- [x] 2026-01-26: Utworzenie brancha `develop`
- [x] 2026-01-26: Konfiguracja `.gitignore`
- [x] 2026-01-26: Utworzenie struktury katalogow (assets/, blog/)
- [x] 2026-01-26: Utworzenie PROGRESS.md
- [x] 2026-01-26: Szkielet HTML (index.html) — wszystkie sekcje
- [x] 2026-01-26: Style bazowe (reset, zmienne CSS, dark mode)
- [x] 2026-01-26: Responsywnosc (mobile/tablet/desktop)
- [x] 2026-01-26: Mobile hamburger menu (JS)
- [x] 2026-01-26: Ikony SVG do kart uslug (Lucide Icons)
- [x] 2026-01-26: Favicon SVG (symbol fali) + site.webmanifest
- [x] 2026-01-26: Google Analytics 4 (z cookie consent, RODO-compliant)
- [x] 2026-01-26: Baner cookie consent
- [x] 2026-01-26: Strona polityki prywatnosci (privacy.html)
- [x] 2026-01-26: Audyt bezpieczenstwa + poprawki (walidacja GA ID, noreferrer, referrer-policy)
- [x] 2026-01-26: SEO: robots.txt, sitemap.xml, canonical URL
- [x] 2026-01-26: Structured Data (JSON-LD): Person, ProfessionalService, WebSite
- [x] 2026-01-26: Open Graph + Twitter Cards + og-image.svg
- [x] 2026-01-26: Narzedzie PMAXTP (/tools/pmaxtp.html) - ukryte, dark mode
- [x] 2026-01-26: Plik wodowskazy.csv (/tools/wodowskazy.csv)
- [x] 2026-01-26: Strona 404.html
- [x] 2026-01-26: Zdjecie profilowe (profile.jpg) w sekcji O mnie
- [x] 2026-01-26: Dane firmowe z CEIDG (NIP, REGON, adres, email)
- [x] 2026-01-26: Testy cross-browser + poprawki kompatybilnosci Safari
- [x] 2026-01-26: Polaczenie z GitHub (https://github.com/Daldek/debever.pl)
- [x] 2026-01-26: GA4 Measurement ID skonfigurowany (G-3KHED211LP)
- [x] 2026-01-26: Deploy testowy na Mikrus (http://srv08.mikr.us:40693/)
- [x] 2026-01-26: Blog — skrypt build.py (Markdown -> HTML)
- [x] 2026-01-26: Blog — szablon template.html dla wpisow
- [x] 2026-01-26: Blog — szablon index-template.html dla listy wpisow
- [x] 2026-01-26: Blog — style CSS dla bloga (sekcja Blog styles w style.css)
- [x] 2026-01-26: Blog — migracja 26 wpisow z WordPress do Markdown
- [x] 2026-01-26: Blog — wygenerowane 26 plikow HTML + index.html
- [x] 2026-01-26: Nawigacja — dodany link do bloga
- [x] 2026-01-26: Sitemap — dodane 26 URL-i wpisow blogowych
- [x] 2026-01-26: Blog — strony tagow (/blog/tag/*.html)
- [x] 2026-01-26: Blog — klikalne tagi we wpisach
- [x] 2026-01-26: Blog — lista tagow (blog/TAGS.md)
- [x] 2026-01-26: Blog — poprawki CSS (padding-top, mniejsze naglowki)
- [x] 2026-01-26: SEO — RSS Feed (/blog/feed.xml)
- [x] 2026-01-26: SEO — automatyczna aktualizacja sitemap.xml przy build.py
- [x] 2026-01-26: Deploy na Mikrus — zainstalowane zaleznosci Python (markdown2, pyyaml)
- [x] 2026-01-26: Portfolio — 6 grafik (Modelowanie_2D.png, Telemac.jpeg, Hydrologia.jpg, GIS.jpg, Ortofotomapa.jpg, Analiza_danych.png)
- [x] 2026-01-26: Hero — tlo ze zdjeciem fiordu (Norwegia.jpg) z przyciemnieniem i parallax
- [x] 2026-01-26: CSS — style dla obrazkow portfolio (object-fit, hover zoom)

## Nastepne kroki (TODO)
1. Wygenerowac apple-touch-icon.png (180x180) z favicon.svg
2. Skonwertowac og-image.svg na PNG (1200x630)
3. Deploy produkcyjny (SSL + domena debever.pl)
4. (Opcjonalnie) Pobrac obrazki z WordPress do blog/assets/images/

## Znane problemy / Blokery
- Brak apple-touch-icon.png (wygenerowac z favicon.svg na realfavicongenerator.net)
- Brak og-image.png (skonwertowac og-image.svg na PNG 1200x630)

## Decyzje projektowe
- 2026-01-26: Fonty — Google Fonts (Merriweather + Inter)
- 2026-01-26: Kolory dark mode — bg #0d1117, akcent #58a6ff (niebieski)
- 2026-01-26: BEM dla CSS (block__element--modifier)
- 2026-01-26: GitHub remote: https://github.com/Daldek/debever.pl
- 2026-01-26: Tlo hero — Norwegia.jpg z 70-80% overlay i parallax

## Notatki dla przyszlej sesji
> Strona testowa dziala na Mikrusie: http://srv08.mikr.us:40693/
> GA4 tymczasowo wylaczone (zakomentowane w index.html).
>
> **Blog — dodawanie nowych wpisow:**
> 1. Utworz plik `blog/posts/YYYY-MM-DD-slug.md` z frontmatter YAML
> 2. Uruchom `python3 blog/build.py`
> 3. Zacommituj i push
> 4. Na Mikrusie: `cd /var/www/debever.pl && sudo git pull && python3.12 blog/build.py`
>
> **Zaleznosci Python:** pyyaml, markdown2
> - Na Mikrusie uzyc `python3.12` (system ma Python 3.10, ale pip zainstalowal pakiety dla 3.12)
>
> **Dostepne tagi:** zobacz `blog/TAGS.md` lub output z `build.py`
>
> **RSS Feed:** /blog/feed.xml (autodiscovery w naglowkach HTML)
>
> **Grafiki portfolio:**
> - Modelowanie_2D.png — mapa glebokosci z modelu 2D
> - Telemac.jpeg — siatka TELEMAC (obrocona, odbita, hue-rotate CSS)
> - Hydrologia.jpg — notatki z obliczen hydrologicznych
> - GIS.jpg — mapa nachylenia zlewni Rzeki Glownej
> - Ortofotomapa.jpg — zbiornik wodny z drona
> - Analiza_danych.png — kod Python (biblioteka hydrologiczna)
> - Norwegia.jpg — tlo hero (fiord)
>
> Do deploymentu produkcyjnego:
> - Wlaczyc GA4
> - Skonfigurowac SSL (Let's Encrypt)
> - Przekierowac domene debever.pl na Mikrusa
> - Zaktualizowac nginx na port 80/443
