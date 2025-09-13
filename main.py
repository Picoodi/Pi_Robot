import serial
import keyboard
import time

serial = serial.Serial('COM8', 115200)  # Port anpassen (unter Linux /dev/ttyACM0)
time.sleep(2)  # Verbindung aufbauen lassen
print("Start")

while True:
    if keyboard.is_pressed("w"):
        print("w is pressed")
        serial.write(b'Forward\n')

    elif keyboard.is_pressed("s"):
        print("s is pressed")
        serial.write(b"Backwards\n")

    elif keyboard.is_pressed("a"):
        print("a is pressed")
        serial.write(b"Left\n")

    elif keyboard.is_pressed("d"):
        print("d is pressed")
        serial.write(b"Right\n")

    else:
        serial.write(b"Stop\n")


serial.close()