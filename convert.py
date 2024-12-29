conversions = [line.split() for line in r'''
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
0 -----
'''.splitlines()[1:]]

def letter(char, mode):
    char = char.upper()
    for pair in conversions:
        if char == pair[mode]:
            print(pair[not mode])

letter("a", 0)
