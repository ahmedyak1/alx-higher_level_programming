#!/usr/bin/python3
"""Class Square"""

from models/rectangle import Rectangle



class Square(Rectangle):
    """Class Square

     Attributes:
        width  width of rectangle
        height height of rectangle
        x  x
        y  y
        id  id of square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Create new insta of Square

        Args:
            size  width and height
            x  x
            y  y 
            id ID number of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints square"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Getter for size

        Returns: size square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter for width of square
        Args:  width of square.
   
   
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update arguemtns

        Args:
            args  args
            kwargs  double pointe dicti
        """
        if args != None and len(args) != 0:
            la = ['id', 'size', 'x', 'y']
            for k in range(len(args)):
                if la[k] == 'size':
                    setattr(self, 'width', args[k])
                    setattr(self, 'height', args[k])
                else:
                    setattr(self, la[k], args[k])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dict represen Square

        Returns: square
        """
        d1 = self.__dict__
        d2 = {}
        d2['id'] = d1['id']
        d2['size'] = d1['_Rectangle__width']
        d2['x'] = d1['_Rectangle__x']
        d2['y'] = d1['_Rectangle__y']

        return d2

