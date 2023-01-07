#!/usr/bin/python3
""" Unit tests for max_integer module """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Define unittests for max_integer """

    def test_ordered_list(self):
        """ tests if input is an ordered list of ints """
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Tests for an unordered list of integers"""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list with max int at the start"""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)
    
    def test_one_element_list(self):
        """Tests a list with a single element"""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Tests a list of floats"""
        floats = [1.53, 6.33, -9.214, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Tests a list of ints and floats"""
        ints_and_floats = [5.32, 6.7, 15, -9, 12.3]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Tests a string"""
        string = 'Right'
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Tests a list of strings"""
        strings = ['I', 'am', 'trying', 'so', 'hard']
        self.assertEqual(max_integer(strings), 'name')

    def test_empty_string(self):
        """ Tests and empty string """
        self.assertEqual(max_integer(''), None)


if __name__ == 'main':
    unittest.main()
