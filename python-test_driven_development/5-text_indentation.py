#!/usr/bin/python3
"""Defines a function that prints text with indentation rules.

The module holds a single function that prints a text and adds two new
lines after each of the characters ., ? and : without extra spaces.
"""


def text_indentation(text):
    """Print a text with two new lines after each ., ? and : character.

    Args:
        text: The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip() != "":
        print(line.strip(), end="")
