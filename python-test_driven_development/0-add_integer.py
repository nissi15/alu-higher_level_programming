#!/usr/bin/python3
"""Defines an integer addition function.

The module holds a single function that adds two numbers together after
casting them to integers, and validates that both arguments are numbers.
"""


def add_integer(a, b=98):
    """Return the addition of two numbers casted to integers.

    Args:
        a: The first number to add.
        b: The second number to add, 98 by default.

    Raises:
        TypeError: If a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
