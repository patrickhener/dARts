#!/usr/bin/env python3

# Imports
import serial
import time

# Serielle Konfiguration
ser = serial.Serial()
ser.port = '/dev/ttyACM0'
ser.baudrate = 9600
ser.timeout = 1

# Port öffnen
ser.open()
print("Serielle Kommunikation gestartet")

# Variablen
matrix_dict = {
    '120': '20',
    '220': 'D20',
    '320': 'T20',
}

# Main Loop bis CTRL+X
if __name__ == "__main__":
    try:
        while 1:
            string = ser.readline()
            if string:
                string = string[:-2]
                if string.decode() in matrix_dict:
                    print("Treffer war {}".format(matrix_dict[string.decode()]))
                else:
                    print(string.decode())

    except(KeyboardInterrupt, SystemExit):
        print("\nProgramm wird beendet")
        ser.close()
        print("Serielle Verbindung geschlossen.")
        print("ENDE")
