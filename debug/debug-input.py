#!/usr/bin/env python3

# imports
import serial
import sys
from os import system

# Serial setup
ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/tmp/virtualcom1'

# Port öffnen
try:
    ser.open()
    print("Serielle Kommunikation gestartet")
except(serial.serialutil.SerialException, SystemExit):
    print("FEHLER: Serielle Kommunikation nicht möglich")

# Variablen

matrixlist = ["101", "201", "301", "102", "202", "302", "103", "203", "303",
              "104", "204", "304", "105", "205", "305", "106", "206", "306",
              "107", "207", "307", "108", "208", "308", "109", "209", "309",
              "110", "210", "310", "111", "211", "311", "112", "212", "312",
              "113", "213", "313", "114", "214", "314", "115", "215", "315",
              "116", "216", "316", "117", "217", "317", "118", "218", "318",
              "119", "219", "319", "120", "220", "320", "125", "225"]


# Funktionen
def print_menu():
    system('clear')
    print(30 * "-" + "MENU" + 30 * "-")
    print("1:       Knopf wurde gedrückt")
    print("2:       Fehlwurferkennung durch Piezo")
    print("3:       Pfeilrückholung wird erkannt")
    print("CTRL+C:  Exit")
    print(7 * "-")

def main():
    try:
        while 1:
            print_menu()
            command = ""
            string = input("Wurfwert (Beispiel 312 für T12) oder [1-3 aus Menü]: ")

            if string == "1":
                command = "KNOPFa\r"
            elif string == "2":
                command = "FEHLWURFa\r"
            elif string == "3":
                command = "PFEILEa\r"
            elif string in matrixlist:
                command = string + "a\r"
            else:
                input("Ungültige Auswahl. Any Key für Wiederholung.")

            ser.write(command.encode('utf-8'))

    except(KeyboardInterrupt, SystemExit):
        print("\nProgramm wird beendet")
        ser.close()
        print("Serielle Verbindung geschlossen.")
        print("ENDE")


if __name__ == "__main__":
    main()

