#!/usr/bin/python3
"""Function is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of ot if the object is
    an instance of a class
    else return False.

    Args:  obj : object to check type.
           a_class: type of type to check.

    Returns: true || false 
    """

    return isinstance(obj, a_class)

