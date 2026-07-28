#!/usr/bin/python3
"""Defines a class BaseGeometry with an area method."""


class BaseGeometry:
    """Represents the base geometry."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")
