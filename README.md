# DEPRECATED
Dieses Projekt wird nicht mehr weiterentwickelt. Der Nachfolger findet sich hier: [DaSCR-Machine](https://github.com/dascr/dascr-machine), [dascr.org](https://dascr.org)

# dARts
Dieses Projekt soll eine E-Dart Scheibe in Automatenqualität, wie zum Beispiel dem Löwen Darts HB8 mit dem Scoreboard Dart-O-Mat 3000 vereinen (WICHTIG: dart-o-mat-3000 BRANCH "dARts" verwenden!). Die volle Dokumentation findet man hier:  
[https://darts.readthedocs.io/en/latest/](https://darts.readthedocs.io/en/latest/)  
[![Documentation Status](https://readthedocs.org/projects/darts/badge/?version=latest)](https://darts.readthedocs.io/en/latest/?badge=latest)  
Wer gerne ein eiskaltes Bier spendieren möchte kann das hier tun:  
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate/?hosted_button_id=W2KPLBLTVYK3A)


# Hardware
Die Hardware besteht aus einem Ersatzteile Satz für einen Löwen Darts Automaten inklusive Matrix, Spinne, Segmente, ... und außerdem aus einem Arduino Mega 2560 mit Programm und schlussendlich einem Raspberry PI für die Kommunikation mit dem Scoreboard.

# Scoreboard
Das Scoreboard ist nicht mit eingeschlossen und kann <a href="https://github.com/patrickhener/dart-o-mat-3000/tree/dARts" target="_blank">hier</a> gefunden werden. Die Software kann auf dem Raspberry PI des Projektes mitbetrieben werden.

# Projektordner und Inhalte
Dieses Projekt besteht aus mehreren Ordnern mit unterschiedlichen Inhalten.

## arduino
Hierin sind Beispiel Sketches für den Arduino enthalten

## pcb_gerber
Hierin befindet sich eine Gerber Datei mit einem PCB Design für das Bestellen einer vorgefertigten Leiterplatine.

## python
Hierin enthalten ist der Koppler Script, der den Arduino mit dem Dart-O-Mat 3000 verbindet.

## system
Hierin befinden sich Konfigurationsdateien für das Setup eines WLAN Hotspots mit DHCP, DNS und Captive Portal

# Demo

Hier gibt es die Demo Videos:

## Spiel einstellen
[![Spiel einstellen](https://img.youtube.com/vi/NGI12focr8E/0.jpg)](https://www.youtube.com/watch?v=NGI12focr8E)

## 301 Spiel
[![301](https://img.youtube.com/vi/cbdSK9wNLu8/0.jpg)](https://www.youtube.com/watch?v=cbdSK9wNLu8)

## Cricket Spiel
[![Cricket](https://img.youtube.com/vi/CJ5lnEe3wmM/0.jpg)](https://www.youtube.com/watch?v=CJ5lnEe3wmM)
