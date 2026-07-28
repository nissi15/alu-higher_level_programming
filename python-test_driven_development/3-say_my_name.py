#!/usr/bin/python3
"""Defines a function that prints a full name.

The module holds a single function that prints a first name and a last
name in a fixed sentence, and validates that both are strings.
"""


def say_my_name(first_name, last_name=""):
    """Print My name is followed by the first name and the last name.

    Args:
        first_name: The first name to print.
        last_name: The last name to print, empty by default.

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
