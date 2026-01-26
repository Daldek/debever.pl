# CLAUDE.md — Strona wizytówka debever.pl

## Kontekst projektu

Tworzysz statyczną stronę-wizytówkę dla **Piotra de Bevera** — inżyniera hydrologa i modelarza hydraulicznego prowadzącego jednoosobową działalność gospodarczą. Strona ma zastąpić obecny WordPress i służyć jako profesjonalna wizytówka do pozyskiwania klientów (biura projektowe, inwestorzy prywatni) oraz budowania wiarygodności wobec HR-ów.

### Właściciel projektu

- **Imię i nazwisko:** Piotr de Bever
- **Specjalizacja:** Hydrologia, modelowanie hydrauliczne, GIS, analiza danych
- **Lokalizacja:** Poznań, Polska
- **Strona docelowa:** https://debever.pl/
- **GitHub:** https://github.com/Daldek
- **LinkedIn:** https://www.linkedin.com/in/piotr-de-bever/

### Dane firmowe

```
Nazwa firmy: Piotr de Bever
NIP: 7773460753
REGON: 543702842
Adres: ul. Kazimierza Odnowiciela 6, 62-010 Pobiedziska
Email: kontakt@debever.pl
```

---

## Architektura projektu

### Stack technologiczny

- **Frontend:** Statyczny HTML5 + CSS3 + vanilla JavaScript (bez frameworków)
- **Styl:** Dark mode, czcionka serif, minimalistyczny design
- **Hosting:** Mikrus VPS (Debian)
- **Serwer WWW:** Do wyboru (nginx lub Apache — skonfigurować według potrzeb)
- **SSL:** Let's Encrypt (sprawdzić istniejący certyfikat lub wygenerować nowy)
- **Deployment:** Git (repozytorium GitHub + ręczny `git pull` na serwerze)

### Struktura katalogów

```
debever.pl/
├── index.html              # Strona główna (wizytówka)
├── blog/                   # Blog (Phase 2)
│   ├── index.html          # Lista wpisów
│   └── posts/              # Pojedyncze wpisy w HTML (z Markdown)
├── assets/
│   ├── css/
│   │   └── style.css       # Główny arkusz stylów
│   ├── js/
│   │   └── main.js         # Skrypty (jeśli potrzebne)
│   ├── images/
│   │   ├── profile.jpg     # Zdjęcie profilowe
│   │   └── portfolio/      # Screenshoty z projektów
│   └── fonts/              # Fonty (jeśli self-hosted)
├── CLAUDE.md               # Ten plik (specyfikacja projektu)
├── PROGRESS.md             # WAŻNE: Status prac, aktualizowany przez Claude Code
└── README.md               # Dokumentacja dla dewelopera
```

---

## Phase 1: Strona wizytówka

### Struktura strony głównej (index.html)

Strona typu one-page z płynnym scrollowaniem między sekcjami:

```
┌─────────────────────────────────────────┐
│ HEADER (sticky)                         │
│ Logo/Imię | Nav: Usługi|Portfolio|O mnie|Kontakt │
├─────────────────────────────────────────┤
│ HERO SECTION                            │
│ - Imię i nazwisko                       │
│ - Tagline: "Inżynier hydrolog |         │
│   Modelowanie hydrauliczne | GIS"       │
│ - CTA button: "Skontaktuj się"          │
├─────────────────────────────────────────┤
│ SEKCJA: USŁUGI                          │
│ 4 karty z ikonami:                      │
│ - Modelowanie hydrauliczne              │
│ - Analizy hydrologiczne                 │
│ - Analizy przestrzenne GIS              │
│ - Analiza danych                        │
├─────────────────────────────────────────┤
│ SEKCJA: PORTFOLIO                       │
│ 5 kafelków z miniaturami:               │
│ - Modelowanie 1D/2D (HEC-RAS, MIKE)     │
│ - Modelowanie 3D (TELEMAC)              │
│ - Modelowanie hydrologiczne             │
│ - Mapy zagrożenia powodziowego          │
│ - Ortofotomapy                          │
├─────────────────────────────────────────┤
│ SEKCJA: O MNIE                          │
│ - Zdjęcie profilowe (obecne z WP)       │
│ - Bio (2-3 akapity)                     │
│ - Doświadczenie: Sweco, WSP, Hydroprojekt│
│ - Wykształcenie: UP Wrocław             │
├─────────────────────────────────────────┤
│ SEKCJA: KONTAKT                         │
│ - Dane firmowe (NIP, adres)             │
│ - Email (mailto:)                       │
│ - LinkedIn, GitHub                      │
│ - Opcjonalnie: prosty formularz         │
├─────────────────────────────────────────┤
│ FOOTER                                  │
│ - Copyright                             │
│ - Link do bloga                         │
└─────────────────────────────────────────┘
```

### Treści do wykorzystania

#### Hero tagline
```
Piotr de Bever
Inżynier hydrolog · Modelowanie hydrauliczne · GIS
```

#### Usługi (opisy do kart)

1. **Modelowanie hydrauliczne**
   Modele 1D, 2D i 3D przepływu wody w korytach rzecznych, zbiornikach i na terenach zalewowych. Narzędzia: HEC-RAS, MIKE DHI, TELEMAC.

2. **Analizy hydrologiczne**
   Wyznaczanie zlewni, obliczanie hydrogramów odpływu, bilanse wodne, czasy koncentracji.

3. **Analizy przestrzenne GIS**
   Mapy zagrożenia powodziowego, przetwarzanie danych przestrzennych, analiza NMT.

4. **Analiza danych**
   Automatyzacja przetwarzania danych hydrologicznych i meteorologicznych, wizualizacja wyników, Python.

#### Portfolio (typy projektów)

1. **Modelowanie hydrauliczne 1D/2D**
   Analiza przepływu w korytach rzecznych i na terenach zalewowych z wykorzystaniem HEC-RAS i MIKE DHI.
   *[Screenshot: mapa zasięgu zalewu lub przekrój poprzeczny]*

2. **Modelowanie 3D**
   Zaawansowane symulacje przepływu z wykorzystaniem TELEMAC.
   *[Screenshot: wizualizacja 3D lub siatka obliczeniowa]*

3. **Modelowanie hydrologiczne**
   Wyznaczanie zlewni, hydrogramy odpływu, analiza opadów.
   *[Screenshot: mapa zlewni lub hydrogramy]*

4. **Mapy zagrożenia powodziowego**
   Analizy przestrzenne dla planowania przestrzennego i zarządzania ryzykiem.
   *[Screenshot: mapa zagrożenia z legendą]*

5. **Ortofotomapy**
   Przetwarzanie zdjęć z dronów, tworzenie ortofotomap w OpenDroneMap.
   *[Screenshot: ortofotomapa z drona]*

#### Bio (sekcja O mnie)

```
Absolwent Uniwersytetu Przyrodniczego we Wrocławiu (Inżynieria i Gospodarka Wodna). 
Specjalizuję się w modelowaniu hydraulicznym, pracując z narzędziami takimi jak 
HEC-RAS, MIKE DHI i TELEMAC.

Doświadczenie zdobywałem współpracując z wiodącymi firmami branży: Sweco, WSP Polska, 
WSP Sverige oraz Hydroprojekt Wrocław. Brałem udział w projektach zbiorników 
retencyjnych, regulacji rzek i analiz powodziowych.

Poza pracą komercyjną rozwijam narzędzia open-source do analiz hydrologicznych 
oraz tworzę materiały edukacyjne o modelowaniu hydraulicznym.
```

---

## Phase 2: Migracja bloga

### Zakres

Migracja obecnych wpisów z WordPress (debever.pl) do statycznego bloga pod `debever.pl/blog/`.

### Źródło treści

Obecne wpisy do zmigrowania (przykłady):
- Seria "HEC-RAS od zera" (5+ wpisów)
- "Czym jest zlewnia?"
- "Tworzenie siatki w BlueKenue"
- "Skąd brać dane do projektów?"
- Wpisy z kategorii Programming

### Format docelowy

1. **Wpisy w Markdown** — przechowywane w `/blog/posts/` jako `.md`
2. **Generator statyczny** — prosty skrypt (Python/Node) lub ręczna konwersja do HTML
3. **Szablon wpisu** — spójny z resztą strony (dark mode, serif)

### Struktura bloga

```
blog/
├── index.html              # Lista wpisów (najnowsze pierwsze)
├── posts/
│   ├── 2025-09-28-hec-ras-geometria.md
│   ├── 2025-09-08-hec-ras-interfejs.md
│   └── ...
└── assets/                 # Obrazki specyficzne dla bloga
```

### Schemat metadanych wpisu (frontmatter)

```yaml
---
title: "HEC-RAS od zera – tworzenie geometrii modelu"
date: 2025-09-28
category: [Hydraulics, HEC-RAS]
tags: [hec-ras, tutorial, modelowanie]
excerpt: "Omówienie tworzenia geometrii modelu w HEC-RAS..."
---
```

---

## Wytyczne projektowe

### Styl wizualny

| Element | Specyfikacja |
|---------|--------------|
| Motyw | Dark mode (ciemne tło, jasny tekst) |
| Tło główne | `#0d1117` lub `#1a1a2e` |
| Tło kart/sekcji | `#161b22` lub `#16213e` |
| Tekst główny | `#e6edf3` lub `#f0f0f0` |
| Akcent | Niebieski (#58a6ff) lub cyjan (#4cc9f0) — nawiązanie do wody |
| Typografia | Serif dla nagłówków (np. Merriweather, Playfair Display) |
| Typografia body | Sans-serif (np. Inter, Source Sans Pro) lub serif |

### Responsywność

- Mobile-first approach
- Breakpointy: 480px (mobile), 768px (tablet), 1024px (desktop)
- Menu hamburger na mobile
- Karty usług: 1 kolumna (mobile) → 2 kolumny (tablet) → 4 kolumny (desktop)

### Dostępność

- Semantyczny HTML5 (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`)
- Alt-texty dla wszystkich obrazków
- Kontrast tekstu zgodny z WCAG AA
- Focus states dla elementów interaktywnych

### Performance

- Brak frameworków JS (vanilla tylko)
- Optymalizacja obrazków (WebP gdzie możliwe)
- Minimalizacja CSS/JS w produkcji
- Lazy loading dla obrazków w portfolio

---

## Bezpieczeństwo

### Hardening serwera WWW

#### Nagłówki bezpieczeństwa (nginx)

```nginx
# Dodać do bloku server {}
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;

# Content Security Policy — dostosować do użytych zasobów
add_header Content-Security-Policy "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; frame-ancestors 'none'; base-uri 'self'; form-action 'self';" always;
```

#### SSL/TLS (Let's Encrypt + hardening)

```nginx
# Protokoły i szyfry
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;
ssl_prefer_server_ciphers off;

# HSTS (włączyć po potwierdzeniu działania SSL)
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;

# OCSP Stapling
ssl_stapling on;
ssl_stapling_verify on;
resolver 1.1.1.1 8.8.8.8 valid=300s;
```

#### Ochrona plików

```nginx
# Blokada dostępu do ukrytych plików i katalogów
location ~ /\. {
    deny all;
    access_log off;
    log_not_found off;
}

# Blokada dostępu do plików konfiguracyjnych
location ~* (CLAUDE\.md|README\.md|\.git|\.env)$ {
    deny all;
}

# Blokada listowania katalogów
autoindex off;
```

#### Przekierowanie HTTP → HTTPS

```nginx
server {
    listen 80;
    server_name debever.pl www.debever.pl;
    return 301 https://debever.pl$request_uri;
}

server {
    listen 443 ssl;
    server_name www.debever.pl;
    return 301 https://debever.pl$request_uri;
}
```

### Bezpieczeństwo formularza kontaktowego

Jeśli formularz kontaktowy będzie implementowany:

1. **Brak backendu** — formularz mailto: lub zewnętrzna usługa (Formspree, Netlify Forms)
2. **Jeśli własny backend:**
   - Rate limiting (max 5 wiadomości / IP / godzinę)
   - Honeypot field (ukryte pole — boty je wypełniają)
   - Walidacja server-side
   - Sanityzacja inputów
   - CSRF token

### Checklist bezpieczeństwa

- [ ] SSL certyfikat aktywny i auto-renewal (certbot)
- [ ] Nagłówki bezpieczeństwa skonfigurowane
- [ ] HTTP → HTTPS redirect
- [ ] Ukryte pliki zablokowane (.git, .env, CLAUDE.md)
- [ ] Brak listowania katalogów
- [ ] Regularne aktualizacje serwera (`apt update && apt upgrade`)
- [ ] Backup konfiguracji nginx
- [ ] Test na https://securityheaders.com/
- [ ] Test SSL na https://www.ssllabs.com/ssltest/

---

## Zarządzanie projektem i kontekstem

### WAŻNE: Ciągłość pracy Claude Code

Claude Code jest **jedynym developerem** tego projektu. Aby zapewnić ciągłość pracy w przypadku utraty kontekstu (nowa sesja, timeout, błąd):

#### Plik PROGRESS.md

W katalogu głównym repozytorium **ZAWSZE** utrzymuj aktualny plik `PROGRESS.md`:

```markdown
# Progress projektu debever.pl

## Ostatnia aktualizacja: [DATA I GODZINA]

## Aktualny status
- [ ] Phase 1: Wizytówka — W TRAKCIE / UKOŃCZONE
- [ ] Phase 2: Blog — NIE ROZPOCZĘTE / W TRAKCIE / UKOŃCZONE

## Co zostało zrobione
- [x] 2025-01-26: Utworzono repozytorium i strukturę katalogów
- [x] 2025-01-26: Szkielet HTML (index.html)
- [x] 2025-01-26: Style bazowe (reset, zmienne CSS, dark mode)
- [ ] ...

## Aktualnie w trakcie
> Pracuję nad: [KONKRETNE ZADANIE]
> Branch: develop
> Ostatni commit: [HASH] - [OPIS]

## Następne kroki (TODO)
1. [NAJBLIŻSZE ZADANIE]
2. [KOLEJNE ZADANIE]
3. ...

## Znane problemy / Blokery
- [OPIS PROBLEMU jeśli istnieje]

## Decyzje projektowe
- [DATA]: [DECYZJA I UZASADNIENIE]
- ...

## Notatki dla przyszłej sesji
> [Cokolwiek ważnego do zapamiętania — kontekst, ustalenia z właścicielem, itp.]
```

#### Zasady aktualizacji PROGRESS.md

1. **Aktualizuj na początku każdej sesji** — przeczytaj, zrozum kontekst
2. **Aktualizuj po każdym ZNACZĄCYM kroku** — nie po każdej linijce, ale po ukończeniu zadania
3. **Aktualizuj PRZED zakończeniem sesji** — zapisz gdzie skończyłeś i co dalej
4. **Commituj PROGRESS.md razem z kodem** — zawsze aktualny w repo

### Git workflow

#### Struktura branchy

```
main        ← Produkcja (tylko merge z develop, NIGDY direct push)
  │
  └── develop    ← Branch roboczy (cały development tutaj)
        │
        └── feature/nazwa   ← Opcjonalnie dla większych funkcji
```

#### Zasady commitowania

1. **Częste commity** — małe, atomowe zmiany (1 commit = 1 logiczna zmiana)
2. **Opisowe message** — format: `[SEKCJA] Krótki opis zmian`
   ```
   [HTML] Dodano szkielet sekcji Hero
   [CSS] Style dla kart usług + responsywność mobile
   [FIX] Poprawiono kontrast tekstu w footer
   [DOCS] Aktualizacja PROGRESS.md
   ```
3. **Commit PROGRESS.md** — przy każdej większej zmianie

#### Merge do main

```bash
# Na develop, po ukończeniu funkcjonalności:
git checkout main
git merge develop --no-ff -m "Merge: [OPIS CO ZOSTAŁO DODANE]"
git push origin main

# Wróć na develop do dalszej pracy:
git checkout develop
```

**Kiedy mergować do main:**
- Ukończona sekcja strony (np. cały Hero, całe Portfolio)
- Strona jest w stanie "deployowalnym" (nie zepsuta)
- Po testach responsywności

### Procedura rozpoczęcia nowej sesji

Gdy Claude Code rozpoczyna pracę (nowa sesja lub po przerwie):

```
1. git pull origin develop
2. Przeczytaj PROGRESS.md — zrozum aktualny stan
3. Przeczytaj CLAUDE.md — przypomnij sobie wymagania
4. Sprawdź ostatnie commity: git log --oneline -10
5. Kontynuuj od miejsca zapisanego w PROGRESS.md
```

### Procedura zakończenia sesji

Przed zakończeniem pracy:

```
1. Zapisz wszystkie zmiany
2. Zaktualizuj PROGRESS.md (status, co zrobione, co dalej)
3. git add .
4. git commit -m "[DOCS] Aktualizacja PROGRESS.md + [inne zmiany]"
5. git push origin develop
```

---

## Deployment

### Repozytorium

```
GitHub: https://github.com/Daldek/debever.pl (do utworzenia)
Branch produkcyjny: main
Branch roboczy: develop
```

### Workflow

1. Claude Code pushuje zmiany do `develop`
2. Po ukończeniu funkcjonalności — merge do `main`
3. SSH na Mikrus
4. `cd /var/www/debever.pl && git pull origin main`
5. Opcjonalnie: restart nginx jeśli zmiana konfiguracji

### Konfiguracja serwera (przykład nginx)

```nginx
server {
    listen 80;
    listen 443 ssl;
    server_name debever.pl www.debever.pl;
    
    root /var/www/debever.pl;
    index index.html;
    
    # SSL (Let's Encrypt)
    ssl_certificate /etc/letsencrypt/live/debever.pl/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/debever.pl/privkey.pem;
    
    location / {
        try_files $uri $uri/ =404;
    }
    
    # Cache static assets
    location ~* \.(css|js|jpg|jpeg|png|gif|ico|svg|woff|woff2)$ {
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

---

## Checklist implementacji

### Phase 0: Setup projektu

- [ ] Utworzyć repozytorium GitHub (Daldek/debever.pl)
- [ ] Utworzyć branch `develop`
- [ ] Utworzyć PROGRESS.md (szablon powyżej)
- [ ] Sklonować na Mikrus do `/var/www/debever.pl`
- [ ] Skonfigurować nginx (z nagłówkami bezpieczeństwa)
- [ ] Sprawdzić/odnowić certyfikat SSL
- [ ] Test bezpieczeństwa (securityheaders.com)

### Phase 1: Wizytówka

- [ ] Struktura katalogów (assets/, images/, css/, js/)
- [ ] index.html — szkielet HTML5 + meta tagi
- [ ] style.css — zmienne CSS, reset, dark mode base
- [ ] Sekcja Hero + CTA
- [ ] Sekcja Usługi (4 karty z ikonami)
- [ ] Sekcja Portfolio (5 kafelków) — placeholdery na screenshoty
- [ ] Sekcja O mnie — bio + zdjęcie
- [ ] Sekcja Kontakt — dane firmowe + linki
- [ ] Footer + link do bloga
- [ ] Nawigacja sticky + smooth scroll + hamburger mobile
- [ ] Responsywność (mobile 480px / tablet 768px / desktop 1024px)
- [ ] Favicon
- [ ] Testy cross-browser (Chrome, Firefox, Safari, mobile)
- [ ] Merge do main + deploy

### Phase 2: Blog

- [ ] Eksport treści z WordPress (XML lub scraping)
- [ ] Konwersja do Markdown z frontmatter
- [ ] Szablon wpisu HTML (blog/post-template.html)
- [ ] Lista wpisów (blog/index.html)
- [ ] Nawigacja między wpisami (poprzedni/następny)
- [ ] Integracja z główną stroną (link w nav i footer)
- [ ] Przekierowania ze starych URL-i (opcjonalnie, nginx rewrite)
- [ ] Merge do main + deploy

---

## Zasoby

### Obrazki do pobrania z obecnej strony

- Zdjęcie profilowe: `https://debever.pl/wp-content/uploads/2021/03/Autor.jpg`
- Ortofotomapa Szkudelniak: `https://debever.pl/wp-content/uploads/2023/04/Szkudelniak-scaled.jpg`
- Jaz Biezdruchowo: `https://debever.pl/wp-content/uploads/2024/02/Jaz-Biezdruchowo.jpg`

### Ikony

Użyć jednego z:
- Lucide Icons (https://lucide.dev/) — lekkie, MIT license
- Heroicons (https://heroicons.com/) — od Tailwind
- Feather Icons (https://feathericons.com/)

Sugerowane ikony dla usług:
- Modelowanie hydrauliczne: `waves` lub `droplets`
- Analizy hydrologiczne: `cloud-rain` lub `git-branch`
- GIS: `map` lub `layers`
- Analiza danych: `bar-chart` lub `trending-up`

### Fonty

Opcja 1 (Google Fonts):
```html
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

Opcja 2 (self-hosted dla performance):
Pobrać fonty i umieścić w `/assets/fonts/`

---

## Uwagi dla Claude Code

### Zarządzanie kontekstem (KRYTYCZNE)

1. **Zawsze zaczynaj od PROGRESS.md** — przeczytaj i zrozum stan projektu
2. **Zawsze aktualizuj PROGRESS.md** — przed zakończeniem sesji i po ważnych krokach
3. **Commituj często** — małe, atomowe zmiany z opisowymi message
4. **Pracuj na `develop`** — NIGDY nie pushuj bezpośrednio do `main`
5. **Merge do `main`** — tylko po ukończeniu funkcjonalności i testach

### Standardy kodu

6. **Nie wykonuj kodu automatycznie** — przedstaw propozycje i czekaj na akceptację
7. **Komentuj kod** — jasne opisy sekcji i funkcji
8. **Zachowaj spójność:**
   - Indentacja: 2 spacje
   - CSS: metodologia BEM (`.block__element--modifier`)
   - HTML: semantyczne tagi, atrybuty w kolejności alfabetycznej
9. **Testuj responsywność** — każda zmiana musi działać na mobile

### Bezpieczeństwo

10. **Dane firmowe** — zostaw placeholdery `[DO UZUPEŁNIENIA]`, właściciel uzupełni sam
11. **Nie commituj wrażliwych danych** — hasła, klucze API, prywatne dane
12. **Sprawdzaj konfigurację nginx** — przed deployem upewnij się, że nagłówki bezpieczeństwa działają

### Komunikacja

13. **W razie wątpliwości — pytaj** przed implementacją
14. **Dokumentuj decyzje** — w PROGRESS.md sekcja "Decyzje projektowe"

---

## Kontakt z właścicielem

W razie wątpliwości dotyczących:
- Treści/copywritingu
- Wyboru screenshotów do portfolio
- Danych firmowych
- Priorytetów funkcjonalności

→ Zapytaj przed implementacją.
