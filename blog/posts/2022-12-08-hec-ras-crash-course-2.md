---
title: "HEC-RAS crash course #2, czyli o tym jak wyciągnąć cyferki z kolorowej mapy"
date: 2022-12-08
category: HEC-RAS
tags: [hec-ras, qgis, gis, modelowanie-hydrauliczne, tutorial]
excerpt: "Pierwsza część przyspieszonego kursu modelowania HEC-RAS obejmowała podstawy modelowania 2D. Ten artykuł pokazuje jak analizować wyniki."
---

## HEC-RAS 2D i QGIS

Pierwsza część przyspieszonego kursu modelowania HEC-RAS obejmowała podstawy modelowania 2D. Analiza wytworzyła dane o głębokościach wody, rzędnych zwierciadła wody i prędkościach przepływu — trzy podstawowe domyślne warstwy wynikowe.

HEC-RAS umożliwia tworzenie dodatkowych warstw, takich jak iloczyn prędkości i głębokości (DV), który pomaga identyfikować szczególnie niebezpieczne obszary dla ludzi, lub warstwy przydatne hydraulicznie jak liczby Froude'a czy Couranta.

## HEC-RAS na początek

Aby utworzyć dodatkowe warstwy map wynikowych:

1. Otwórz **Ras Mapper**
2. Rozwiń zakładkę **Results**
3. Kliknij prawym przyciskiem na nazwę planu i wybierz **Create a New Results Map Layer**
4. Rozwiń interesujący typ mapy
5. Wybierz wartości minimalne, maksymalne lub dla konkretnego kroku czasowego
6. Potwierdź klikając **Add map**
7. Oblicz/zaktualizuj zapisaną mapę klikając **Compute/Update Stored Map**

Dla wizualizacji DV zmodyfikuj ustawienia legendy w **Layer Properties**, ustawiając górny zakres na 2. Wartości powyżej 0,5 wskazują poważne ryzyko dla dorosłych.

## Przechodzimy do QGISa

Ras Mapper ma ograniczoną funkcjonalność GIS, więc eksportuj wyniki do formatu TIFF do dalszej pracy w QGIS.

Dla danych głębokości, rzędnych i prędkości kliknij prawym przyciskiem na warstwę, rozwiń **Export Layer** i wybierz **Export Raster**. Inne utworzone warstwy automatycznie zapisują się w odpowiednich formatach.

### Źródła danych o budynkach

- **OpenStreetMap** (pobierz z Geofabrik.de)
- **BDOT10k** (polska baza danych topograficznych, dostępna na Geoportal)

Zwróć uwagę na różnice w układach współrzędnych.

### Usuwamy to co zbędne

Ogranicz dane budynków do zasięgu modelu. Użyj **Extract by Location** z Processing Toolbox:

- **Extract features from:** warstwa budynków
- **Condition:** Intersect
- **By comparing to:** granica modelu 2D

### Analiza wyników

Przeanalizuj cztery parametry dla każdego budynku używając **Zonal Statistics**:

- Zalana powierzchnia (liczba komórek)
- Średnia, maksymalna i minimalna głębokość wody

### Wizualizacja wyników

Zmień symbolikę w **Properties → Symbology** z **Single Symbol** na **Rule-based**. Klasyfikuj na trzy kategorie:

| Kategoria | Warunek | Poziom ryzyka |
|-----------|---------|---------------|
| Wysoce zagrożone | "MAX" >= 0.3 m | Czerwony |
| Umiarkowanie zagrożone | "MAX" > 0.1 AND "MAX" < 0.3 m | Żółty |
| Bezpieczne | "MAX" <= 0.1 m | Zielony |

### Dodajemy etykiety

Dodaj etykiety w **Properties → Labels** z odpowiednim wyrażeniem dla zalanej powierzchni budynku.

**Uwaga dotycząca warstwy DV:** Tam gdzie są budynki, prędkość wody powinna być zerowa, więc wyświetlanie tam DV nie dodaje wartości.
