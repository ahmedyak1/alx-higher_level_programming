#!/usr/bin/python3
"""Function is_same_class()"""


def is_same_class(obj, a_class):
    """Return True if  exactly an instance of the
    specified class else return False

    Args:
        obj: object to check type.
        a_class (type): type of type to check.

    Returns: true || false 
    """
    return type(obj) == a_class

