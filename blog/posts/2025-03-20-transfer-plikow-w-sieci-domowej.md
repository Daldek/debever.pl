---
title: "Transfer plików w sieci domowej"
date: 2025-03-20
category: Programming
tags: [python, http-server, sieć, transfer]
excerpt: "Praktyczny przewodnik jak szybko przesyłać pliki między komputerami w sieci domowej za pomocą wbudowanego serwera HTTP w Pythonie."
---

Nietypowo, ale muszę sobie gdzieś zapisać jak szybko przesyłać pliki między komputerami w sieci domowej.

## Instrukcja krok po kroku

### Krok 1: Otwórz wiersz poleceń

Otwórz Wiersz poleceń w folderze, który chcesz udostępnić. Najprościej wpisać "cmd" w pasku adresu eksploratora plików.

### Krok 2: Sprawdź adres IP komputera

Użyj polecenia:

```
ipconfig
```

Znajdź adres IPv4 (np. 192.168.1.2).

### Krok 3: Uruchom serwer HTTP Pythona

```
python -m http.server 8000
```

Domyślny port to 8000.

### Krok 4: Pobierz pliki z innego komputera

Na drugim komputerze otwórz przeglądarkę i wpisz adres:

```
192.168.1.2:8000
```

(zastąp adresem IP z kroku 2)

## Podsumowanie

Et voila! Nie trzeba szukać pendrive lub dysku zewnętrznego. Szybki i prosty sposób na transfer plików w sieci lokalnej.
