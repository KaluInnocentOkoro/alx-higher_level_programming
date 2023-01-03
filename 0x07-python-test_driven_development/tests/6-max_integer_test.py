#!/usr/bin/python3
"""unitest for 6-max_integer.py"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """Test maximum integer in a list"""

    def test_positive_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 8]), 8)

    def test_negative_int(self):
        self.assertEqual(max_integer([-2, -5, -10, -3, -12]), -2)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_same_element(self):
        self.assertEqual(max_integer([2, 2, 2, 2, 2]), 2)

    def test_list_of_list(self):
        self.assertEqual(max_integer([[1, 2, 5], [7, 8, 9], [10, 11, 12]]), [10, 11, 12])

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_int_in_quotes(self):
        self.assertEqual(max_integer(["1", "2", "3", "4"]), 4)

    def test_string_and_ints(self):
        with self.assertRaises(TypeError):
            max_integer([1, 5, 8, 4, "come"])

    def test_dict(self):
        with self.assertRaises(KeyError):
            max_integer({1: "a", 5: "b", 8: "c", 4: "d"})
