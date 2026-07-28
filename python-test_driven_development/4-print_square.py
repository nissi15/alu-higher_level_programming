#!/usr/bin/python3
"""Defines a function that prints a square.

The module holds a single function that prints a square of a given size
using the # character, and validates the size before printing.
"""


def print_square(size):
    """Print a square with the # character.

    Args:
        size: The length of a side of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)
