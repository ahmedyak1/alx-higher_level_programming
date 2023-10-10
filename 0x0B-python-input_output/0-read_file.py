#!/usr/bin/python3
"""Function read file"""


def read_file(filename=""):
    """Reads a file and prints to stdout.

    Args: filename name file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        rd = f.read()
        print(rd, end='')

