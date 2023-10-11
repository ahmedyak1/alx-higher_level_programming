#!/usr/bin/python3
"""Function inherits_from()"""


def inherits_from(obj, a_class):
    """the object is an instance of a class that inherited
    from the specified class Return true else return false

    Args: obj : object to check type.
            a_class : type of type to check.

    Return True || False
    """
    if type(obj) is a_class:
        return False
        
    return issubclass(type(obj), a_class)

