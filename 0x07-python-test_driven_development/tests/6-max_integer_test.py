#!/usr/bin/python3
# 6-max_integer_test.py
"""unitttt test for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for the function"""

    def test_func_ordered_list(self):
        """test_func an ord list of integers"""
        listt = [5, 6, 7 ,8]
        self.assertEqual(max_integer(listt), 8)

    def test_func_unordered_list(self):
        """test_func an unorlist of integers."""
        listt = [5, 6, 7 ,8]
        self.assertEqual(max_integer(listt), 8)

    def test_func_max_at_begginning(self):
        """test_func a list with a beginning max value."""
        listt = [50, 6, 7 ,8]
        self.assertEqual(max_integer(listt), 50)

    def test_func_empty_list(self):
        """test_func an empty list."""
        list_ = []
        self.assertEqual(max_integer(list_), None)

    def test_func_one_element_list(self):
        """test_func a list with a single element."""
        listt = [666]
        self.assertEqual(max_integer(listt), 666)

    def test_func_floats(self):
        """test_func a list of floats."""
        listt = [5.66, 666.79, -30.123, 6666.2, 65.0]
        self.assertEqual(max_integer(listt), 6666.2)

    def test_func_ints_and_floats(self):
        """test_func a list of ints and floats."""
        listt = [13.63, 605.5, -900000, 150405, 6]
        self.assertEqual(max_integer(listt), 150405)

    def test_func_string(self):
        """test_func a string."""
        toto = "Ahmed"
        self.assertEqual(max_integer(toto), 'm')

    def test_func_list_of_strings(self):
        """test_func a list of strings."""
        listt = ["Ahmed", "yakine", "zee"]
        self.assertEqual(max_integer(listt), "zee")

    def test_func_empty_string(self):
        """test_func an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()


