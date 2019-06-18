# dARts
Dieses Projekt soll eine E-Dart Scheibe in Automatenqualität, wie zum Beispiel dem Löwen Darts HB8 mit dem Scoreboard Dart-O-Mat 3000 vereinen. Die volle Dokumentation findet man hier: [https://darts.readthedocs.io/en/latest/](https://darts.readthedocs.io/en/latest/)[![Dokumentationsstatus](https://readthedocs.org/projects/dARts/badge/?version=latest)](https://darts.readthedocs.io/en/latest/)

# Hardware
Die Hardware besteht aus einem Ersatzteile Satz für einen Löwen Darts Automaten inklusive Matrix, Spinne, Segmente, ... und außerdem aus einem Arduino Mega 2560 mit Programm und schlussendlich einem Raspberry PI für die Kommunikation mit dem Scoreboard.

# Scoreboard
Das Scoreboard ist nicht mit eingeschlossen und kann <a href="https://github.com/patrickhener/dart-o-mat-3000" target="_blank">hier</a> gefunden werden. Die Software kann auf dem Raspberry PI des Projektes mitbetrieben werden.

# Projektordner und Inhalte
Dieses Projekt besteht aus mehreren Ordnern mit unterschiedlichen Inhalten.

## arduino
Hierin sind Beispiel Sketches für den Arduino enthalten

## debug
Hierin ist ein Modul enthalten mit dem man den Script auch ohne Arduino testen und weiterentwickeln kann.

## pcb_gerber
Hierin befindet sich eine Gerber Datei mit einem PCB Design für das Bestellen einer vorgefertigten Leiterplatine.

## python
Hierin enthalten ist der Koppler Script, der den Arduino mit dem Dart-O-Mat 3000 verbindet.

## schaltung_holzbau
Hierin sind Details zur Verschaltung und zum Bau des Automaten aus Sicht der Holzarbeiten enthalten.
