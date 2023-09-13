#!/usr/bin/python3
import sys

if _name_ == "_main_":
   
    arg = len(sys.argv) - 1
    if arg == 0:
        print("0 arguments.")
    elif arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg))
    for k in range(arg):
        print("{}: {}".format(k + 1, sys.argv[k + 1]))
