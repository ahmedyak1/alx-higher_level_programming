#!/usr/bin/python3
"""Function append Write"""


def append_write(filename="", text=""):
    """Appends a string text file

    Args:
        filename  name file
        text  string of text to write to file

    Return: number of char 
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

