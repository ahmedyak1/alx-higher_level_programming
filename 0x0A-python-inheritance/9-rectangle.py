#!/usr/bin/python3
"""Class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
       """Instance rectangle

        Args:
            width width rectangle
            height height rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Area Rectangle

        Returns: area
        """
        return self.__width * self.__height

    def __str__(self):
        """string representation Rectangle.

        Return:String representation rectangle
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

