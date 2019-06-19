Setup des Systems
=================

In diesem Kapitel wird beschrieben, wie man das System aufsetzen kann

System Basissetup
-----------------

Ich habe auf dem Raspberry Pi ein Arch Linux installiert. Eine gute Anleitung dazu findet man hier: |arch|. Es ist wichtig darauf zu achten, dass Ihr das 32bit Image installiert.
Außerdem benötigt Ihr |python| und solltet die |Arduino IDE| installieren.

.. |arch| raw:: html

  <a href="https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-3" target="_blank">archlinuxarm.org</a>

.. |python| raw:: html

  <a href="https://wiki.archlinux.org/index.php/Python#Python_3" target="_blank">Python 3</a>

.. |Arduino IDE| raw:: html

  <a href="https://wiki.archlinux.org/index.php/Arduino#Installation" target="_blank">Arduino IDE</a>

Arduino flashen
---------------

Aus Gründen der Bequemlichkeit und der Kompatibilität mit *vim*, den ich als Texteditor verwende nutze ich das *Makefile* aus |diesem| Projekt. Man clont das Repo, wie in meinem Fall unter **~/.arduino_mk** und kann dann ein Makefile im Ordner mit dem Sketch verwenden.
Dazu könnt Ihr einfach mein Makefile entsprechend auf eure Orderstruktur anpassen.

.. literalinclude:: ../arduino/Makefile
   :language: Bash

Das ARDUINO_DIR gibt an, wo die IDE zu finden ist. Die include Zeile inkludiert das Makefile aus dem oben erwähnten Git Repo.  
Anschließend könnt Ihr mit drei Befehlen das Flashen des Arduinos steuern:

.. code-block:: bash

  # Kompilieren des Codes
  make

  # Hochladen des Codes auf den Arduino
  make upload

  # Seriellen Monitor starten
  make monitor

Und weil ich tippfaul bin habe ich mir alias Einträge in meinem profil hinterlegt: *m*, *mu* und *mm*.

.. |diesem| raw:: html

  <a href="https://github.com/sudar/Arduino-Makefile" target="_blank">diesem</a>

Python Koppler als systemd Dienst
---------------------------------

Der Python Koppler kann als systemd Dienst installiert werden, sodass man ihn beim Start des Pi's bequem automatisch starten lassen kann. Dazu habe ich im Ordner *python* ein service file inkludiert.

.. literalinclude:: ../python/dARts.service
   :language: Bash

Wichtig ist, dass Ihr die Pfadangaben an eure Orderstruktur anpasst. Dann kopiert Ihr die Datei nach */home/<euer Benutzername>/.config/systemd/user/dARts.service*. So wird der Service als Benutzerservice zur Verfügung gestellt.

Anschließend könnt Ihr den Service wie jeden systemd Service nutzen:

.. code-block:: bash

  # Service starten:
  systemctl --user start dARts.service

  # Service stoppen:
  systemctl --user stop dARts.service

  # Autostart bei boot:
  systemctl --user enable dARts.service

Hostapd und Dnsmasq als WLAN Access Point
-----------------------------------------

Den Pi habe ich zum WLAN-Hotspot gemacht. So kann eine Spielergruppe einfach ein Anzeigegerät für den Dart-O-Mat 3000 per WLAN einbuchen. Auch das Smartphone kann so als Game Controller einfach genutzt werden.
Ich nutze dazu hostapd. Um IP Adressen und DNS kümmert sich bei mir Dnsmasq. Damit die Geräte nach dem Einwählen direkt umgeleitet werden (Captive Portal, wie zum Beispiel im Hotel) wird nginx eingesetzt. Eine gute Anleitung, wie man das einrichtet findet man beispielsweise |hier|.

.. |hier| raw:: html

  <a href="https://brennanhm.ca/knowledgebase/2016/10/raspberry-pi-access-point-and-captive-portal-without-internet/#Configure_Hostapd" target="_blank">hier</a>

Für mich haben folgende Konfigurationseinstellungen funktioniert.

hostapd
^^^^^^^

Die Datei kommt nach */etc/hostapd/hostapd.conf*

.. literalinclude:: ../system/hostapd/hostapd.conf
   :language: Bash

Der Inhalt von */etc/default/hostapd* sollte so aussehen:

.. literalinclude:: ../system/hostapd/hostapd
   :language: Bash

dnsmasq
^^^^^^^

Die Datei kommt nach */etc/dnsmasq.conf*

.. literalinclude:: ../system/dnsmasq/dnsmasq.conf
   :language: Bash

nginx
^^^^^

Die Datei kommt nach */etc/nginx/nginx.conf*

.. literalinclude:: ../system/nginx/nginx.conf
   :language: Bash

Und die Datei kommt nach /etc/nginx/sites-available/hotspot.conf

.. literalinclude:: ../system/nginx/hotspot.conf
   :language: Bash

Die Hotspotseite wird aktiviert, indem man die Datei mit einem Symlink nach sites-enabled verlinkt:

.. code-block:: bash

  ln -s /etc/nginx/sites-available/hotspot.conf /etc/nginx/sites-enabled/hotspot.conf

/etc/hosts
^^^^^^^^^^

In der */etc/hosts* sollte noch folgender Eintrag unten angefügt werden.

.. code-block:: bash

  10.41.18.20   dart-o-mat-3000.darts

Autostarts
^^^^^^^^^^

Wenn die Dienste alle korrekt laufen kann man sie mit den folgenden Befehlen noch zum Autostart hinzufügen:

.. code-block:: bash

  sudo systemctl enable hostapd
  sudo systemctl enable dnsmasq
  sudo systemctl enable nginx
