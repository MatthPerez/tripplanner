import pyautogui
from pynput import mouse 
# import csv

def position_souris(x, y):
    x, y = pyautogui.position()
    print(x, y)

    # with open("Files/position_souris.csv", mode='a') as file:
    #         phrase = str(x) + '|' + str(y) + '\n'
    #         file.write(phrase)


listener = mouse.Listener(on_move=position_souris)
listener.start()
listener.join()
