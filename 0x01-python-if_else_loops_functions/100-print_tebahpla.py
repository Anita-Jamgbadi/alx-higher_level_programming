#!/usr/bin/python3
for i in range(ord('z'), ord('a') -1, -1):
    if i % 2 == 0:
        sub = 0
    else:
        sub = 32
    print('{}'.format(chr(i - sub)), end='')
