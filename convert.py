#!/usr/bin/env python
import morse
import sys

if len(sys.argv) > 1 and sys.argv[1] == "-r":
    print("".join(morse.m2str(input().split())))
else:
    print(" ".join(morse.str2m(input())))
