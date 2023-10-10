#!/usr/bin/python3
"""Function Write file"""


def write_file(filename="", text=""):
    """write into fine and return number of char in fiel

    Args:filename  name  file
        text : string to write in file 

    return: number of char in file 
    """
    with open(filename, 'w', encoding="utf-8") as f:
        
        
        return f.write(text)

