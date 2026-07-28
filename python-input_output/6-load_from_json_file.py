#!/usr/bin/python3
"""Defines a function that loads an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Return the object represented by the JSON content of a file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
