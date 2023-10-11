#!/usr/bin/python3
"""MyList that inherit from list"""

class MyList(list):
    """Class that inherits from list.

    Args:
        list: list
    """
    def print_sorted(self):
        """Prints a list in ascending order.
        """
        l = self[:]
        l.sort()
        print(l)

