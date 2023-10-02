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
			
	def area(self):
        """area rectangle

        Returns:area
        """
        return  self.__width * self.__height

    def perimeter(self):
        """perimeter rectangle

        Returns: perimeter
        """
        if  self.width == 0 or self.__height == 0 :
            return 0
        else:
            return  (self.__height + self.__width) * 2
			
	def __str__(self):
        """rectangle character 

        Returns: the rectangle
        """
        recta = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for k in range(self.__height):
            for m in range(self.__width):
                recta.append("#")
            recta.append("\n")

        recta.pop()

        return "".join(recta)

	def __repr__(self):
        """string representation  rectangle.

        Returns:rectangle representation.
        """
		pres = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return pres
		
	def __del__(self):
        """del instance class
        """
        print("{:s}".format("Bye rectangle..."))

