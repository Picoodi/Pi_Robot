import serial
import time

serial = serial.Serial('COM8', 115200)  # Port anpassen (unter Linux z.B. /dev/ttyACM0)
time.sleep(2)  # Verbindung aufbauen lassen

serial.write(b'LED ON\n')
time.sleep(1)
serial.write(b'LED OFF\n')

serial.close()
