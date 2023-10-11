#!/usr/bin/python3
"""Class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Class Rectangled"""

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

