.. _Python Koppler:

Python Koppler
==============

In diesem Kapitel wird der verwendete Python Koppler beschrieben

Programmcode
------------

.. literalinclude :: ../python/dARts.py
   :language: Python

Imports
-------

In diesem Abschnitt werden notewendige Imports gemacht. Darunter zum Beispiel die Programmbibliothek *serial*, die den Arduino via serieller Konsole ausliest.

Systemd stuff
-------------

Dieser Abschnitt ist notwendig, um den Programmcode sauber beenden zu können, wenn er als systemd Dienst verwendet wird. Andernfalls würde beim Stoppen des Dienstes die serielle Kommunikation nicht sauber beendet.

Config
------

In diesem Abschnitt wird die config.yml ausgelesen und interpretiert.

Scoreboard variablen
^^^^^^^^^^^^^^^^^^^^

Die Variablen über den Host und den Port, wo der Dart-O-Mat 3000 zu finden sind werden hier gespeichert.

General variablen
^^^^^^^^^^^^^^^^^

Die Variablen über die Auszeit beim Pfeile Abziehen und den seriellen Port werden hier gespeichert.

Serielle Konfiguration
^^^^^^^^^^^^^^^^^^^^^^

Es wird eine Instanz ser der Klasse serial.Serial() erzeugt und konfiguriert.

Ports öffnen
------------

In diesem Abschnitt wird versucht die serielle Kommunikation mit dem Arduino zu starte. Schlägt das fehl wird der Code beendet mit einer Fehlermeldung.

Variablen
---------

In diesem Abschnitt werden die notwendigen Variablen definiert, die zum Abprüfen von Zuständen verwendet werden. Außerdem werden die Daten aus dem Matrix Array in das API Format vom Dart-O-Mat 3000 übersetzt, sodass zum Beispiel der Wert 320 (Triple 20) einen URL Anteil von 20/3 (Triple 20) ergibt. Dieses Dicitionary wird später von der Funktion makeRequest(urlpart) verwendet.

Funktionen
----------

makeRequest(urlpart)
^^^^^^^^^^^^^^^^^^^^

Diese Funktion konstruiert aus der *host* und *port* Variablen, sowie dem übergebenen *urlpart* einen Request an das Scoreboard. Dann wird die Antwort ausgewertet. Enthält sie das Wort "Dart" wird die Variable *pfeile_holen* auf **True** gesetzt. Beim Wort "Sieger" oder "Winner" wird die Variable *won* auf **True** gesetzt. Außerdem wird in beiden Fällen das Licht am Knopf aktiviert, indem mithilfe der Funktion button_on() das Wort *BAN* auf die Konsole geschrieben wird.

Die aufgerufenen URL an der Scoreboard API lautet: http://IP:PORT/game/throw/Wurfwert(z.B. /20/3 für triple 20)

requestRematch()
^^^^^^^^^^^^^^^^

Diese Funktion wird ausgeführt, wenn die Variable *won* auf **True** steht und der Knopf gedrückt wird. So kann schnell ein neues Match mit den gleichen Einstellungen gestartet werden.

Die aufgerufenen URL an der Scoreboard API lautet: http://IP:PORT/game/rematch

requestStuck()
^^^^^^^^^^^^^^

Diese Funktion wird aufgerufen, wenn in kürzester Zeit mehrmals die gleichen Werte auf der Konsole empfangen werden. Hierbei darf man davon ausgehen, dass ein Dartpfeil stecken geblieben ist. Das Scoreboard wird audiovisuell reagieren, sodass der Spieler auf den steckengebliebenen Pfeil aufmerksam gemacht wird.

Die aufgerufenen URL an der Scoreboard API lautet: http://IP:PORT/game/stuck

nextPlayer()
^^^^^^^^^^^^

Diese Funktion schaltet zum nächsten Spieler um.

Die aufgerufenen URL an der Scoreboard API lautet: http://IP:PORT/game/nextPlayer

get_wurfzaehler()
^^^^^^^^^^^^^^^^^

Diese Funktion ermittelt die Anzahl der Würfe, die ein Spieler in der aktuellen Wurfrunde (0-3) bereits gemacht hat. Die Wurfanzahl wird an mehreren Stellen ausgewertet und ist entscheiden dafür, wie sich der Python Koppler verhält. Außerdem wird über diese Funktion gesteuert, ob der Knopf angeschaltet werden muss, zum Beispiel wenn schon 3 Würfe gemacht wurden. Dies ist das Signal für den Spieler, dass er seine Pfeile holen muss.

Die aufgerufenen URL an der Scoreboard API lautet: http://IP:PORT/game/getThrowcount

check_button_on()
^^^^^^^^^^^^^^^^^

In dieser Funktion wird anhand der Anzahl der bereits geworfenen Darts entschieden, ob der Knopf aus oder an sein muss.

button_on()
^^^^^^^^^^^

Mithilfe dieser Funktion wird das Wort "BAN" auf die serielle Konsole geschrieben und der Arduino schaltet so die LED des Knopfs an.

button_off()
^^^^^^^^^^^^

Mithilfe dieser Funktion wird das Wort "BAUS" auf die serielle Konsole geschrieben und der Arduino schaltet so die LED des Knopfs aus.

button_blinken()
^^^^^^^^^^^^^^^^

Mithilfe dieser Funktion wird der Knopf zum Blinken gebracht

read_serial()
^^^^^^^^^^^^^

Diese Funktion liest einen String von der seriellen Konsole aus und formatiert ihn (Entfernt Zeilenumbrüche). Dann gibt sie den formatierten Wert zurück.

GET- und SET-Methoden
^^^^^^^^^^^^^^^^^^^^^

Die unterschiedlichen GET- und SET-Methoden sind dazu da die globalen Variablen für die Spielsteuerung zu schreiben oder auszulesen.

main() Als Hauptprogrammloop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Diese Funktion ist eine endlosschleife, wie im Arduino Sketch und steuert zyklisch die Kommunikation zwischen Arduino und dem Scoreboard Dart-O-Mat 3000.

Im Schritt 1 wird ein String von der Konsole empfangen mithilfe der Funktion read_serial(). Wenn ein String gelesen werden konnte wird die aktuelle Zeit als Zeitstempel ermittelt (Dient der Stuck Dart Erkennung).

Im Schritt 2 wird ausgewertet, ob der erkannte String im Dictionary der Dart Matrix steht. Wenn ja und weder *pfeile_holen* **True** ist oder der Wurfzähler 3 beträgt so wird anschließend auf Stuck Dart geprüft. Der Stuck Dart wird ermittelt, indem verglichen wird welches der letzte Wurfwert war. Ist es derselbe, wie der aktuelle Wurfwert wird das Zeitdelta verglichen zwischen letztem Empfang des Wertes und dem aktuellen. Ist dieser kleiner als die Zeitschwelle (halbe Sekunde) wird von einem Stuck Dart ausgegangen und die Funktion requestStuck() aufgerufen. Andernfalls wird der Wert an das Scoreboard gesendet via makeRequest() und der Wurf wird verbucht.

Ist der String kein Wurfwert wird in Schritt 3 kontrolliert, ob es das Wort "FEHLWURF" ist. Wenn ja und werder *pfeile_holen* **True** ist noch der Wurfzähler 3 beträgt und die Variable *pfeile_abgezogen* **True** ist, so wird via makeRequest() der Wert 0, also Fehlwurf an das Scoreboard geschickt.

Ist der String kein Fehlwurf wird in Schritt 4 kontrolliert, ob es das Wort "KNOPF" ist. Wenn ja, wird geprüft, ob *won* auf **True** steht. Ist das der Fall wird via requestRematch() ein neues Match angefordert. Andernfalls wird der Wurfzähler geprüft. Abhängig davon welchen Wert er hat werden entweder die Würfe mit Fehlwürfen (makeRequest('/0/1')) aufgefüllt oder auf den nächsten Spieler gewechselt (nextPlayer()).

Ist der String nicht Knopf wird in Schritt 5 kontrolliert, ob es das Wort "PFEILE" ist. In diesem Fall und dem Fall, dass sowohl *pfeile_holen* **True** ist und der Wurfzähler 3 beträgt wird die Pfeileholzeit lang gewartet und dann auf den nächsten Spieler geschaltet.

Dann startet der cycle von vorne.

Logging
-------

Alle Events werden zentral in der Datei dARts.log festgehalten. Man kann sich die Datei zu Debug zwecken also auf der Konsole des Pi's anschauen, indem man folgenden Aufruf im Ordner des Python Kopplers startet:

.. code-block:: bash

  tail -f dARts.log

