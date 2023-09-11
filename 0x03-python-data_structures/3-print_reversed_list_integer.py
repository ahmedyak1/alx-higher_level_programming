#!/usr/bin/python3
"""
    reverse order number in list 
    args : my_list
"""
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for k in my_list:
            print("{:d}".format(k))

