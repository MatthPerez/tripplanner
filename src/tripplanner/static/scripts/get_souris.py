# Position curseur
import pyautogui
from pynput import mouse
import csv

saisie = "saisie.tsv"

def position_souris(x, y):
    x, y = pyautogui.position()
    print(x, y)

    with open("Files/" + saisie, mode='a') as file:
            phrase = str(x) + '|' + str(y) + '\n'
            # file.write(phrase)
            print(phrase)

def clic_souris(x, y, button, pressed):
    if pressed:
        if str(button) == 'Button.left':
            button_name = 'gauche'
        elif str(button) == 'Button.right':
            button_name = 'droit'
        elif str(button) == 'Button.middle':
            button_name = 'molette'
        else:
            button_name = str(button)
            
        phrase = str(x) + '\t' + str(y) + '\t' + button_name
        
        # with open("Files/" + saisie, mode='a') as file:
        #     file.write(phrase + '\n')
        print(phrase)


listener = mouse.Listener(on_move=position_souris)
listener = mouse.Listener(on_click=clic_souris)
listener.start()
listener.join()

