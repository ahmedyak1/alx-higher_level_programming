#!/usr/bin/python3
"""add_intgers function
"""


def add_integer(a, b=98):
    """plus two int && || float values
	
    Returns:
        int: a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(b, float):
        b = int(b)
        
    if isinstance(a, float):
        a = int(a)
    return b + a

