---
title: "HEC-RAS od zera – tworzenie geometrii modelu"
date: 2025-09-28
category: HEC-RAS
tags: [hec-ras, tutorial, modelowanie, geometria, hydraulika]
excerpt: "Ten poradnik kontynuuje serię HEC-RAS od zera, budując na poprzednim omówieniu interfejsu użytkownika."
---

## Wprowadzenie

Ten poradnik kontynuuje serię "HEC-RAS od zera", budując na poprzednim omówieniu interfejsu użytkownika. Choć RAS Mapper oferuje zaawansowane możliwości modelowania geometrii, ten przewodnik skupia się na podstawowym edytorze do tworzenia sieci hydrograficznej i przekrojów poprzecznych.

## Tworzenie nowego projektu

Uruchom HEC-RAS i przejdź do **File > New Project**. Wybierz katalog bez polskich znaków (ą, ę, itd.) w ścieżce. Wprowadź tytuł projektu i potwierdź. System wyświetli nazwę projektu, ścieżkę pliku i system jednostek — zalecane jest ustawienie **jednostek SI** jako domyślnych natychmiast po instalacji.

## Praca w edytorze geometrii

Wejdź do modułu geometrii klikając **View/Edit geometric data** z głównego okna.

### Sieć hydrograficzna

HEC-RAS pozwala na tworzenie złożonych sieci rzecznych, ale to ćwiczenie wykorzystuje pojedynczy odcinek. Narysowany kształt reprezentuje tylko schemat; rzeczywiste dane lokalizacji pochodzą z RAS Mapper. Aby dodać odcinek, wybierz **River Reach** z paska narzędzi i narysuj dwupunktową linię reprezentującą kierunek przepływu wody. Kliknij dwukrotnie, aby zakończyć, następnie nazwij rzekę i odcinek w wyświetlonym oknie dialogowym.

### Przekroje poprzeczne

Dodaj przekroje poprzeczne przez opcję **Cross Section** w lewym menu. Ten poradnik tworzy przekroje trapezoidalne z parametrami:

- Szerokość dna koryta: 8 m
- Głębokość: 2 m
- Nachylenie brzegu: 1:2.5
- Spadek zwierciadła wody: 0.0005
- Współczynnik Manninga n: 0.034

Użyj **Options > Add a New Cross Section**, aby określić lokalizację. Wprowadź współrzędne w tabeli **Cross Section Coordinates** (kolumny Station i Elevation). Utwórz profil czteropunktowy: 0;2, 5;0, 13;0, 18;2. Ustaw współczynnik Manninga n tylko w polu Channel. Zdefiniuj stacje lewego i prawego brzegu odpowiednio jako 0 i 18. Skopiuj przekroje do dodatkowych stacji rzecznych (100, 300, 400), dostosowując rzędne na podstawie spadku 5 cm na 100 m.

### Interpolacja przekrojów

Wróć do głównego edytora geometrii. Wybierz **Tools > XS Interpolation > Between 2 XS's**. Ustaw maksymalną odległość między przekrojami na 100 m, aby automatycznie wygenerować brakujące przekroje.

### Mosty

Mosty wymagają gęsto rozmieszczonych przekrojów. Dokumentacja zaleca cztery przekroje: dwa bezpośrednio powyżej i poniżej konstrukcji, plus dwa w strefach niezakłóconego przepływu powyżej i poniżej.

Interpoluj przekroje między stacjami 300–400 w odstępach 20 m dla mostu na stacji 350. W **Brdg/Culv** wybierz **Add a Bridge and/or Culvert**. W **Deck/Roadway** określ odległość do najbliższego przekroju powyżej i szerokość pomostu. Podaj współrzędne dla krawędzi górnej i dolnej, następnie skopiuj dane z góry na dół używając **Copy US to DS**.

Dodaj dwa filary w zakładce **Pier**, każdy o szerokości 1 m. Określ stację osi i podaj współrzędne dolnej i górnej rzędnej dla każdego.

### Budowle poprzeczne (jazy)

Interpoluj przekroje między stacjami 1–100 przed dodaniem budowli. Budowla poprzeczna wymaga odległości od poprzedniego przekroju, szerokości i współrzędnych rzędnych.

### Przepusty

Przepusty mogą towarzyszyć mostom lub być samodzielnymi budowlami. Parametry konfiguracji obejmują:

- Średnica: 0.5 m
- Odległość do przekroju powyżej: 7 m
- Długość: 6 m
- Współczynnik strat wlotowych: 0.5
- Współczynnik Manninga n (góra przepustu): 0.013
- Współczynnik Manninga n (dno przepustu): 0.03
- Zamulenie (od dna): 0.2 m
- Rzędna wlotu/wylotu: -0.15 m
- Stacja osi: 9 m

## Dopracowanie modelu

Ustandaryzuj odległości między wszystkimi przekrojami w równych odstępach. Dostosuj współczynniki kontrakcji i ekspansji w pobliżu budowli z 0.1 do 0.3 (i z 0.3 do 0.5) używając **Tables > Contraction/Expansion Coefficients (Steady Flow)**. Regularnie zapisuj pracę.
