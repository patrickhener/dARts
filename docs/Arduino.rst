Arduino Sketch
==============

Nachfolgend wird der verwendete Arduino sketch beschrieben

Der Sketch
----------

.. literalinclude:: ../arduino/dARts.ino
   :language: C++

PINS
----

In diesem Abschnitt des Sketches werden die Pin Definitionen gemacht. Wie unter :ref:`Pinbelegung <Pinbelegung>` zu erkennen ist definiere ich hier Die Ultraschall Pins (echo = 8, trigger = 9), die PiezoPins A0 und A1 als array, den Button Pin 2 und den Button LED Pin 3, sowie die Output und Input Pins der Matrix.

VARIABLEN
---------

In diesem Abschnitt des Sketches werden unterschiedliche Variablen definiert. Sicherlich am interessantesten ist die Definition der Wertematrix für das Auslesen des Matrix als zweidimensionales Array.

FUNKTIONEN
----------

Nachfolgend werden die Funktionen des Sketches beschrieben.

Ultraschall()
^^^^^^^^^^^^^

In dieser Funktion wird der Ultraschall Sensor ausgelesen. Zuerst wird der Sensor durch aus- und anschalten frei gemacht, dann wird eine Dauer des Echos ermittelt und so verrechnet, dass sich eine Abstandseinheit in cm ergibt. Unterschreitet dieser Abstand eine Schwelle, so hat der Spieler seine Pfeile geholt und auf der seriellen Konsole wird das Wort "PFEILE" geschrieben. Danach erfolgt eine Wartezeit.

checkButton()
^^^^^^^^^^^^^

In dieser Funktion wird der Knopf ausgelesen. Wird er gedrückt wird das Wort "KNOPF" auf der seriellen Konsole geschrieben. Es erfolgt eine Wartezeit.

WurfSchicken(int x, int y)
^^^^^^^^^^^^^^^^^^^^^^^^^^

In dieser Funktion wird der ermittelte Wurf auf die serielle Konsole geschrieben. Der Funktion wird ein Wert des zweidimensionalen Matrixarrays übergeben. Dieser wird dann im Array nachgeschaut und auf die Konsole geschrieben. Außerdem wird die Variable bHitDetected (also Wurf erkannt) auf true gesetzt. Im Falle, dass ein Piezo ausgelöst wurde wird so verhindert, dass ein Fehlwurf anstatt des erkannten Wurfwertes gebucht wird.

WurfAuswerten()
^^^^^^^^^^^^^^^

In dieser Funktion wird die Matrix des Automaten ausgelesen. Hierbei wird nacheinander auf den Output Pins der Matrix ein Signal gegeben und dann auf jedem Input Pin der Matrix geprüft ob der Kontakt geschlossen ist. Ist dies der Fall wird genau dieser Wert des zweidimensionalen Matrixarrays an die Funktion WurfSchicken(int x, int y) übergeben.

FehlwurfErkennen()
^^^^^^^^^^^^^^^^^^

In dieser Funktion werden die Piezos ausgelesen und evaluiert, ob es sich um einen Fehlwurf handelt. Dafür wird nacheinander jeder Piezo zweimal in Folge ausgelesen und wenn der ausgelesene Wert den Schwellwert übersteigt, so wird die Variable bFehlwurf auf true gesetzt. Anschließend wird geprüft, ob ein Wurf erkannt wurde anhand des Status der Variablen bHitDetected. Ist dieser false, also es wurde kein Wurf erkannt, aber bFehlwurf ist true, also ein Fehlwurf wurde erkannt so wird das Wort "FEHLWURF" auf die serielle Konsole geschrieben.

Blinken(int Anzahl)
^^^^^^^^^^^^^^^^^^^

In dieser Funktion kann der Knopf zum blinken gebracht werden. Der Funktion wird eine Anzahl für das Blinken übergeben. Dann blinkt der Knopf, indem er an- und wieder ausgeschaltet wird.

ReagiereAufSerialString()
^^^^^^^^^^^^^^^^^^^^^^^^^

In dieser Funktion können Befehle verarbeitet werden, die dem Arduino auf die serielle Konsole geschrieben werden. Aktuell wird geprüft, ob jemand "BAN", "BAUS" oder "BB" schreibt. Die Abkürzungen stehen für "Button AN", also Knopf anschalten, "Button AUS", also Knopf ausschalten oder "Button BLINKEN", also einmal blinken lassen mithilfe der Funktion Blinken(int Anzahl).

LOOPS
-----

Nachfolgend werden die Loops des Programms beschrieben

Setup
^^^^^

Der Setup Loop wird immer beim Boot des Arduino ausgeführt, einmalig. Hier werden die einzelnen Pins als Input oder Output Pin definiert. Außerdem blinkt der Knopf dreimal mithilfe der Funktion Blinken(int Anzahl) und eine serielle Übertragung wird gestartet. Diese Übertragung wird vom :ref:`Python Koppler <Python Koppler>` ausgelesen und behandelt.

Main
^^^^

Der Main Loop bildet praktisch einen cycle des Prozessors ab. Dieser Loop läuft unendlich lange und wird immer wieder wiederholt. Es werden hier nacheinander die Funktionen Ultraschall(), checkButton(), WurfAuswerten()und  FehlwurfErkennen() ausgeführt. Anschließend wird noch geprüft, ob durch den Loop serialEvent() ein fertige String empfangen wurde. Wenn ja wird er mithilfe der Funktion ReagiereAufSerialString() ausgewertet und behandelt. Danach startet der cycle von vorne. Ein cycle benötigt ohne Wartezeiten der Funktionen etwa 20 Millisekunden.

serialEvent
^^^^^^^^^^^

In diesem Loop wird überprüft, ob auf der seriellen Konsole ein String empfangen wurde und ob dieser schon zuende geschrieben wurde (erkennbar an einem Zeilenumbruch). Dieser string wird dann in der Funktion ReagiereAufSerialString() behandelt.
