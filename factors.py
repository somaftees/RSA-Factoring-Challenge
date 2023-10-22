#!/usr/bin/python3

from sys import argv


def factor(v):

    i = 2

    if v < 2:
        return
    while v % i:
        i += 1
    print("{:.0f}={:.0f}*{:.0f}".format(v, v / i, i))


if len(argv) != 2:
    exit()

try:
    with open(argv[1]) as file:
        line = file.readline()

        while line != "":
            v = int(line.split('\n')[0])
            factor(v)
            line = file.readline()

except ValueError as e:
    pass
