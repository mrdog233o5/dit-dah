#!/usr/bin/env python
import keyboard
import time
import morse
KEY = "shift"
KEY_LENGTH = 0.1
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
    global char
    global phrase
    keyboard.write(morse.m2letter(char))
    char = ""
    phrase = []

def checkTime():
    global char
    if time.time() - lastRelease > KEY_LENGTH*4 and len(char) > 0:
        write()

keyboard.on_press_key(KEY, press)
keyboard.on_release_key(KEY, release)

while 1:
    checkTime()
