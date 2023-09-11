#!/usr/bin/python3

def no_c(my_string):
    my_string_copy = [i for i in my_string if i.lower() != 'c']
    return ("".join(my_string_copy))
