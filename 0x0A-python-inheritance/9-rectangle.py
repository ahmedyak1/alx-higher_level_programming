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
        self.__height = height
        self.__width = width
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        

    def area(self):
        """Area Rectangle.

        Returns: area
        """
        return  self.__height * self.__width 

    def __str__(self):
        """string representation Rectangle.

        Return:String representation rectangle.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

