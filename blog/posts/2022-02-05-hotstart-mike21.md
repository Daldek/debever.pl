---
title: "Hotstart, czyli jak uratować przerwaną symulację w Mike21?"
date: 2022-02-05
category: Hydraulics
tags: [mike21, hotstart, symulacja, modelowanie-hydrauliczne]
excerpt: "Artykuł wyjaśnia jak wykorzystać pliki hotstart do wznowienia przerwanej symulacji hydrodynamicznej w oprogramowaniu Mike21."
---

## Scenariusz

Miesięczna symulacja spływu powierzchniowego modelująca opad Chicago Design Storm (CDS) z prawdopodobieństwem przekroczenia 1% przestała zapisywać wyniki do pliku Dfs2. Zamiast restartować całą symulację od początku, tworzymy plik hotstart, aby kontynuować od ostatniego obliczonego stanu.

## Kroki do wykonania

### 1. Modyfikacja w Data Utility

Zmień parametr Data Type z 0 na 1 w narzędziu Data Utility w Mike Zero.

### 2. Generowanie pliku Hotstart

Użyj narzędzia "Hot start File Generator" w Mike21. Upewnij się, że uwzględnione są trzy parametry:

- Water Depth
- Flow Flux P
- Flow Flux Q

### 3. Aktualizacja pliku symulacji

Zmodyfikuj oryginalny plik .m21:

- Przełącz z "Cold start" na "Hot start"
- Dostosuj okres symulacji i interwały zapisu wyników
- Przelicz Eddy Viscosity według wzoru:

```
E = 0.02 × (Δx²/Δt)
```

## Uwagi techniczne

Artykuł zawiera uwagi o praktykach niezalecanych przez DHI, niepewności parametrów (oznaczone gwiazdkami) oraz nierozwiązane pytania dotyczące zmiennych modułu infiltracji.

Osiem zrzutów ekranu dokumentuje proces przez kroki interfejsu Mike Zero.
