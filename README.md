Project-Keylogger/

├── main.py          # Main file with the keylogger code
├── keylog.txt       # File where logs are recorded (empty at the beginning)
├── requirements.txt # List of Python dependencies
└── README.md        # Project documentation

#Code Explanation

#-Imports

import keyboard: Captures global keyboard events.
import os: Handles forced program output.

#-LOG_FILE variable
Defines the output file: ‘keylog.txt’.
on_key_press(event) function

#-Executes for each keystroke.
key = event.name: Gets the name of the key (e.g., ‘a’, ‘space’).
if/elif block

#-Filters and records specific keys:
if key.isalpha(): Records letters.
elif key == ‘space’: Records space.
elif key == ‘,’: Records comma.
elif key == ‘.’: Records period.
elif key == ‘!’: Records exclamation mark.
elif key == ‘?’: Records question mark.
elif key == ‘enter’: Registers line break.
Use with open(LOG_FILE, ‘a’) to write in append mode.

#-Program termination
If key == ‘esc’: Prints message, stops listener, and exits.
Listener startup
keyboard.on_press(on_key_press): Registers the function.
keyboard.wait(): Maintains infinite loop.

##Examples of execution:
#In cmd:
PS C:\Users\emili\OneDrive\Documentos\Cybersecurity> & C:/Users/emili/AppData/Local/Programs/Python/Python314/python.exe c:/Users/emili/OneDrive/Documentos/Cybersecurity/virusScan.py
(Here are been writen all te characters readed on the OS, this include the comands for change pages, but also continue to write into the "keylog.txt" all the information of the keyboard)

Stoping keylogger...
(Here the virus stop)
