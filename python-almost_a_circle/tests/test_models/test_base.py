#!/usr/bin/python3
"""Unit tests for the Base class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Test the instantiation of the Base class."""

    def test_id_is_incremented(self):
        """Test that consecutive instances get consecutive ids."""
        first = Base()
        second = Base()
        self.assertEqual(second.id, first.id + 1)

    def test_given_id(self):
        """Test that a given id is used as is."""
        self.assertEqual(Base(12).id, 12)

    def test_given_id_does_not_change_counter(self):
        """Test that a given id does not increment the counter."""
        first = Base()
        Base(98)
        second = Base()
        self.assertEqual(second.id, first.id + 1)

    def test_none_id(self):
        """Test that a None id falls back to the counter."""
        first = Base()
        second = Base(None)
        self.assertEqual(second.id, first.id + 1)

    def test_negative_id(self):
        """Test that a negative id is used as is."""
        self.assertEqual(Base(-5).id, -5)

    def test_string_id(self):
        """Test that a string id is used as is."""
        self.assertEqual(Base("hello").id, "hello")

    def test_nb_objects_is_private(self):
        """Test that the number of objects is a private attribute."""
        with self.assertRaises(AttributeError):
            print(Base(1).__nb_objects)

    def test_two_args(self):
        """Test that only one argument is accepted."""
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    """Test the to_json_string static method of the Base class."""

    def test_none(self):
        """Test that None returns an empty list string."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """Test that an empty list returns an empty list string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_type(self):
        """Test that the returned value is a string."""
        self.assertIs(type(Base.to_json_string([{"id": 1}])), str)

    def test_one_dictionary(self):
        """Test the representation of a list of one dictionary."""
        self.assertEqual(Base.to_json_string([{"id": 9}]), '[{"id": 9}]')

    def test_two_dictionaries(self):
        """Test the length of the representation of two dictionaries."""
        dictionaries = [{"id": 1, "width": 2}, {"id": 2, "width": 3}]
        self.assertEqual(len(Base.to_json_string(dictionaries)), 46)

    def test_rectangle_dictionary(self):
        """Test the length of the representation of a rectangle."""
        rectangle = Rectangle(10, 7, 2, 8, 1)
        result = Base.to_json_string([rectangle.to_dictionary()])
        self.assertEqual(len(result), 53)

    def test_square_dictionary(self):
        """Test the length of the representation of a square."""
        square = Square(10, 2, 1, 1)
        result = Base.to_json_string([square.to_dictionary()])
        self.assertEqual(len(result), 39)

    def test_no_args(self):
        """Test that an argument is mandatory."""
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestBaseFromJsonString(unittest.TestCase):
    """Test the from_json_string static method of the Base class."""

    def test_none(self):
        """Test that None returns an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """Test that an empty string returns an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_type(self):
        """Test that the returned value is a list."""
        self.assertIs(type(Base.from_json_string('[{"id": 1}]')), list)

    def test_one_dictionary(self):
        """Test the deserialization of a list of one dictionary."""
        self.assertEqual(Base.from_json_string('[{"id": 9}]'), [{"id": 9}])

    def test_two_dictionaries(self):
        """Test the deserialization of a list of two dictionaries."""
        json_string = '[{"id": 1, "width": 2}, {"id": 2, "width": 3}]'
        expected = [{"id": 1, "width": 2}, {"id": 2, "width": 3}]
        self.assertEqual(Base.from_json_string(json_string), expected)

    def test_dictionary_types(self):
        """Test that the deserialized items are dictionaries."""
        result = Base.from_json_string('[{"id": 1}, {"id": 2}]')
        self.assertIs(type(result[0]), dict)

    def test_no_args(self):
        """Test that an argument is mandatory."""
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestBaseSaveToFile(unittest.TestCase):
    """Test the save_to_file class method of the Base class."""

    def tearDown(self):
        """Remove the files created by the tests."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            try:
                os.remove(name)
            except FileNotFoundError:
                pass

    def test_none(self):
        """Test that None saves an empty list."""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_empty_list(self):
        """Test that an empty list saves an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_one_rectangle(self):
        """Test the file content for one rectangle."""
        rectangle = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rectangle])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 53)

    def test_one_square(self):
        """Test the file content for one square."""
        square = Square(10, 2, 1, 5)
        Square.save_to_file([square])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 39)

    def test_filename_is_class_name(self):
        """Test that the file is named after the class."""
        Rectangle.save_to_file([Rectangle(1, 1)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_overwrite(self):
        """Test that an existing file is overwritten."""
        Square.save_to_file([Square(9, 0, 0, 1)])
        Square.save_to_file([Square(1, 0, 0, 1)])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(),
                             '[{"id": 1, "size": 1, "x": 0, "y": 0}]')

    def test_no_args(self):
        """Test that an argument is mandatory."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


class TestBaseCreate(unittest.TestCase):
    """Test the create class method of the Base class."""

    def test_rectangle_type(self):
        """Test that a rectangle dictionary creates a rectangle."""
        self.assertIs(type(Rectangle.create(**{"id": 1})), Rectangle)

    def test_rectangle_attributes(self):
        """Test that a rectangle is created with the right attributes."""
        dictionary = {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        rectangle = Rectangle.create(**dictionary)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 3/4 - 1/2")

    def test_rectangle_is_a_new_instance(self):
        """Test that create returns a different instance."""
        rectangle = Rectangle(3, 5, 1)
        other = Rectangle.create(**rectangle.to_dictionary())
        self.assertIsNot(rectangle, other)

    def test_rectangle_is_not_equal(self):
        """Test that the created instance is not equal to the original."""
        rectangle = Rectangle(3, 5, 1)
        other = Rectangle.create(**rectangle.to_dictionary())
        self.assertNotEqual(rectangle, other)

    def test_square_type(self):
        """Test that a square dictionary creates a square."""
        self.assertIs(type(Square.create(**{"id": 1})), Square)

    def test_square_attributes(self):
        """Test that a square is created with the right attributes."""
        dictionary = {"id": 89, "size": 1, "x": 3, "y": 4}
        self.assertEqual(str(Square.create(**dictionary)),
                         "[Square] (89) 3/4 - 1")

    def test_square_is_a_new_instance(self):
        """Test that create returns a different square instance."""
        square = Square(3, 5, 1)
        self.assertIsNot(square, Square.create(**square.to_dictionary()))


class TestBaseLoadFromFile(unittest.TestCase):
    """Test the load_from_file class method of the Base class."""

    def tearDown(self):
        """Remove the files created by the tests."""
        for name in ("Rectangle.json", "Square.json"):
            try:
                os.remove(name)
            except FileNotFoundError:
                pass

    def test_no_file(self):
        """Test that a missing file returns an empty list."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_type(self):
        """Test that the returned value is a list."""
        Rectangle.save_to_file([Rectangle(1, 1)])
        self.assertIs(type(Rectangle.load_from_file()), list)

    def test_rectangle_types(self):
        """Test that the loaded instances are rectangles."""
        Rectangle.save_to_file([Rectangle(10, 7, 2, 8)])
        self.assertIs(type(Rectangle.load_from_file()[0]), Rectangle)

    def test_rectangle_content(self):
        """Test that the loaded rectangles keep their attributes."""
        first = Rectangle(10, 7, 2, 8, 1)
        second = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([first, second])
        loaded = Rectangle.load_from_file()
        self.assertEqual([str(first), str(second)],
                         [str(loaded[0]), str(loaded[1])])

    def test_square_types(self):
        """Test that the loaded instances are squares."""
        Square.save_to_file([Square(5)])
        self.assertIs(type(Square.load_from_file()[0]), Square)

    def test_square_content(self):
        """Test that the loaded squares keep their attributes."""
        square = Square(7, 9, 1, 5)
        Square.save_to_file([square])
        self.assertEqual(str(Square.load_from_file()[0]), str(square))

    def test_empty_file(self):
        """Test that an empty saved list loads an empty list."""
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])

    def test_extra_args(self):
        """Test that no argument is accepted."""
        with self.assertRaises(TypeError):
            Rectangle.load_from_file([])


if __name__ == "__main__":
    unittest.main()
