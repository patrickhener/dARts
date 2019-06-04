Arduino Sketche
===============

Dieser Ordner bietet Arduino Sketche für einen Arduino Mega 2560.

MAKEFILE
========

Das Makefile ist dazu da den Quelltext mit den Befehlen `make` zu bauen, `make upload` auf den Arduino zu laden und `make monitor` eine serielle Verbindung zum Arduino aufzunehmen.
Dieses Makefile steht in Abhängigkeit zu |diesem| Projekt.

.. |diesem| raw:: html

    <a href="https://github.com/pratimugale/arduino-makefile-vim" target="_blank">diesem</a>

Varianten
=========

Bislang gibt es zwei Varianten. Eine davon (*dARts_nopiezo.ino*) verwendet keine Piezos für die Fehlwurferkennung und die andere (*dARts.ino*) verwendet Piezos.
Da es in Abhängigkeit zum oben aufgeführten Makefile immer nur eine eindeutige INO-Datei pro Projektordner geben darf wird eine mit .bak benannt sein.
