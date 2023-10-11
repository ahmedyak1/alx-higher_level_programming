#!/usr/bin/python3
"""function lookup"""


def lookup(obj):
    """Available attributes and methods,function an object
    Args:
        obj: object
    Return:
        list: list of available attributes and methods of an object
    """
    return dir(obj)

