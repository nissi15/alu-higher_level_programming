#!/usr/bin/python3
"""Defines a function that checks class membership including parents."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of it."""
    return isinstance(obj, a_class)
