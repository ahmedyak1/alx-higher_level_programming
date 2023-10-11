#!/usr/bin/python3
"""Funtion add_attribute"""


def add_attribute(object, attr_name, value):
    """new attribute to an ovj

    Args:
        object : name of the object
        attr_name  name of the attribute
        value : value of the attribute
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attr_name, value)

