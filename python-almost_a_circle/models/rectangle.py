#!/usr/bin/python3
"""Defines the Rectangle class, which inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle with a width, a height and a position."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance.

        Args:
            width: The width of the new rectangle.
            height: The height of the new rectangle.
            x: The horizontal offset of the new rectangle.
            y: The vertical offset of the new rectangle.
            id: The identity of the new rectangle.

        Raises:
            TypeError: If width, height, x or y is not an integer.
            ValueError: If width or height is <= 0, or if x or y is < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return the horizontal offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal offset of the rectangle."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return the vertical offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical offset of the rectangle."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the character #, respecting x and y."""
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Update the rectangle attributes.

        Args:
            args: The new attribute values in the order id, width, height,
                x and y.
            kwargs: The new attribute values by name, skipped if args exists
                and is not empty.
        """
        if args and len(args) > 0:
            attributes = ["id", "width", "height", "x", "y"]
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

    def __str__(self):
        """Return the print representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
