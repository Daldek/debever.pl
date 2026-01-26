# Progress projektu debever.pl

## Ostatnia aktualizacja: 2026-01-26 (sesja 3 — migracja bloga)

## Aktualny status
- [ ] Phase 1: Wizytówka — W TRAKCIE (90% gotowe, brakuje portfolio)
- [x] Phase 2: Blog — UKOŃCZONE

## Co zostało zrobione
- [x] 2026-01-26: Inicjalizacja repozytorium Git
- [x] 2026-01-26: Utworzenie brancha `develop`
- [x] 2026-01-26: Konfiguracja `.gitignore`
- [x] 2026-01-26: Utworzenie struktury katalogów (assets/, blog/)
- [x] 2026-01-26: Utworzenie PROGRESS.md
- [x] 2026-01-26: Szkielet HTML (index.html) — wszystkie sekcje
- [x] 2026-01-26: Style bazowe (reset, zmienne CSS, dark mode)
- [x] 2026-01-26: Responsywność (mobile/tablet/desktop)
- [x] 2026-01-26: Mobile hamburger menu (JS)
- [x] 2026-01-26: Ikony SVG do kart usług (Lucide Icons)
- [x] 2026-01-26: Favicon SVG (symbol fali) + site.webmanifest
- [x] 2026-01-26: Google Analytics 4 (z cookie consent, RODO-compliant)
- [x] 2026-01-26: Baner cookie consent
- [x] 2026-01-26: Strona polityki prywatności (privacy.html)
- [x] 2026-01-26: Audyt bezpieczeństwa + poprawki (walidacja GA ID, noreferrer, referrer-policy)
- [x] 2026-01-26: SEO: robots.txt, sitemap.xml, canonical URL
- [x] 2026-01-26: Structured Data (JSON-LD): Person, ProfessionalService, WebSite
- [x] 2026-01-26: Open Graph + Twitter Cards + og-image.svg
- [x] 2026-01-26: Narzędzie PMAXTP (/tools/pmaxtp.html) - ukryte, dark mode
- [x] 2026-01-26: Plik wodowskazy.csv (/tools/wodowskazy.csv)
- [x] 2026-01-26: Strona 404.html
- [x] 2026-01-26: Zdjęcie profilowe (profile.jpg) w sekcji O mnie
- [x] 2026-01-26: Dane firmowe z CEIDG (NIP, REGON, adres, email)
- [x] 2026-01-26: Testy cross-browser + poprawki kompatybilności Safari
- [x] 2026-01-26: Połączenie z GitHub (https://github.com/Daldek/debever.pl)
- [x] 2026-01-26: GA4 Measurement ID skonfigurowany (G-3KHED211LP)
- [x] 2026-01-26: Deploy testowy na Mikrus (http://srv08.mikr.us:40693/)
- [x] 2026-01-26: Blog — skrypt build.py (Markdown → HTML)
- [x] 2026-01-26: Blog — szablon template.html dla wpisów
- [x] 2026-01-26: Blog — szablon index-template.html dla listy wpisów
- [x] 2026-01-26: Blog — style CSS dla bloga (sekcja Blog styles w style.css)
- [x] 2026-01-26: Blog — migracja 26 wpisów z WordPress do Markdown
- [x] 2026-01-26: Blog — wygenerowane 26 plików HTML + index.html
- [x] 2026-01-26: Nawigacja — dodany link do bloga
- [x] 2026-01-26: Sitemap — dodane 26 URL-i wpisów blogowych

## Następne kroki (TODO)
1. Dodać screenshoty do portfolio (5 obrazków w assets/images/portfolio/)
2. Wygenerować apple-touch-icon.png (180x180) z favicon.svg
3. Skonwertować og-image.svg na PNG (1200x630)
4. Deploy produkcyjny (SSL + domena debever.pl)
5. (Opcjonalnie) Pobrać obrazki z WordPress do blog/assets/images/

## Znane problemy / Blokery
- Brak screenshotów do portfolio (do dostarczenia przez właściciela)
- Brak apple-touch-icon.png (wygenerować z favicon.svg na realfavicongenerator.net)
- Brak og-image.png (skonwertować og-image.svg na PNG 1200x630)

## Decyzje projektowe
- 2026-01-26: Fonty — Google Fonts (Merriweather + Inter)
- 2026-01-26: Kolory dark mode — bg #0d1117, akcent #58a6ff (niebieski)
- 2026-01-26: BEM dla CSS (block__element--modifier)
- 2026-01-26: GitHub remote: https://github.com/Daldek/debever.pl

## Notatki dla przyszłej sesji
> Strona testowa działa na Mikrusie: http://srv08.mikr.us:40693/
> GA4 tymczasowo wyłączone (zakomentowane w index.html).
>
> **Blog:**
> - 26 wpisów z WordPress zmigrowanych do Markdown w blog/posts/
> - Skrypt `python3 blog/build.py` generuje pliki HTML
> - Po dodaniu/edycji wpisu uruchomić build.py ponownie
> - Zależności Python: pyyaml, markdown2
>
> Do deploymentu produkcyjnego:
> - Włączyć GA4
> - Skonfigurować SSL (Let's Encrypt)
> - Przekierować domenę debever.pl na Mikrusa
> - Zaktualizować nginx na port 80/443
>
> Aktualizacja strony na Mikrusie:
> ```
> cd /var/www/debever.pl && sudo git pull && python3 blog/build.py && sudo systemctl reload nginx
> ```
