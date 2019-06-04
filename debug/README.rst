DEBUG
=====

Dieses Modul ist dafür gedacht den Script weiterzuentwickeln, ohne einen Arduino und sonstige Hardware in Betrieb zu haben.  
Es genügt ein Linux mit python zu haben. Dabei kann der Dart-O-Mat 3000, die dARts.py und das Debugging-Script auf einem System laufen.  

Verwendung
==========

Zuerst muss man das Debugging starten. Hierfür wird socat benötigt.

Starten
-------

Das beiliegende Script *start-debug.sh* startet im Hintergrund zwei virtuelle serielle Schnittstellen (*/tmp/virtualcom0* und */tmp/virtualcom1*).  
Als nächstes muss sichergestellt werden, dass in der *config.yml* von *dARts.py* als parameter *serial* der Wert */tmp/virtualcom0* aufgeführt ist.  

Stoppen
-------

Die Debugging Schnittstelle lässt sich einfach via Script *stop-debug.sh* wieder beenden. ACHTUNG! Dabei werden alle socat Verbindungen geschlossen.
Auch jene, die eventuell nichts mit *dARts* zu tun haben.

debug-input.py
==============

Hat man das Debugging gestartet kann man nun via Script *debug-input.py* menügeführt Befehle an das gestartete *dARts.py* senden. Hierbei empfängt *dARts.py*
die Befehle so, als ob der Arduino (die Hardware) die Befehle senden würde.

```
------------------------------MENU------------------------------
1:       Knopf wurde gedrückt
2:       Fehlwurferkennung durch Piezo
3:       Pfeilrückholung wird erkannt
CTRL+C:  Exit
-------
Wurfwert (Beispiel 312 für T12) oder [1-3 aus Menü]:
```

1: Knopf
--------

Dieser Befehl simuliert einen Druck auf den physikalischen Knopf.

2: Fehlwurferkennung
--------------------

Dieser Befehl simuliert einen ausgelösten Piezo Sensor durch einen Fehlwurf in den äußeren Ring.

3: Pfeilrückholung
------------------

Dieser Befehl simuliert den ausgelösten Ultraschallsensor, wenn der Spieler seine Pfeile abzieht.

CTRL+C: Exit
------------

Drückt man Strg + C, so wird das Programm beendet.

Wurfwerte:
----------

Außerdem kann anstatt der Menüauswahl auch ein Wurfwert übertragen werden, so wie es der Arduino machen würde, wenn er in der Matrix einen Wurfwert erkennt.
Der Wurfwert setzt sich aus einer Ziffer für den Modifier und zwei Ziffern für den Wert zusammen.  
So steht 103 zum Beispiel für eine einfache 3 und 320 für eine Triple 20. 225 zum Beispiel wäre Bulls eye.
