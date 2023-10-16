#!/usr/bin/python3
"""Class Rectangle inherti from Base"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle

     Attributes: width rectangle
                 height rectangle
                 x  x 
                 y  y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates new instances of rectangle

        Attributes: width rectangle
                 height rectangle
                 x : x 
                 y  : y
                 id  :id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Prints rectangle"""
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.__x, self.__y, self.__width, self.__height))

    @property
    def width(self):
        """Width getter

        Return width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """prop setter

        Args: width of rectangle

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter

        Return: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height

        Args: height of rectangle
        
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter

        Return: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x

        Args: value  x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter

        Returns:
            int y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y

        Args: value y

        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calcu area of a rectangle

        Return: int: area
        """
        return self.__width * self.__height

    def display(self):
        """sdout the Rectangle insta with the character"""
        if self.__y > 0:
            for k in range(self.__y):
                print()
            self.__y = 0
        for k in range(self.__height):
            for j in range(self.__width):
                if self.__y == j:
                    print(" " * self.__x, end="")
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """arg  each attribute

        Args: arguments
              double pointer to a dicti
        """

        if args != None and len(args) != 0:
            la = ['id', 'width', 'height', 'x', 'y']
            for k in range(len(args)):
                setattr(self, la[k], args[k])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dicti repres of a Rectangle

        Returns: rectangle
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)

