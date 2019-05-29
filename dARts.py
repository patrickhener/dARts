#!/usr/bin/env python3

# Imports
import serial
import time
import yaml
import urllib.request
import urllib.parse

# Serielle Konfiguration
ser = serial.Serial()
ser.port = '/dev/ttyACM0'
ser.baudrate = 9600
ser.timeout = 1

# Port öffnen
try:
    ser.open()
    print("Serielle Kommunikation gestartet")
except(serial.serialutil.SerialException, SystemExit):
    print("FEHLER: Serielle Kommunikation nicht möglich\n\n\n")

# Config lesen
with open ("config.yml", 'r') as ymlconfig:
    cfg = yaml.load(ymlconfig, Loader=yaml.BaseLoader)

# Scoreboard variablen aus Config
host = cfg['scoreboard']['host']
port = cfg['scoreboard']['port']

# General variablen aus Config
pfeilzeit = cfg['general']['pfeilzeit']

# Variablen
matrix_dict = {
    '120': '/20/1',
    '220': '/20/2',
    '320': '/20/3',
    '101': '/1/1',
    '201': '/1/2',
    '301': '/1/3',
    '118': '/18/1',
    '218': '/18/2',
    '318': '/18/3',
    '104': '/4/1',
    '204': '/4/2',
    '304': '/4/3',
    '113': '/13/1',
    '213': '/13/2',
    '313': '/13/3',
    '106': '/6/1',
    '206': '/6/2',
    '306': '/6/3',
    '110': '/10/1',
    '210': '/10/2',
    '310': '/10/3',
    '115': '/15/1',
    '215': '/15/2',
    '315': '/15/3',
    '102': '/2/1',
    '202': '/2/2',
    '302': '/2/3',
    '117': '/17/1',
    '217': '/17/2',
    '317': '/17/3',
    '103': '/3/1',
    '203': '/3/2',
    '303': '/3/3',
    '119': '/19/1',
    '219': '/19/2',
    '319': '/19/3',
    '107': '/7/1',
    '207': '/7/2',
    '307': '/7/3',
    '116': '/16/1',
    '216': '/16/2',
    '316': '/16/3',
    '108': '/8/1',
    '208': '/8/2',
    '308': '/8/3',
    '111': '/11/1',
    '211': '/11/2',
    '311': '/11/3',
    '114': '/14/1',
    '214': '/14/2',
    '314': '/14/3',
    '109': '/9/1',
    '209': '/9/2',
    '309': '/9/3',
    '112': '/12/1',
    '212': '/12/2',
    '312': '/12/3',
    '105': '/5/1',
    '205': '/5/2',
    '305': '/5/3',
    '125': '/25/1',
    '225': '/25/2',
}

wurfzaehler = 0
pfeile_holen = False

# Funktionen

def makeRequest(urlpart):
    try:
        url = host + ":" + port + "/game/throw" + urlpart
        response = urllib.request.urlopen(url)
        return response.read().decode('utf-8')
    except(urllib.error.HTTPError):
        print("Fehler bei der Scoreboard Anfrage.")

def nextPlayer():
    try:
        url = host + ":" + port + "/game/nextPlayer"
        response = urllib.request.urlopen(url)
        return response.read().decode('utf-8')
    except(urllib.error.HTTPError):
        print("Fehler bei der Scoreboard Anfrage.")


def get_wurfzaehler():
    try:
        url = host + ":" + port + "/game/getThrowcount"
        response = urllib.request.urlopen(url)
        return response.read().decode('utf-8')
    except(urllib.error.HTTPError):
        print("Kein Spiel gestartet.")


# Main Loop bis CTRL+X
if __name__ == "__main__":
    try:
        while 1:
            string = ser.readline()
            if string:
                string = string[:-2]
                if string.decode() in matrix_dict:
                    wurfzaehler = get_wurfzaehler()
                    if pfeile_holen == False:
                        if not wurfzaehler == "3":
                            print(makeRequest(matrix_dict[string.decode()]))
                        else:
                            pfeile_holen = True

                elif string.decode() == "FEHLWURF":
                    wurfzaehler = get_wurfzaehler()
                    if pfeile_holen == False:
                        if not wurfzaehler == "3":
                            print(makeRequest('/0/1'))
                    else:
                        pfeile_holen = True

                elif string.decode() == "KNOPF":
                    wurfzaehler = get_wurfzaehler()
                    if wurfzaehler == "3":
                        pfeile_holen = True

                    if not pfeile_holen:
                        while not wurfzaehler == "3":
                            print(makeRequest('/0/1'))
                            wurfzaehler = get_wurfzaehler()
                        time.sleep(int(pfeilzeit))
                        pfeile_holen = True
                    else:
                        print(nextPlayer())
                        pfeile_holen = False

                elif string.decode() == "PFEILE":
                    wurfzaehler = get_wurfzaehler()
                    if pfeile_holen == True and wurfzaehler == "3":
                        time.sleep(int(pfeilzeit))
                        print(nextPlayer())
                else:
                    print("Das sollte niemals angezeigt werden.")

    except(KeyboardInterrupt, SystemExit):
        print("\nProgramm wird beendet")
        ser.close()
        print("Serielle Verbindung geschlossen.")
        print("ENDE")
