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
    return [pair[not mode] for pair in conversions if char == pair[mode]]

def phrase(text, mode):
    return [letter(char, mode) for char in text]

def main():
    print(phrase("hello world", 0))

if __name__ == "__main__":
    main()
