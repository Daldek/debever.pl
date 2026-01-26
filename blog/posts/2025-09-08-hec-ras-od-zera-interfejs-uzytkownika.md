---
title: "HEC-RAS od zera – interfejs użytkownika w programie HEC-RAS"
date: 2025-09-08
category: HEC-RAS
tags: [hec-ras, tutorial, interfejs, hydraulika]
excerpt: "Omówienie odświeżonej wersji HEC-RAS z października, zauważając że najnowsza stabilna wersja to 6.6."
---

## Wprowadzenie

Autor omawia odświeżoną wersję HEC-RAS z października, zauważając że "najnowsza stabilna wersja to 6.6, która wciąż opiera się na dobrze znanym, dość archaicznym interfejsie użytkownika."

## Główne okno programu

Podstawowy interfejs wyświetla pustą przestrzeń roboczą przy pierwszym uruchomieniu. Użytkownicy mogą skonfigurować, czy automatycznie ładować ostatni model. Prawy dolny róg pokazuje ustawienia jednostek, domyślnie jednostki SI zamiast amerykańskiego systemu imperialnego.

## Podstawowe pliki projektu

Cztery podstawowe komponenty projektu są wymagane do symulacji:

- **Project (.prj)**: Główny plik kontrolujący cały projekt
- **Plan (.pXX)**: Zarządza konkretnymi symulacjami z kombinacjami przepływu/geometrii
- **Geometry (.gXX)**: Zawiera dane sieci i przekrojów poprzecznych
- **Typy przepływu**: Kategoryzowane jako ustalony, nieustalony lub quasi-nieustalony

Elementy opcjonalne obejmują opisy projektu i dane osadów (.sXX).

## Ikony paska narzędzi i grupy narzędzi

Interfejs organizuje funkcje w kilka grup ikon:

### Zarządzanie projektem
- Otwieranie istniejących projektów
- Zapisywanie zmian

### Definicja modelu (4 ikony)
- Podgląd/edycja danych geometrycznych
- Podgląd/edycja danych przepływu ustalonego
- Podgląd/edycja danych przepływu quasi-nieustalonego
- Podgląd/edycja danych przepływu nieustalonego

### Sedymentacja i jakość wody
- Warunki brzegowe sedymentacji
- Parametry jakości wody

### Narzędzia specjalistyczne
- RasMapper: Narzędzie GIS do przygotowania geometrii i wizualizacji wyników 2D
- Moduły analizy dla przekrojów, profili, krzywych konsumpcyjnych i hydrogramów

### Analiza wyników
- Tabele właściwości hydraulicznych
- Szczegółowe wyniki obliczeń
- Tabele podsumowujące wyniki
- Przeglądarka danych DSS

## Moduł View/Edit Geometric Data

Ten najbardziej kompleksowy moduł zawiera kolumnę "Editors" ze specjalistycznymi narzędziami.

### Kluczowe komponenty

- **Junct.**: Węzły sieci umożliwiające złożone konfiguracje rzeczne
- **Cross Section**: Definiowanie danych pomiarowych włącznie z rzędnymi, współczynnikami szorstkości i współczynnikami kontrakcji/ekspansji
- **Brdg/Culv**: Konfiguracja mostów i przepustów z geometrią pomostu i filarów
- **Inline Structure**: Modelowanie budowli blokujących przepływ
- **Lateral Structure**: Definiowanie budowli wzdłuż koryt rzecznych
- **Storage Area**: Definiowanie stref retencji
- **2D flow Area**: Tworzenie domen obliczeniowych 2D
- **Pump Station**: Modelowanie obiektów pompowych

### Menu Tools (głównie dla modeli 2D)

- Tworzenie River Reach
- Obszary retencji
- Obszary przepływu 2D
- Linie warunków brzegowych
- Linie łamania dla zgodności siatki
- Strefy szorstkości Manninga
- Warstwy map tła
