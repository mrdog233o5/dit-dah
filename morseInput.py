#!/usr/bin/env python
import keyboard
import time
import morse
FUNCTION_KEY = "space"
KEY = "shift"
KEY_LENGTH = 0.07
lastPress = 0
lastRelease = 0
keyUp = True
phrase = []
char = ""
letters = []

def press(e):
    global keyUp
    if not keyUp:
        return
    global lastPress
    lastPress = time.time()
    keyUp = False

def release(e):
    global keyUp
    global lastRelease
    global KEY_LENGTH
    lastRelease = time.time()
    timeLength = lastRelease - lastPress
    keyUp = True

    temp = [length-1 for length in range(1,3) if abs(timeLength - length*KEY_LENGTH) < 0.05 or timeLength < KEY_LENGTH]
    if len(temp) == 0:
        length = 1
    else:
        length = temp[0]

    phrase.append(length)

def pressFunc(e):
    write()

def write():
    global char
    global phrase
    char = ""
    for data in phrase:
        if data:
            char += "-"
        else:
            char += "."
    keyboard.write(morse.m2letter(char))
    phrase = []


keyboard.on_press_key(KEY, press)
keyboard.on_release_key(KEY, release)
keyboard.on_press_key(FUNCTION_KEY, pressFunc)

while 1:
    pass
