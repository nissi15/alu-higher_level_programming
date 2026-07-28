#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the max_integer function with several kinds of lists."""

    def test_ordered_list(self):
        """Test a list sorted in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list where the maximum is in the middle."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list where the maximum is the first element."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """Test calling the function without any argument."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test a list holding a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list holding only negative numbers."""
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_numbers(self):
        """Test a list holding negative and positive numbers."""
        self.assertEqual(max_integer([-1, 5, -3, 2]), 5)

    def test_floats(self):
        """Test a list holding floats."""
        self.assertEqual(max_integer([1.5, 3.7, 2.2]), 3.7)

    def test_mixed_int_and_float(self):
        """Test a list holding integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_duplicated_max(self):
        """Test a list where the maximum appears several times."""
        self.assertEqual(max_integer([4, 4, 2, 1]), 4)

    def test_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["abc", "xyz", "def"]), "xyz")

    def test_single_string(self):
        """Test a string used as a list of characters."""
        self.assertEqual(max_integer("hello"), "o")

    def test_zeros(self):
        """Test a list holding only zeros."""
        self.assertEqual(max_integer([0, 0, 0]), 0)


if __name__ == "__main__":
    unittest.main()
