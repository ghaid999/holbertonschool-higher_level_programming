#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_normal_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -5, 10, 3]), 10)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_all_equal(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_values(self):
        self.assertEqual(max_integer([1.5, 2.7, 2.6]), 2.7)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)
