#!/usr/bin/python3
"""Defines the Base class, the base of all other classes of this project."""
import json


class Base:
    """Manages the id attribute of all future classes of this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id: The identity of the new instance. If None, the number of
                created objects is incremented and used instead.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries: A list of dictionaries to serialize.

        Returns:
            "[]" if list_dictionaries is None or empty, otherwise the JSON
            string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        The file is named after the current class, for example Rectangle.json,
        and is overwritten if it already exists.

        Args:
            list_objs: A list of instances inheriting from Base. If None, an
                empty list is saved.
        """
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string.

        Args:
            json_string: A string representing a list of dictionaries.

        Returns:
            An empty list if json_string is None or empty, otherwise the list
            represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance of the current class with all attributes set.

        Args:
            dictionary: The key/value pairs used as attributes of the new
                instance.

        Returns:
            A new instance of the current class.
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from the class JSON file.

        Returns:
            An empty list if the file <Class name>.json does not exist,
            otherwise a list of instances of the current class.
        """
        try:
            with open("{}.json".format(cls.__name__), "r") as file:
                list_dictionaries = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []
        return [cls.create(**dictionary) for dictionary in list_dictionaries]
