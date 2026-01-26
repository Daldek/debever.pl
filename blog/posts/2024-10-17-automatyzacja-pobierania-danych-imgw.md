---
title: "O tym jak próbowałem zautomatyzować pobieranie danych z IMGW"
date: 2024-10-17
category: Programming
tags: [api, hydrology, imgw, meteorology, opendata, python]
excerpt: "Historia prób stworzenia narzędzia Python do automatyzacji pobierania publicznych danych z IMGW i napotkanych przy tym wyzwań."
---

Artykuł opisuje wyzwania napotkane podczas tworzenia narzędzia Python do automatyzacji pobierania publicznych danych z IMGW (Instytut Meteorologii i Gospodarki Wodnej).

## Ograniczenia API

API pozwala jedynie na pobieranie bieżących pomiarów bez dostępu do danych historycznych. System jest pełen niespójności:

- Niektóre endpointy akceptują nazwy stacji, inne wymagają wyłącznie ID
- Formaty odpowiedzi różnią się nieprzewidywalnie między słownikami a listami jednoelementowymi

## Problemy z danymi hydrologicznymi

Pliki historyczne dostarczane są jako CSV w archiwach ZIP, podzielone na formaty:

- Dobowe
- Miesięczne
- Połączone półroczne/roczne

Dane obejmują lata 1951-2023. Przed 2022 rokiem konwencje nazewnictwa były spójne. W 2023 usunięto numery miesięcy z nazw plików.

### Problemy z jakością danych

- Identyfikatory numeryczne zakodowane jako tekst
- Wiele reprezentacji brakujących wartości (puste komórki, 99.9, 9999, 99999.999)
- Spacje wiodące przed ID stacji
- Zmiana separatora z przecinka na średnik w 2023 roku

## Chaos danych meteorologicznych

Dane meteorologiczne są znacznie gorsze. Pliki używają niespójnych wielopoziomowych podziałów:

- Klimatologiczne
- Opadowe
- Synoptyczne

Konwencje nazewnictwa plików wydają się losowe, z komponentami pojawiającymi się na różnych pozycjach. Zawartość plików ZIP zmienia nazwy po ekstrakcji.

## Status projektu

Projekt rozwijam od września 2023 roku. Repozytorium dostępne jest na GitHub jako IMGWTools. Ostatnia motywacja pochodziła z powodzi na Odrze w 2023 roku oraz studiów podyplomowych z hydrologii na URK.

Jak mawiał Boromir: "Nie wchodzi się po prostu do Mordoru" - to pozornie proste zadanie okazało się nieoczekiwanie skomplikowane.
