#!/usr/bin/python3
"""max integer function
"""


def max_integer(list=[]):
    """max integer function
    """
    if len(list) == 0:
        return None
        
    out = list[0]
    k = 1
    while k < len(list):
        if list[k] > out:
            out = list[k]
        k += 1
    return out

