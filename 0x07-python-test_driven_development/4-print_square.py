#!/usr/bin/python3
"""print square function
"""


def print_square(size):
    """Prints a square with the character #.
    """
    mou = "size must be an integer"
    
    cara ="#"

    if not isinstance(size, int):
        raise TypeError(mou)

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError(mou)

    for i in range(size):
        print(cara * size)

