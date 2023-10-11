#!/usr/bin/python3
"""Class Square
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Class Square

    Args: REctangle
    """

    def __init__(self, size):
        """Instance Class Square.

        Args:size of 1 side of square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """prints quare

        Returns: string square
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """area square

        Returns: area square
        """
        return self.__size ** 2

