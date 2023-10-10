#!/usr/bin/python3
"""Function load_from_json_file"""
import json


def load_from_json_file(filename):
    """create obje from json file .

    Args:
        filename  name of the file.

    Return: object.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

