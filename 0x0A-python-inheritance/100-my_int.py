#!/usr/bin/python3
"""Class MyInt
"""


class MyInt(int):
    """Class MyInt

    """
    def __init__(self, value):
        """Instance class MyInt

        Args: value integer.
        """
        self.__value = value

    def __eq__(self, other):
        """The method equal

        Args: other  integer

        Return: True || False
        """
        return self.__value != other

    def __ne__(self, other):
        """The method not equal

        Args: other :integer

        Return: True || False
        """
        return self.__value == other

