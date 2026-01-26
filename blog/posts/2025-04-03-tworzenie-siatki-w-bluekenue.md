---
title: "Tworzenie siatki w BlueKenue"
date: 2025-04-03
category: Telemac
tags: [bluekenue, hydraulics, telemac, mesh, siatka]
excerpt: "Przewodnik krok po kroku do przygotowania siatek obliczeniowych w BlueKenue dla modelowania 2D i 3D w oprogramowaniu TELEMAC."
---

Ten artykuł przedstawia przewodnik krok po kroku do przygotowania siatek obliczeniowych w BlueKenue dla modelowania 2D i 3D w oprogramowaniu TELEMAC. Wpis jest w trakcie rozwoju, w miarę jak uczę się tej platformy.

## Etapy przygotowania siatki

Cały proces obejmuje 26 kolejnych kroków:

### Konfiguracja początkowa (Kroki 1-4)

1. Utworzenie shapefiles z granicami wielokątów i specyfikacją rozmiaru siatki
2. Import do BlueKenue przez "File → Import → ArcView Shape File"

### Konwersja formatów (Kroki 5-7)

3. Eksport shapefiles jako pliki i2s (2D Line Set)
4. Przygotowanie generatora siatki przez "File → New → T3 Mesh Generator"

### Konfiguracja siatki (Kroki 8-12)

5. Ustawienie domyślnych parametrów długości krawędzi
6. Organizacja regionów modelu w kategorie:
   - "Outline" - kontur zewnętrzny
   - "Density" - strefy zagęszczenia siatki
   - "SoftLines" - linie łamania
7. Wykonanie generowania siatki

### Integracja batymetrii (Kroki 13-22)

8. Konwersja wygenerowanych siatek do formatu t3s
9. Utworzenie obiektów Selafin
10. Interpolacja danych batymetrycznych z plików XYZ na siatkę

### Warunki brzegowe (Kroki 23-26)

11. Definiowanie warunków brzegowych przez "File → New → Boundary conditions"
12. Eksport jako pliki bc2 i cli

## Uwagi techniczne

**Ważne:** BlueKenue ma trudności z prawidłową interpretacją wielokątów z otworami. Wymaga to oddzielnego traktowania obszarów wykluczonych, takich jak wyspy.

## Przydatne zasoby

- Tutorial na YouTube: "Generating mesh and geometry (selafin, *.slf) file for TELEMAC-2D using Bluekenue"
- Materiały edukacyjne: TELEMAC — Hydro-Informatics website
