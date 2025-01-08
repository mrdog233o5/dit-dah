import os
import sys
import threading
import time
import morse
from pynput import keyboard

controller = keyboard.Controller()
KEY = "shift"
KEY_LENGTH = 0.1
lastPress = 0
lastRelease = 0
keyUp = True
phrase = []
char = ""
letters = []
IS_MAC = sys.platform == 'darwin'
IS_WIN = sys.platform == 'win32'
if IS_MAC:
    from rumps import *
# else:
    # from ruwps import *

icon_file = 'favIcon.png'
app = App('lovegun', icon=icon_file, template=True)
app.menu = [
    None
]

# morse

conversions = [[line[0], line[2:]] for line in r'''
  ........
A .-
B -...
C -.-.
D -..
E .
F ..-.
G --.
H ....
I ..
J ..
K -.-
L .-..
M --
N -.
O ---
P .--.
Q --.-
R .-.
S ...
T -
U ..-
V ...-
W .--
X -..-
Y -.--
Z --..
1 .----
2 ..---
3 ...--
4 ....-
5 .....
6 -....
7 --...
8 ---..
9 ----.
0 -----'''.splitlines()[1:]]

def letter(char, mode):
    char = char.upper()
    try:
        return [pair[not mode] for pair in conversions if char == pair[mode]][0]
    except:
        return ""

def phrase(text, mode):
    return [letter(char, mode) for char in text]

def chr2m(char):
    return letter(char, 0)

def m2chr(char):
    return letter(char, 1)

def str2m(char):
    return phrase(char, 0)

def m2str(char):
    return phrase(char, 1)

def press():
    global app
    global keyUp
    if not keyUp:
        return
    global lastPress
    lastPress = time.time()
    keyUp = False

def release():
    global keyUp
    global lastRelease
    global KEY_LENGTH
    global char
    lastRelease = time.time()
    timeLength = lastRelease - lastPress
    keyUp = True

    temp = [length-1 for length in range(1,3) if abs(timeLength - length*KEY_LENGTH) < 0.05 or timeLength < KEY_LENGTH]
    if len(temp) == 0:
        length = 1
    else:
        length = temp[0]

    if length:
        char += "-"
    else:
        char += "."

def write():
    global controller
    global char
    global phrase
    global typeCD
    controller.type(m2chr(char).lower())
    os.system(f"say {morse.m2chr(char).lower()}")
    char = ""
    phrase = []
    typeCD = 1

def checkTime():
    global char

    if time.time() - lastRelease > KEY_LENGTH*4 and len(char) > 0:
        write()

def inputLoop():
    while 1:
        checkTime()

def menuLoop():
    with keyboard.Events() as events:
        for event in events:
            if type(event) == keyboard.Events.Press:
                press()
            else:
                release()

menuThread = threading.Thread(target=menuLoop) 
inputThread = threading.Thread(target=inputLoop)

menuThread.start()
inputThread.start()


app.run()