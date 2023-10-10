#!/usr/bin/python3
"""Function from_json_string"""
import json


def from_json_string(my_str):
    """return obje 

    Args:my_str json object to convert to Python object.

    Return: phton obj
    """
    return json.loads(my_str)

