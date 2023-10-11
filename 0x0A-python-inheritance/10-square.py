#!/usr/bin/python3
"""Class Square 
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square
    """

    def __init__(self, size):
        """Instance class Square

        Args: size of 1 side of square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Area square.

        Return: Area square
        """
        return self.__size ** 2

