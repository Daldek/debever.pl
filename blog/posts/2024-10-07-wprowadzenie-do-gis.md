---
title: "Wprowadzenie do GIS"
date: 2024-10-07
category: GIS
tags: [gis, dane-przestrzenne, qgis, arcgis]
excerpt: "Systemy Informacji Geograficznej (GIS) to potężne narzędzia do analizy przestrzennej, stosowane w codziennym życiu."
---

Systemy Informacji Geograficznej (GIS) to potężne narzędzia do analizy przestrzennej, stosowane w codziennym życiu — od nawigacji mapowej po analizy zagrożeń naturalnych.

## Co to jest GIS?

GIS to system do gromadzenia, przetwarzania, analizy i wizualizacji danych przestrzennych. Łączy dane dotyczące lokalizacji (współrzędnych geograficznych) z informacjami opisowymi. Popularne aplikacje to Google Maps, QGIS i ArcGIS.

## GIS w codziennym życiu

GIS jest wszechobecny — nawigacja w smartfonach, analiza terenu dla bezpieczeństwa, poszukiwanie optymalnych punktów widokowych. Numeryczne modele terenu (DEM) i analiza widoczności to praktyczne zastosowania.

## Dane wektorowe i rastrowe w GIS

### Dane wektorowe

- **Punkty**: lokalizacje w przestrzeni (x, y)
- **Linie**: obiekty z długością (rzeki, drogi, ścieżki)
- **Poligony**: obszary zamknięte (parki, jeziora, działki)

Idealne do obiektów o wyraźnych granicach.

### Dane rastrowe

Siatka pikseli reprezentująca zjawiska ciągłe:

- Modele wysokościowe terenu (DEM)
- Pokrywa roślinna
- Dane atmosferyczne

## Formaty danych w GIS

### Shapefile

Klasyczny format (.shp) od lat 90., przechowuje dane wektorowe. Ograniczenia: maksymalnie 2 GB, limit 255 kolumn, brak wsparcia dla topologii.

### GeoPackage

Nowoczesna alternatywa (.gpkg) bez limitów wielkości pliku. Obsługuje zarówno dane wektorowe, jak i rastrowe w jednym pliku. Bazuje na SQLite, zapewniając wydajność.

### Geobazy w ArcGIS

- **File Geodatabase (GDB)**: do 1 TB, idealna dla dużych projektów
- **Enterprise Geodatabase**: dostęp wieloużytkownikowy
- **Personal Geodatabase**: przestarzała, limit 2 GB

### Inne formaty

- **CSV/TXT**: pliki tekstowe z danymi atrybutowymi
- **KML/KMZ**: wizualizacja w Google Earth
- **GeoJSON**: format webowy oparty na JSON
- **PostGIS**: rozszerzenie PostgreSQL
- **GeoTIFF**: dane rastrowe z georeferencją

## Usługi WMS, WMTS i WFS

### WMS (Web Map Service)

Dostarcza mapy jako obrazy rastrowe (PNG, JPEG). Brak możliwości edycji danych, automatyczne skalowanie.

### WMTS (Web Map Tile Service)

Mapa w postaci predefiniowanych kafelków. Szybsze ładowanie niż WMS, ale ograniczone do ustalonych skal.

### WFS (Web Feature Service)

Udostępnia rzeczywiste dane wektorowe z możliwością edycji. Obsługuje filtry przestrzenne i atrybutowe. Idealny do zaawansowanych analiz.

## Podsumowanie

GIS to wszechstronne narzędzie do analizy danych geograficznych. Wybór formatu danych (Shapefile, GeoPackage, geobazy) zależy od wymagań projektu. Usługi WMS/WMTS są idealne do podglądów map, WFS umożliwia pełną pracę z danymi wektorowymi.
