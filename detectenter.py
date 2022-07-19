import keyboard
from pynput.mouse import Button, Controller, Listener
import time

f2 = open("text files\globalvars.txt", "w+")

mouse = Controller()

while True:
    f = open("text files\globalvars.txt", "r")
    if keyboard.is_pressed("delete"):
        mouse.click(Button.left, 1)
        time.sleep(0.5)
    if f.readline() =='Shut Off enterdetect[true]':
        f2.write("Shut Off enterdetect[false]")
        break
    f.close()

f2.close()