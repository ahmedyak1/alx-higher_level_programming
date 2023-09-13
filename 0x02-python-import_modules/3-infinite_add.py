#!/usr/bin/python3
from sys import argv

if _name_ == "_main_":
    tot = 0
    for k in range(len(argv) - 1):
        tot += int(argv[k + 1])
    print("{}".format(tot))
