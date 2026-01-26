---
title: "Windows – Debian – macOS"
date: 2026-01-12
category: Programming
tags: [windows, debian, macos, vnc, ssh, python, pyenv]
excerpt: "Po przejściu z Windows na macOS potrzebowałem dostępu do aplikacji niedostępnych na Macu. Rozwiązaniem było zainstalowanie Debiana na starszym komputerze."
---

Po przejściu z Windows na macOS potrzebowałem dostępu do aplikacji niedostępnych na Macu. Rozwiązaniem było zainstalowanie Debiana na starszym komputerze i uruchomienie Windows 10 jako maszyny wirtualnej.

## Połączenie pulpitu zdalnego

- Instalacja klienta VNC na Macu przez Homebrew: `brew install tiger-vnc`
- Konfiguracja tunelu SSH przez IPv4: `ssh -N -L 5901:127.0.0.1:5900 user@host`
- Uruchomienie przeglądarki VNC: `vncviewer 127.0.0.1:5901`
- Zakończenie sesji: Ctrl + C
- Sprawdzenie statusu tunelu: `lsof -iTCP:5901 -sTCP:LISTEN`
- Zakończenie procesu w razie potrzeby: `kill PID`

## Transfer plików: Mac do Debian

```bash
scp /ścieżka/do/pliku/na/macu.csv user@debianhost.local:/ścieżka/na/debianie
```

*(Wykorzystuje mDNS skonfigurowane z `avahi-daemon`)*

## Transfer plików: Debian do Windows

```bash
sftp user@192.168.122.1
get /ścieżka/do/pliku/na/debianie /ścieżka/do/pliku/na/Win
```

## Środowisko wirtualne Python (Pyenv)

- Ustawienie wersji Pythona: `pyenv local 3.12.12`
- Utworzenie środowiska: `python -m venv .venv`
- Aktywacja na macOS: `source .venv/bin/activate`
- Weryfikacja konfiguracji: `which python` i `python --version`
