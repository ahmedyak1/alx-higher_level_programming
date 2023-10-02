#!/usr/bin/python3
"""Class rectangle"""


class Rectangle:
    """
    Class rectangle

    Attributes:
        width : width rectangle.
        height : height rectangle.
    """
    def __init__(self, width=0, height=0):
        """Class intance rectangle.

        Args:
            width : width rectangle.
			height : height rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter width

        Return:
            the width rectangle
        """
        return self.__width

    @property
    def height(self):
        """getter height

        Returns: height rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """setter width rectangle.

        Args: width rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setter height recyangle

        Args: height rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


