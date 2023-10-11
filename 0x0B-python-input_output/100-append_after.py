#!/usr/bin/python3
"""Function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function insert line test into file

    Args:
        filename name  file
        search_string String to search
        new_string : string to append
    """
    with open(filename, "r") as f:
        tot = f.readlines()

    with open(filename, "w") as l:
        stri = ""
        for k in tot:
            stri += k
            if search_string in k:
                stri += new_string
        l.write(stri)

