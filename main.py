import serial
import time
from pynput import keyboard

ser = serial.Serial('COM8', 115200)  # Port anpassen
time.sleep(2)
print("Start")

pressed_keys = set()
last_command = None

def determine_command(keys):
    if 'w' in keys and 'a' in keys:
        return 'Left_Forward'
    if 'w' in keys and 'd' in keys:
        return 'Right_Forward'
    if 's' in keys and 'a' in keys:
        return 'Left_Backwards'
    if 's' in keys and 'd' in keys:
        return 'Right_Backwards'
    if 'w' in keys:
        return 'Forward'
    if 's' in keys:
        return 'Backwards'
    if 'a' in keys:
        return 'Left'
    if 'd' in keys:
        return 'Right'
    return 'Stop'

def send_command(cmd):
    global last_command
    if cmd != last_command:
        ser.write(cmd.encode() + b'\n')
        print(f"Send: {cmd}")
        last_command = cmd

def on_press(key):
    try:
        pressed_keys.add(key.char)
        cmd = determine_command(pressed_keys)
        send_command(cmd)
    except AttributeError:
        pass  # Sondertaste, ignorieren

def on_release(key):
    try:
        pressed_keys.discard(key.char)
        cmd = determine_command(pressed_keys)
        send_command(cmd)
    except AttributeError:
        pass

    if key == keyboard.Key.esc:
        ser.close()
        print("Beendet.")
        return False  # Listener stoppen und Programm beenden

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
