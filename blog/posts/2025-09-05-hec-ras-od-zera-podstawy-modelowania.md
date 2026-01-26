---
title: "HEC-RAS od zera – podstawy modelowania ruchu wody"
date: 2025-09-05
category: HEC-RAS
tags: [hec-ras, tutorial, modelowanie, hydraulika, teoria]
excerpt: "Artykuł otwierający serię HEC-RAS od zera wyjaśnia klasyfikację modeli przepływu wody."
---

## Wprowadzenie

Ten artykuł otwierający serię "HEC-RAS od zera" wyjaśnia klasyfikację modeli przepływu wody. HEC-RAS służy jako narzędzie wśród wielu innych do obliczania ruchu wody, a zrozumienie różnych typów modeli, ich ograniczeń i prawidłowej interpretacji wyników jest niezbędne.

## Modele matematyczne

Modele matematyczne, takie jak te w HEC-RAS, MIKE by DHI i TELEMAC, stanowią znaczne uproszczenie rzeczywistości. Równoważą dokładność obliczeniową z kosztami rozwoju modelu i wymaganiami dotyczącymi zbierania danych.

Ta seria koncentruje się na przepływie w kanałach otwartych napędzanym siłami grawitacyjnymi, charakteryzującym się swobodną powierzchnią wody. Takie warunki występują w rzekach, kanałach i częściowo wypełnionych przewodach.

## Rodzaje ruchu wody

Przepływ w kanałach otwartych dzieli się na dwie główne kategorie:

- **Przepływ ustalony** – wszystkie parametry pozostają stałe w czasie
- **Przepływ nieustalony** – przepływ, prędkość i głębokość zmieniają się w czasie

Każda kategoria dzieli się dalej na:

### 1. Przepływ ustalony równomierny

Parametry stałe w czasie i przestrzeni. Wyobraź sobie długi kanał ze stałym dopływem, gdzie warunki hydrauliczne całkowicie się stabilizują.

### 2. Przepływ ustalony nierównomierny

Parametry stałe w czasie, ale zmienne przestrzennie. Na przykład kanał z jazem powodującym spiętrzenie wody — stały dopływ, ale zmieniające się warunki hydrauliczne wzdłuż kanału.

### 3. Przepływ nieustalony równomierny

Przepływ zmienia się w czasie, podczas gdy parametry przestrzenne pozostają stałe — rzadko obserwowany praktycznie, ale teoretycznie ważny.

### 4. Przepływ nieustalony nierównomierny

Parametry zmieniają się zarówno w czasie, jak i przestrzennie — najbardziej "naturalny" scenariusz ze zmieniającym się przepływem i warunkami hydraulicznymi.

## Głębokość krytyczna

Ruch nierównomierny dzieli się dalej na łagodnie zmienny, gwałtownie zmienny, spokojny i rwący. Rozróżnienie między przepływem spokojnym a rwącym zależy od **głębokości krytycznej**:

> "Głębokość krytyczna reprezentuje głębokość, przy której energia osiąga minimum dla danego przepływu, lub odwrotnie, przepływ osiąga maksimum dla danej energii."

Ten punkt równowagi między energią potencjalną a kinetyczną określa, czy przepływ jest **spokojny (podkrytyczny)** czy **rwący (nadkrytyczny)**.

*Uwaga: Literatura anglojęzyczna odwraca terminologię — subcritical odnosi się do przepływu spokojnego, supercritical do rwącego.*

## Klasyfikacja modeli

### Podejścia obliczeniowe

**Modele CFD** (Computational Fluid Dynamics) oparte na równaniach Naviera-Stokesa produkują imponujące wizualizacje 3D. Jednak ich złożoność obliczeniowa zazwyczaj ogranicza zastosowanie do pojedynczych budowli podczas faz projektowych.

**Modele równań Saint-Venanta**, choć prostsze, skutecznie opisują przepływ łagodnie zmienny w kanałach otwartych. HEC-RAS i większość modeli 1D wykorzystuje to podejście.

### Praktyczne typy modeli

Z praktycznej perspektywy inżynierskiej:

- **1D (jednowymiarowy)** – Prędkość uśredniona w całym przekroju; przepływ opisany tylko wzdłuż osi kanału.
- **2DH (dwuwymiarowy horyzontalny)** – Składowe prędkości poziomej (u,v) z parametrami uśrednionymi po głębokości.
- **2DV (dwuwymiarowy pionowy)** – Rozkład prędkości z głębokością i wzdłuż kanału; uśrednianie poprzeczne.
- **3D (trójwymiarowy)** – Pełny opis prędkości (u,v,w) przy użyciu hydrostatycznych równań Naviera-Stokesa.

### Porównanie charakterystyk modeli

| Typ modelu | Założenia | Zalety | Ograniczenia | Zastosowania |
|---|---|---|---|---|
| **1D** | Prędkość uśredniona w przekroju; przepływ tylko wzdłuż osi | Szybkie obliczenia; minimalne wymagania danych; prosta interpretacja | Brak informacji o rozkładzie prędkości; zakłada przepływ wzdłuż osi | Profile zwierciadła wody; zasięg powodzi; projektowanie mostów/przepustów |
| **2DH** | Składowe prędkości poziomej; uśrednienie po głębokości | Realistyczne mapy zalewowe; dobra reprezentacja terenów zalewowych | Wyższe wymagania obliczeniowe; potrzeba rozległych danych terenowych | Mapy zalewowe; analiza awarii zapór; estuaria |
| **2DV** | Rozkład prędkości po głębokości i wzdłuż kanału | Analizuje zjawiska pionowe (stratyfikacja, efekty dna) | Trudne zastosowanie praktyczne; ograniczona dostępność oprogramowania | Badania laboratoryjne |
| **3D** | Pełny opis prędkości w przestrzeni; hydrostatyczne równania N-S | Najdokładniejszy opis zjawisk; możliwa analiza cyrkulacji i mieszania | Ekstremalne wymagania obliczeniowe; rozległe dane wejściowe | Zbiorniki; estuaria; jakość wody; transport zanieczyszczeń |
