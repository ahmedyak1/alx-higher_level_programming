#!/usr/bin/python3
"""Class Student"""

     
        
 class Student:
    """
    Class  student
    """
    def __init__(self, first_name, last_name, age):
        """Instance Student

        args:
           first_name first name
            last_name last name
            age  age student
        """
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary repr student
        Return:
            dict: dict represrn
        """
        if attrs is None:
            return self.__dict__

        nd = {}
        for item in attrs:
            try:
                nd[item] = self.__dict__[item]
            except Exception:
                pass
        return nd
        
    def reload_from_json(self, json):
        """replace attribes json

        Args:  json obj.
        """
        self.__dict__.update(json)

