#!/usr/bin/python3
"""Defines a class MyList that subclasses the built-in list type."""


class MyList(list):
    """Represents a list that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
