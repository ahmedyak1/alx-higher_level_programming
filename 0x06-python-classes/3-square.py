#!/usr/bin/python3
"""Class Square"""


class Square():
    """ Class Square definition """
    def __init__(self, size=0):
        """ size of square

        Args:
            size: the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
			
        elif size < 0:
            raise ValueError("size must be >= 0")
			
        self.__size = size

    def area(self):
        return self.__size ** 2

