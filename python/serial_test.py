import serial

ser = serial.Serial()
ser.port = "/dev/ttyACM0"
ser.baudrate = 9600
ser.timeout = 1

ser.open()

string = "VOLL\n"
ser.write(string.encode('utf-8'))

ser.close
