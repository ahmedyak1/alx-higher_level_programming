#!/usr/bin/python3
"""
Prints all item in list 
agrs:my_list[]
"""
def print_list_integer(my_list=[]):
    for k in range(len(my_list)):
        print("{:d}".format(my_list[k]))
