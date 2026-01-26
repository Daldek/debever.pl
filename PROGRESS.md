# Progress projektu debever.pl

## Ostatnia aktualizacja: 2026-01-26 (sesja 2)

## Aktualny status
- [ ] Phase 1: Wizytówka — W TRAKCIE (szkielet gotowy)
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

## Aktualnie w trakcie
> Sesja 1 zakończona. Setup projektu kompletny.
> Branch: develop
> Ostatni commit: [HTML] Szkielet index.html + [CSS] Bazowe style

## Następne kroki (TODO)
1. Uzupełnić GA4 Measurement ID w index.html (linia z G-XXXXXXXXXX)
2. Wygenerować apple-touch-icon.png (180x180) z SVG
3. Dodać zdjęcie profilowe (O mnie)
3. Dodać screenshoty do portfolio
4. Uzupełnić dane firmowe (NIP, adres, email, telefon)
5. Dodać favicon
6. Testy cross-browser
7. Połączyć z GitHub remote
8. Deploy na Mikrus VPS

## Znane problemy / Blokery
- Brak screenshotów do portfolio (do dostarczenia przez właściciela)
- Dane firmowe placeholder [DO UZUPEŁNIENIA]
- Brak apple-touch-icon.png (wygenerować z favicon.svg na realfavicongenerator.net)

## Decyzje projektowe
- 2026-01-26: GitHub — pomijamy na razie, praca lokalna
- 2026-01-26: Fonty — Google Fonts (Merriweather + Inter)
- 2026-01-26: Kolory dark mode — bg #0d1117, akcent #58a6ff (niebieski)
- 2026-01-26: BEM dla CSS (block__element--modifier)

## Notatki dla przyszłej sesji
> Setup projektu ukończony. Strona ma kompletny szkielet HTML z wszystkimi sekcjami.
> CSS obsługuje responsywność (1/2/4 kolumny) i mobile menu.
>
> Do zrobienia w kolejnej sesji:
> - Ikony SVG dla usług
> - Obrazki (profile.jpg, portfolio/)
> - Dane firmowe od właściciela
> - GitHub remote + pierwszy deploy
