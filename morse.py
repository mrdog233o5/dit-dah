#!/usr/bin/env python
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
    return [pair[not mode] for pair in conversions if char == pair[mode]][0]

def phrase(text, mode):
    return [letter(char, mode) for char in text]

def letter2m(char):
    return letter(char, 0)

def m2letter(char):
    return letter(char, 1)

def str2m(char):
    return phrase(char, 0)

def m2str(char):
    return phrase(char, 1)

def main():
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "-r":
        print("".join(m2str(input().split())))
    else:
        print(" ".join(str2m(input())))


if __name__ == "__main__":
    main()
