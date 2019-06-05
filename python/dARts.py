#!/usr/bin/env python3

# Imports
import serial
import time
import yaml
import urllib.request
import urllib.parse
import sys
import logging
import os
import signal

# Tracebacks unterdrücken
#  sys.tracebacklimit = 0

# Setup Logging
#  if os.path.isfile("dARts.log"):
    #  os.remove("dARts.log")
logging.basicConfig(filename='dARts.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Start der Applikation")

#  systemd stuff
def signal_handler(signal, frame):
    logging.info("Beende Programm!")
    ser.close()
    logging.info("Serielle Kommunikation gestoppt")
    logging.info("ENDE")
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

# Config lesen
try:
    with open ("config.yml", 'r') as ymlconfig:
        cfg = yaml.load(ymlconfig, Loader=yaml.BaseLoader)
except:
    logging.error("Keine Konfigurationsdatei gefunden!")
    sys.exit("ERROR: Keine Konfigurationsdatei gefunden!")

# Scoreboard variablen aus Config
if cfg:
    host = cfg['scoreboard']['host']
    port = cfg['scoreboard']['port']

    # General variablen aus Config
    pfeilzeit = cfg['general']['pfeilzeit']
    serialport = cfg['general']['serial']

    # Serielle Konfiguration
    ser = serial.Serial()
    ser.port = serialport
    ser.baudrate = 115200
    ser.timeout = 1

# Port öffnen
try:
    ser.open()
    logging.info("Serielle Kommunikation gestartet")
except(serial.serialutil.SerialException):
    logging.error("Serielle Kommunikation nicht möglich!")
    sys.exit("ERROR: Serielle Kommunikation nicht möglich!")

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

valide_wurfzaehler = ["0", "1", "2", "3"]

global pfeile_holen
global knopf_an
global pfeile_abgezogen
global won

pfeile_holen = False
knopf_an = False
pfeile_abgezogen = True
won = False

# Funktionen
def makeRequest(urlpart):
    try:
        url = host + ":" + port + "/game/throw" + urlpart
        response = urllib.request.urlopen(url)
        response_text = response.read().decode('utf-8')
        if "Dart" in response_text:
            set_pfeile_holen(True)
            button_on()
        if "Sieger" in response_text:
            set_won(True)
            button_on()
        if "Winner" in response_text:
            set_won(True)
            button_on()
        logging.info("SCOREBOARDANTWORT: {}".format(response_text))
        return response_text
    except:
        logging.error("Fehler bei der Scoreboard Anfrage")


def requestRematch():
    try:
        url = host + ":" + port + "/game/rematch"
        response = urllib.request.urlopen(url)
        response_text = response.read().decode('utf-8')
        logging.info("SCOREBOARDANTWORT: {}".format(response_text))
        button_off()
        set_won(False)
        return response_text
    except:
        logging.error("Fehler bei der Rematch Anfrage")


def nextPlayer():
    try:
        url = host + ":" + port + "/game/nextPlayer"
        response = urllib.request.urlopen(url)
        response_text = response.read().decode('utf-8')
        if "Dart" in response_text:
            set_pfeile_holen(True)
            button_on()
        logging.info("SCOREBOARDANTWORT: {}".format(response_text))
        return response_text
    except:
        logging.error("Fehler bei der Scoreboard Anfrage")


def get_wurfzaehler():
    try:
        url = host + ":" + port + "/game/getThrowcount"
        response = urllib.request.urlopen(url)
        response_text = response.read().decode('utf-8')
        global pfeile_holen
        if not pfeile_holen:
            check_button_on(response_text)
        return response_text
    except:
        logging.error("Kein Spiel gestartet")


def check_button_on(wurfzaehler):
    try:
        global knopf_an
        if wurfzaehler == "2":
            if not knopf_an:
                button_on()
        else:
            if knopf_an:
                button_off()
    except:
        logging.error("Button Check fehlgeschlagen")


def button_on():
    global knopf_an
    outputString = "BUTTONAN\n"
    ser.write(outputString.encode('utf-8'))
    knopf_an = True


def button_off():
    global knopf_an
    outputString = "BUTTONAUS\n"
    ser.write(outputString.encode('utf-8'))
    knopf_an = False


def read_serial():
    string = ser.readline()
    if string:
        string = string[:-2]
        string = string.decode()
        return string
    else:
        return ""


def get_pfeile_holen():
    global pfeile_holen
    return pfeile_holen


def set_pfeile_holen(status):
    global pfeile_holen
    pfeile_holen = status
    return get_pfeile_holen


def get_pfeile_abgezogen():
    global pfeile_abgezogen
    return pfeile_abgezogen


def set_pfeile_abgezogen(status):
    global pfeile_abgezogen
    pfeile_abgezogen = status
    return get_pfeile_abgezogen


def get_won():
    global won
    return won


def set_won(status):
    global won
    won = status
    return won


def init():
    if get_wurfzaehler() == "3":
        set_pfeile_holen(True)

def main():
    init()
    while True:
        string = read_serial()
        if string:
            logging.info("string ist: {}".format(string))
            if string in matrix_dict:
                wurfzaehler = get_wurfzaehler()
                if not get_pfeile_holen():
                    if not wurfzaehler == "3":
                        if get_pfeile_abgezogen():
                            antwort = makeRequest(matrix_dict[string])

            elif string == "FEHLWURF":
                wurfzaehler = get_wurfzaehler()
                if not get_pfeile_holen():
                    if not wurfzaehler == "3":
                        if get_pfeile_abgezogen():
                            antwort = makeRequest('/0/1')

            elif string == "KNOPF":
                if get_won():
                    requestRematch()
                else:
                    wurfzaehler = get_wurfzaehler()
                    if wurfzaehler in valide_wurfzaehler:
                        if not get_pfeile_holen():
                            while not wurfzaehler == "3":
                                antwort = makeRequest('/0/1')
                                wurfzaehler = get_wurfzaehler()
                                button_on()
                            set_pfeile_abgezogen(False)

                        else:
                            antwort = nextPlayer()
                            set_pfeile_holen(False)
                            set_pfeile_abgezogen(True)
                            button_off()

            elif string == "PFEILE":
                wurfzaehler = get_wurfzaehler()
                if get_pfeile_holen() and wurfzaehler == "3":
                    time.sleep(int(pfeilzeit))
                    antwort = nextPlayer()
                    set_pfeile_holen(False)
                    set_pfeile_abgezogen(True)
                    button_off()
                else:
                    logging.error("Das sollte niemals angezeigt werden")

# Main Loop
if __name__ == "__main__":
    main()

