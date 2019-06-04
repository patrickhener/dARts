Koppler verwenden
=================

Dieser Koppler überträgt alles, was er vom Arduino bekommt an den Dart-O-Mat 3000.  
Dazu muss man in der config.yml den Host und den Port auf dem der Dart-O-Mat 3000 erreichbar ist angeben.  
Es gibt eine config.yaml.sample, die einfach in config.yaml umbenannt und angepasst werden kann.  
Außerdem wird die serielle Schnittstelle benötigt unter der der Arduino erreichbar ist.  

Dies sollte standardmäßig */dev/ttyACM0* sein.  
Wenn man das Debugging Modul verwendet sollte hier */tmp/virtualcom0* stehen.  
Für Details siehe Ordner *debug*.  

Den Koppler startet man entweder interaktiv *./dARts.py* oder als Service (siehe unten).

Ausgabe
=======

Die Ausgabe des Kopplers wird in eine Datei namens *dARts.log* geschrieben. Diese Datei wird im gleichen Ordner erzeugt, wie die *dARts.py*.  
Mit folgendem Befehl kann man dauerhaft mitschauen, was passiert (perfekt für Debugging):

.. code-block:: bash

    tail -f dARts.log

Service
=======

Die dARts.service ist eine systemd Service file:

.. code-block:: bash

    [Unit]
    Description=dARts.py E-Dart Kopplungs service
    After=multi-user.target

    [Service]
    Type=simple
    WorkingDirectory=/home/patrick/projects/dARts/python
    ExecStart=/usr/bin/python3 /home/patrick/projects/dARts/python/dARts.py

    [Install]
    WantedBy=multi-user.target

Damit sie funktioniert muss der Pfad zu dARts.py und das WorkingDirectory entsprechend angepasst werden.
Danach kopiert man sie nach *~/.config/systemd/user/*.
Danach kann man den Service wie gewohnt behandeln:

.. code-block:: bash

    Service starten:
    systemctl --user start dARts.service

    Service stoppen:
    systemctl --user stop dARts.service

    Autostart bei boot:
    systemctl --user enable dARts.service
