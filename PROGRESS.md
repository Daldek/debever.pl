# Progress projektu debever.pl

## Ostatnia aktualizacja: 2026-01-26 (sesja 2 zakończona)

## Aktualny status
- [ ] Phase 1: Wizytówka — W TRAKCIE (90% gotowe, brakuje portfolio)
- [ ] Phase 2: Blog — NIE ROZPOCZĘTE

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

## Następne kroki (TODO)
1. Uzupełnić GA4 Measurement ID w index.html (linia z G-XXXXXXXXXX)
2. Dodać screenshoty do portfolio (5 obrazków w assets/images/portfolio/)
3. Wygenerować apple-touch-icon.png (180x180) z favicon.svg
4. Skonwertować og-image.svg na PNG (1200x630)
5. Testy cross-browser
6. Połączyć z GitHub remote
7. Deploy na Mikrus VPS (konfiguracja nginx + SSL)

## Znane problemy / Blokery
- Brak screenshotów do portfolio (do dostarczenia przez właściciela)
- Brak apple-touch-icon.png (wygenerować z favicon.svg na realfavicongenerator.net)
- Brak og-image.png (skonwertować og-image.svg na PNG 1200x630)

## Decyzje projektowe
- 2026-01-26: GitHub — pomijamy na razie, praca lokalna
- 2026-01-26: Fonty — Google Fonts (Merriweather + Inter)
- 2026-01-26: Kolory dark mode — bg #0d1117, akcent #58a6ff (niebieski)
- 2026-01-26: BEM dla CSS (block__element--modifier)

## Notatki dla przyszłej sesji
> Strona prawie gotowa do deploymentu. Brakuje tylko:
> - Screenshotów do portfolio (5 obrazków)
> - GA4 Measurement ID
> - Konwersja SVG → PNG (favicon, og-image)
>
> Strona może być wdrożona bez portfolio — kafelki będą miały placeholdery.
> Narzędzia Python w przyszłości: subdomeny lub ścieżki, potrzebny gunicorn + nginx reverse proxy.
