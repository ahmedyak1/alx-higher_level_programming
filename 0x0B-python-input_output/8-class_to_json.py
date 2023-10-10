#!/usr/bin/python3
"""Function class_to_json"""


def class_to_json(obj):
    """Returns the dictionary 

    Args: obj : object.

    Return: dict: dictionary.
    """
    return obj.__dict__

