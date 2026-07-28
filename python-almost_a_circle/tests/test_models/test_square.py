#!/usr/bin/python3
"""Unit tests for the Square class."""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Test the instantiation of the Square class."""

    def test_is_a_rectangle(self):
        """Test that a square is a Rectangle instance."""
        self.assertIsInstance(Square(5), Rectangle)

    def test_is_a_base(self):
        """Test that a square is a Base instance."""
        self.assertIsInstance(Square(5), Base)

    def test_one_arg(self):
        """Test that the size is enough to instantiate."""
        self.assertEqual(Square(5).size, 5)

    def test_size_sets_width_and_height(self):
        """Test that the size is assigned to width and height."""
        square = Square(5)
        self.assertEqual((square.width, square.height), (5, 5))

    def test_default_x_and_y(self):
        """Test that x and y default to zero."""
        square = Square(5)
        self.assertEqual((square.x, square.y), (0, 0))

    def test_four_args(self):
        """Test that all four arguments are assigned."""
        square = Square(5, 3, 4, 7)
        self.assertEqual((square.size, square.x, square.y, square.id),
                         (5, 3, 4, 7))

    def test_id_is_incremented(self):
        """Test that consecutive squares get consecutive ids."""
        first = Square(5)
        second = Square(5)
        self.assertEqual(second.id, first.id + 1)

    def test_no_args(self):
        """Test that the size is mandatory."""
        with self.assertRaises(TypeError):
            Square()

    def test_five_args(self):
        """Test that a fifth argument is refused."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_no_new_attribute(self):
        """Test that the square does not define its own size attribute."""
        with self.assertRaises(AttributeError):
            print(Square(5).__size)


class TestSquareSize(unittest.TestCase):
    """Test the size property of the Square class."""

    def test_getter(self):
        """Test that the getter returns the width."""
        self.assertEqual(Square(7).size, 7)

    def test_setter(self):
        """Test that the setter updates the size."""
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)

    def test_setter_sets_width_and_height(self):
        """Test that the setter updates both width and height."""
        square = Square(5)
        square.size = 10
        self.assertEqual((square.width, square.height), (10, 10))

    def test_string(self):
        """Test that a string size raises a width TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_float(self):
        """Test that a float size raises a width TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_none(self):
        """Test that a None size raises a width TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_string_from_setter(self):
        """Test that the setter refuses a string size."""
        square = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.size = "9"

    def test_zero(self):
        """Test that a zero size raises a width ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_negative(self):
        """Test that a negative size raises a width ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_negative_from_setter(self):
        """Test that the setter refuses a negative size."""
        square = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.size = -5


class TestSquareValidation(unittest.TestCase):
    """Test the inherited x and y validation of the Square class."""

    def test_string_x(self):
        """Test that a string x raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "3")

    def test_negative_x(self):
        """Test that a negative x raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -3)

    def test_string_y(self):
        """Test that a string y raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 3, "4")

    def test_negative_y(self):
        """Test that a negative y raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 3, -4)

    def test_size_before_x(self):
        """Test that the size is validated before x."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5", "3")


class TestSquareArea(unittest.TestCase):
    """Test the inherited area method of the Square class."""

    def test_small(self):
        """Test the area of a small square."""
        self.assertEqual(Square(2).area(), 4)

    def test_area(self):
        """Test the area of a square."""
        self.assertEqual(Square(5).area(), 25)

    def test_offsets_are_ignored(self):
        """Test that x, y and id do not change the area."""
        self.assertEqual(Square(3, 1, 3, 9).area(), 9)

    def test_after_size_change(self):
        """Test that the area follows a size change."""
        square = Square(5)
        square.size = 3
        self.assertEqual(square.area(), 9)


class TestSquareDisplay(unittest.TestCase):
    """Test the inherited display method of the Square class."""

    def capture(self, square):
        """Return what a square prints when displayed.

        Args:
            square: The square to display.

        Returns:
            The captured standard output as a string.
        """
        output = io.StringIO()
        sys.stdout = output
        square.display()
        sys.stdout = sys.__stdout__
        return output.getvalue()

    def test_one_by_one(self):
        """Test the display of the smallest square."""
        self.assertEqual(self.capture(Square(1)), "#\n")

    def test_size(self):
        """Test the display of a two by two square."""
        self.assertEqual(self.capture(Square(2)), "##\n##\n")

    def test_x(self):
        """Test that x offsets each row."""
        self.assertEqual(self.capture(Square(2, 2)), "  ##\n  ##\n")

    def test_x_and_y(self):
        """Test the display of a square with both offsets."""
        self.assertEqual(self.capture(Square(3, 1, 3)),
                         "\n\n\n ###\n ###\n ###\n")


class TestSquareStr(unittest.TestCase):
    """Test the __str__ method of the Square class."""

    def test_default_offsets(self):
        """Test the representation of a square without offsets."""
        self.assertEqual(str(Square(5, 0, 0, 1)), "[Square] (1) 0/0 - 5")

    def test_x(self):
        """Test the representation of a square with an x offset."""
        self.assertEqual(str(Square(2, 2, 0, 2)), "[Square] (2) 2/0 - 2")

    def test_x_and_y(self):
        """Test the representation of a square with both offsets."""
        self.assertEqual(str(Square(3, 1, 3, 3)), "[Square] (3) 1/3 - 3")

    def test_after_size_change(self):
        """Test that the representation follows a size change."""
        square = Square(5, 0, 0, 1)
        square.size = 10
        self.assertEqual(str(square), "[Square] (1) 0/0 - 10")


class TestSquareUpdateArgs(unittest.TestCase):
    """Test the update method of the Square class with args."""

    def test_no_args(self):
        """Test that no argument changes nothing."""
        square = Square(5, 0, 0, 1)
        square.update()
        self.assertEqual(str(square), "[Square] (1) 0/0 - 5")

    def test_id(self):
        """Test that the first argument is the id."""
        square = Square(5, 0, 0, 1)
        square.update(10)
        self.assertEqual(str(square), "[Square] (10) 0/0 - 5")

    def test_size(self):
        """Test that the second argument is the size."""
        square = Square(5, 0, 0, 1)
        square.update(1, 2)
        self.assertEqual(str(square), "[Square] (1) 0/0 - 2")

    def test_x(self):
        """Test that the third argument is x."""
        square = Square(5, 0, 0, 1)
        square.update(1, 2, 3)
        self.assertEqual(str(square), "[Square] (1) 3/0 - 2")

    def test_y(self):
        """Test that the fourth argument is y."""
        square = Square(5, 0, 0, 1)
        square.update(1, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (1) 3/4 - 2")

    def test_extra_args(self):
        """Test that extra arguments are ignored."""
        square = Square(5, 0, 0, 1)
        square.update(1, 2, 3, 4, 5)
        self.assertEqual(str(square), "[Square] (1) 3/4 - 2")

    def test_size_updates_height(self):
        """Test that the size argument updates the height too."""
        square = Square(5, 0, 0, 1)
        square.update(1, 7)
        self.assertEqual(square.height, 7)

    def test_none_id(self):
        """Test that a None id is assigned as is."""
        square = Square(5, 0, 0, 1)
        square.update(None)
        self.assertIsNone(square.id)

    def test_invalid_size(self):
        """Test that an invalid size is refused."""
        square = Square(5, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(1, "invalid")

    def test_zero_size(self):
        """Test that a zero size is refused."""
        square = Square(5, 0, 0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(1, 0)

    def test_negative_y(self):
        """Test that a negative y is refused."""
        square = Square(5, 0, 0, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square.update(1, 2, 3, -4)

    def test_args_before_kwargs(self):
        """Test that kwargs are skipped when args exists."""
        square = Square(5, 0, 0, 1)
        square.update(1, 2, y=9)
        self.assertEqual(str(square), "[Square] (1) 0/0 - 2")


class TestSquareUpdateKwargs(unittest.TestCase):
    """Test the update method of the Square class with kwargs."""

    def test_one_kwarg(self):
        """Test that one keyword argument is assigned."""
        square = Square(5, 0, 0, 1)
        square.update(x=12)
        self.assertEqual(str(square), "[Square] (1) 12/0 - 5")

    def test_two_kwargs(self):
        """Test that two keyword arguments are assigned."""
        square = Square(5, 0, 0, 1)
        square.update(size=7, y=1)
        self.assertEqual(str(square), "[Square] (1) 0/1 - 7")

    def test_all_kwargs(self):
        """Test that the order of keyword arguments is irrelevant."""
        square = Square(5, 0, 0, 1)
        square.update(size=7, id=89, y=1, x=2)
        self.assertEqual(str(square), "[Square] (89) 2/1 - 7")

    def test_unknown_kwarg(self):
        """Test that an unknown keyword argument is still assigned."""
        square = Square(5, 0, 0, 1)
        square.update(name="square")
        self.assertEqual(square.name, "square")

    def test_invalid_size(self):
        """Test that an invalid size is refused."""
        square = Square(5, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square.update(size="invalid")

    def test_negative_size(self):
        """Test that a negative size is refused."""
        square = Square(5, 0, 0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square.update(size=-7)

    def test_negative_x(self):
        """Test that a negative x is refused."""
        square = Square(5, 0, 0, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square.update(x=-1)


class TestSquareToDictionary(unittest.TestCase):
    """Test the to_dictionary method of the Square class."""

    def test_type(self):
        """Test that the returned value is a dictionary."""
        self.assertIs(type(Square(10, 2, 1).to_dictionary()), dict)

    def test_keys(self):
        """Test the keys of the returned dictionary."""
        self.assertEqual(sorted(Square(10).to_dictionary().keys()),
                         ["id", "size", "x", "y"])

    def test_values(self):
        """Test the values of the returned dictionary."""
        square = Square(10, 2, 1, 1)
        self.assertEqual(square.to_dictionary(),
                         {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_used_as_update(self):
        """Test that the dictionary can update another square."""
        first = Square(10, 2, 1, 1)
        second = Square(1, 1)
        second.update(**first.to_dictionary())
        self.assertEqual(str(first), str(second))

    def test_not_equal_after_update(self):
        """Test that two updated squares are still different objects."""
        first = Square(10, 2, 1, 1)
        second = Square(1, 1)
        second.update(**first.to_dictionary())
        self.assertNotEqual(first, second)

    def test_args(self):
        """Test that to_dictionary takes no argument."""
        with self.assertRaises(TypeError):
            Square(1).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
