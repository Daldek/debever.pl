---
title: "HEC-RAS crash course #1, czyli o supremacji modeli 2D nad 1D"
date: 2022-11-21
category: HEC-RAS
tags: [hec-ras, 2d, qgis, modelowanie-hydrauliczne, tutorial]
excerpt: "Druga zwrotka bo zawsze chciałem zacząć od środka. Rozpoczynając pracę z modelowaniem hydraulicznym, preferowałem szybkie przejście do modeli 2D."
---

> Druga zwrotka bo zawsze chciałem zacząć od środka ~Abradab

## Dlaczego nie lubię modeli 1D?

Rozpoczynając pracę z modelowaniem hydraulicznym, preferowałem szybkie przejście do modeli dwuwymiarowych, postrzegając podejście jednowymiarowe jako uproszczone i przestarzałe.

Jednak doświadczenie ujawniło, że "modele 1D mogą być zaskakująco wymagające, szczególnie gdy sieci rzeczne są złożone, rozgałęziające się, ponownie łączące, z przelewaniem przez wały lub nasypami drogowymi."

### Ale czy zawsze jest gorsze niż 2D?

Chociaż modele 1D mają ograniczenia, pozostają użyteczne w specyficznych scenariuszach — takich jak proponowanie wielu wariantów rozwiązań lub dostarczanie skalibrowanych wartości dla zaawansowanych modeli.

"Zrozumienie podstaw hydrauliki jest niezbędne do kompetentnego modelowania zarówno w 1D jak i 2D."

## Budowanie modelu

Model koncentruje się na Białogardzie w północno-zachodniej Polsce, położonym na rzece Parsęcie w kilometrze 61, gdzie zbiega się dopływ Liśnica. Obszar badań rozciąga się od km 59 do km 61,5.

### Numeryczny Model Terenu

Struktura organizacyjna jest niezbędna. Zalecam tworzenie folderów:

```
Parseta
├─ GIS
│  ├─ Input
│  └─ Shp
└─ HEC-RAS
```

### Modelarz to też GISowiec

Utwórz nowy projekt QGIS używając układu współrzędnych PUWG 1992 (EPSG:2180). Pobierz i zintegruj Numeryczny Model Terenu ze zmodyfikowaną symboliką i cieniowaniem.

### Wyznaczanie granic modelu

Narysuj granice poligonowe dla obszaru modelu 2D i polilinie osi rzeki. "Preferowane są proste kształty bez nadmiernych zakrętów, chociaż osie rzek powinny być dokładnie odwzorowane."

Zapisz je jako Shapefiles — HEC-RAS nie akceptuje innych formatów wektorowych.

### Czas na HEC-RASa

Przed kontynuacją zweryfikuj, że regionalne ustawienia systemu używają kropek (nie przecinków) jako separatorów dziesiętnych. Uruchom HEC-RAS i wybierz jednostki SI z menu Options.

### Czy RAS Mapper to alternatywa dla programów GIS?

"RAS Mapper to niedorozwinięte oprogramowanie GIS, którego nie należy traktować poważnie." Jednak ponieważ krytyczne przygotowanie danych odbyło się w QGIS, użycie RAS Mapper będzie ograniczone do generowania siatki, umieszczania warunków brzegowych, korygowania błędów i definiowania parametrów symulacji.

### Geometria

W RAS Mapper utwórz nową geometrię i zaimportuj granice z shapefile. Skonfiguruj parametry obliczeniowe:

- Cell Size X i Y: 6 metrów
- Generate as Hexagon: zaznaczone
- Dla Breaklines ustaw Near Spacing na 3 metry

### Warunki brzegowe modelu

Skonfiguruj dwa górne warunki brzegowe jako "Flow Hydrograph":

- Liśnica: 10 m³/s
- Parsęta: 60 m³/s

Ustaw dolny warunek brzegowy jako "Normal depth" ze spadkiem 0.001.

### Obliczenia przepływów nieustalonych

Wybierz wszystkie programy obliczeniowe oprócz "Sediment". W Computation Settings ustaw:

- Time steps: 5 minut
- Computation Interval: 5 sekund

Kliknij "Compute" i czekaj na wyniki. Wyniki można wizualizować w RAS Mapper z możliwością animowanego odtwarzania.

**Dalsze zasoby:** [HEC-RAS training. 2D Unsteady Flow (2021)](https://www.hec.usace.army.mil/confluence/rasdocs/rastraining/latest/hec-ras-classes/2d-unsteady-flow-2021)
