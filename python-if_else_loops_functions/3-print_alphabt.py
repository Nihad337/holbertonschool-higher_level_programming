#!/usr/bin/python3

for c in range(97, 123):  # ASCII 'a' (97) - 'z' (122)
    if c != 101 and c != 113:  # e=101, q=113
        print("{}".format(chr(c)), end="")
