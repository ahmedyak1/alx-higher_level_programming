#!/usr/bin/python3
import sys
arguments_len = len(sys.argv) - 1

if name == "__main__":
    
    if arguments_len == 0:
        print("0 arguments.")
    elif arguments_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arguments_len))
    for k in range(arguments_len):
        print("{}: {}".format(k + 1, sys.argv[k + 1])
