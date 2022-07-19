import tkinter as tk
from tkinter.constants import *
import keyboard
import sys
import pydirectinput
from pynput.mouse import Button, Controller, Listener
from pprint import pprint
import time

f = open("text files\dictionary.txt", "r")
f2 = open("text files\globalvars.txt", "w+")

a = ''
takenletters = []

mouse = Controller()

window=tk.Tk()

width = int(window.winfo_screenwidth()/7)+20
height = int(window.winfo_screenheight()/3+40)

rwidth = int(window.winfo_screenwidth())
rheight = int(window.winfo_screenheight())


def resetlist():
    print('Before clear: ', takenletters)
    takenletters.clear()
    print('After clear: ', takenletters)


def exitk():
    f2.write(f"Shut Off enterdetect[true]")
    f2.close()
    window.quit()


tk.Label(window, text= ("_"*100+"\n")*100,bg='#1B1B1B', fg='#1B1B1B',font=('rockwell bold', 15)).place(x=0, y=0)
tk.Label(window, text= "Auto Typer",bg='#1B1B1B', fg='#72bcd4',font=('rockwell bold', 15)).place(x=65, y=5)
exit_button = tk.Button(window, text="X", width=5, height=1, command=exitk)
exit_button.place(x=width-45, y=0)

reset_button = tk.Button(window, text="Reset List", width=8, height=1, command=resetlist)
reset_button.place(x=width-200, y=200)

def printInput():
    inp=''
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = inp)

    print(inp)
    for x in f:
        print(x)
        if inp in x and x != takenletters:
            takenletters.append(x)
            a=x
            print(a)
            break
        if x == "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ":
            a=''
            break

    mouse.position = (rwidth/2, rheight/1.02)
    mouse.click(Button.left, 1)
    for h in a:
        pydirectinput.keyDown(h)
    pydirectinput.keyDown('enter')
    pydirectinput.keyUp('enter')
    mouse.position = (rwidth/1.1, rheight/15)
    mouse.click(Button.left, 1)
    mouse.position = (rwidth/1.1, rheight/10)
    for x in range(1,4):
        pydirectinput.keyDown('backspace')
        pydirectinput.keyUp('backspace')
  
# TextBox Creation
inputtxt = tk.Text(window,
                   height = 1,
                   width = 10)
  
inputtxt.place(x=width/3.2, y=40)
  
# Button Creation
printButton = tk.Button(window,
                        text = "Send", 
                        command = printInput)
printButton.place(x=width/2.4,y=62)
  
# Label Creation
lbl = tk.Label(window, text = "")
lbl.place(x=0,y=90)


window.overrideredirect(True)
window.resizable(False, False)
window.geometry(f"{width}x{height}+{(window.winfo_screenwidth()-width)-10}+{10}")
window.attributes('-topmost',True)
window.attributes('-alpha',0.8)

window.mainloop()