#!/usr/bin/python3
"""Class Student"""


class Student:
    """
    Class Student 

    
    """
    def __init__(self, first_name, last_name, age):
        """Instance Student

        args:
           first_name first name
            last_name last name
            age  age student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retreive instance student

        Returns: dict representation
        """
        return self.__dict__

