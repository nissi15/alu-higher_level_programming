#!/usr/bin/python3
"""Defines a class Square with a string representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a square with a validated size.

        Args:
            size: The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
