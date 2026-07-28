#!/usr/bin/python3
"""Defines the Square class, which inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, a rectangle with the same width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size: The size of the new square.
            x: The horizontal offset of the new square.
            y: The vertical offset of the new square.
            id: The identity of the new square.

        Raises:
            TypeError: If size, x or y is not an integer.
            ValueError: If size is <= 0, or if x or y is < 0.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square attributes.

        Args:
            args: The new attribute values in the order id, size, x and y.
            kwargs: The new attribute values by name, skipped if args exists
                and is not empty.
        """
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}

    def __str__(self):
        """Return the print representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
