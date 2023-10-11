#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """Class BaseGeometry
    """
    def area(self):
        """Area function

   
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """valideur des valeurs 

        Args:
            name  name obj.
            value value parameter.

  
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

