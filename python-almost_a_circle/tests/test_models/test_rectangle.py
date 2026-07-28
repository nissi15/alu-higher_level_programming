#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Test the instantiation of the Rectangle class."""

    def test_is_a_base(self):
        """Test that a rectangle is a Base instance."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_two_args(self):
        """Test that width and height are enough to instantiate."""
        rectangle = Rectangle(10, 2)
        self.assertEqual((rectangle.width, rectangle.height), (10, 2))

    def test_default_x_and_y(self):
        """Test that x and y default to zero."""
        rectangle = Rectangle(10, 2)
        self.assertEqual((rectangle.x, rectangle.y), (0, 0))

    def test_five_args(self):
        """Test that all five arguments are assigned."""
        rectangle = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual((rectangle.width, rectangle.height, rectangle.x,
                          rectangle.y, rectangle.id), (10, 2, 3, 4, 5))

    def test_id_is_incremented(self):
        """Test that consecutive rectangles get consecutive ids."""
        first = Rectangle(10, 2)
        second = Rectangle(2, 10)
        self.assertEqual(second.id, first.id + 1)

    def test_no_args(self):
        """Test that width and height are mandatory."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test that height is mandatory."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_six_args(self):
        """Test that a sixth argument is refused."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_is_private(self):
        """Test that width is a private attribute."""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2).__width)

    def test_height_is_private(self):
        """Test that height is a private attribute."""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2).__height)

    def test_x_is_private(self):
        """Test that x is a private attribute."""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2).__x)

    def test_y_is_private(self):
        """Test that y is a private attribute."""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2).__y)


class TestRectangleWidth(unittest.TestCase):
    """Test the width validation of the Rectangle class."""

    def test_setter(self):
        """Test that the setter updates the width."""
        rectangle = Rectangle(10, 2)
        rectangle.width = 7
        self.assertEqual(rectangle.width, 7)

    def test_string(self):
        """Test that a string width raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_float(self):
        """Test that a float width raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 2)

    def test_none(self):
        """Test that a None width raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_list(self):
        """Test that a list width raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1], 2)

    def test_bool(self):
        """Test that a boolean width raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_zero(self):
        """Test that a zero width raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_negative(self):
        """Test that a negative width raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_negative_from_setter(self):
        """Test that the setter refuses a negative width."""
        rectangle = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.width = -10

    def test_width_before_height(self):
        """Test that width is validated before height."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", "2")


class TestRectangleHeight(unittest.TestCase):
    """Test the height validation of the Rectangle class."""

    def test_setter(self):
        """Test that the setter updates the height."""
        rectangle = Rectangle(10, 2)
        rectangle.height = 7
        self.assertEqual(rectangle.height, 7)

    def test_string(self):
        """Test that a string height raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_float(self):
        """Test that a float height raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, 2.5)

    def test_none(self):
        """Test that a None height raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)

    def test_dict(self):
        """Test that a dictionary height raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {})

    def test_zero(self):
        """Test that a zero height raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_negative(self):
        """Test that a negative height raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_negative_from_setter(self):
        """Test that the setter refuses a negative height."""
        rectangle = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.height = -2

    def test_height_before_x(self):
        """Test that height is validated before x."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2", "3")


class TestRectangleX(unittest.TestCase):
    """Test the x validation of the Rectangle class."""

    def test_setter(self):
        """Test that the setter updates x."""
        rectangle = Rectangle(10, 2)
        rectangle.x = 7
        self.assertEqual(rectangle.x, 7)

    def test_zero_is_valid(self):
        """Test that a zero x is accepted."""
        self.assertEqual(Rectangle(10, 2, 0).x, 0)

    def test_string(self):
        """Test that a string x raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3")

    def test_dict(self):
        """Test that a dictionary x raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_none(self):
        """Test that a None x raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, None)

    def test_negative(self):
        """Test that a negative x raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3)

    def test_negative_from_setter(self):
        """Test that the setter refuses a negative x."""
        rectangle = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rectangle.x = -3

    def test_x_before_y(self):
        """Test that x is validated before y."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3", "4")


class TestRectangleY(unittest.TestCase):
    """Test the y validation of the Rectangle class."""

    def test_setter(self):
        """Test that the setter updates y."""
        rectangle = Rectangle(10, 2)
        rectangle.y = 7
        self.assertEqual(rectangle.y, 7)

    def test_zero_is_valid(self):
        """Test that a zero y is accepted."""
        self.assertEqual(Rectangle(10, 2, 0, 0).y, 0)

    def test_string(self):
        """Test that a string y raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "4")

    def test_float(self):
        """Test that a float y raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, 4.5)

    def test_none(self):
        """Test that a None y raises a TypeError."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, None)

    def test_negative(self):
        """Test that a negative y raises a ValueError."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_negative_from_setter(self):
        """Test that the setter refuses a negative y."""
        rectangle = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rectangle.y = -1


class TestRectangleArea(unittest.TestCase):
    """Test the area method of the Rectangle class."""

    def test_small(self):
        """Test the area of a small rectangle."""
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_rectangle(self):
        """Test the area of a rectangle."""
        self.assertEqual(Rectangle(2, 10).area(), 20)

    def test_with_id(self):
        """Test that x, y and id do not change the area."""
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_one_by_one(self):
        """Test the area of the smallest rectangle."""
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_after_update(self):
        """Test that the area follows an update."""
        rectangle = Rectangle(2, 10)
        rectangle.width = 5
        self.assertEqual(rectangle.area(), 50)

    def test_large(self):
        """Test the area of a large rectangle."""
        self.assertEqual(Rectangle(999999999, 999999999).area(),
                         999999998000000001)

    def test_args(self):
        """Test that area takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).area(1)


class TestRectangleDisplay(unittest.TestCase):
    """Test the display method of the Rectangle class."""

    def capture(self, rectangle):
        """Return what a rectangle prints when displayed.

        Args:
            rectangle: The rectangle to display.

        Returns:
            The captured standard output as a string.
        """
        output = io.StringIO()
        sys.stdout = output
        rectangle.display()
        sys.stdout = sys.__stdout__
        return output.getvalue()

    def test_one_by_one(self):
        """Test the display of the smallest rectangle."""
        self.assertEqual(self.capture(Rectangle(1, 1)), "#\n")

    def test_square_shape(self):
        """Test the display of a two by two rectangle."""
        self.assertEqual(self.capture(Rectangle(2, 2)), "##\n##\n")

    def test_wide(self):
        """Test the display of a wide rectangle."""
        self.assertEqual(self.capture(Rectangle(4, 2)), "####\n####\n")

    def test_x(self):
        """Test that x offsets each row."""
        self.assertEqual(self.capture(Rectangle(3, 2, 1)), " ###\n ###\n")

    def test_y(self):
        """Test that y prints leading new lines."""
        self.assertEqual(self.capture(Rectangle(2, 1, 0, 2)), "\n\n##\n")

    def test_x_and_y(self):
        """Test the display of a rectangle with both offsets."""
        self.assertEqual(self.capture(Rectangle(2, 3, 2, 2)),
                         "\n\n  ##\n  ##\n  ##\n")

    def test_args(self):
        """Test that display takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).display(1)


class TestRectangleStr(unittest.TestCase):
    """Test the __str__ method of the Rectangle class."""

    def test_full(self):
        """Test the representation of a fully described rectangle."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")

    def test_default_y(self):
        """Test the representation with a default y."""
        self.assertEqual(str(Rectangle(5, 5, 1, 0, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_default_x_and_y(self):
        """Test the representation with default offsets."""
        self.assertEqual(str(Rectangle(1, 2, 0, 0, 7)),
                         "[Rectangle] (7) 0/0 - 1/2")

    def test_after_update(self):
        """Test that the representation follows an update."""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/3")

    def test_args(self):
        """Test that __str__ takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).__str__(1)


class TestRectangleUpdateArgs(unittest.TestCase):
    """Test the update method of the Rectangle class with args."""

    def test_no_args(self):
        """Test that no argument changes nothing."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update()
        self.assertEqual(str(rectangle), "[Rectangle] (1) 10/10 - 10/10")

    def test_id(self):
        """Test that the first argument is the id."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(89)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 10/10")

    def test_width(self):
        """Test that the second argument is the width."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(89, 2)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/10")

    def test_height(self):
        """Test that the third argument is the height."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(89, 2, 3)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/3")

    def test_x(self):
        """Test that the fourth argument is x."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(89, 2, 3, 4)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/10 - 2/3")

    def test_y(self):
        """Test that the fifth argument is y."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/3")

    def test_extra_args(self):
        """Test that extra arguments are ignored."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/3")

    def test_none_id(self):
        """Test that a None id is assigned as is."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(None)
        self.assertIsNone(rectangle.id)

    def test_invalid_width(self):
        """Test that an invalid width is refused."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(89, "invalid")

    def test_zero_width(self):
        """Test that a zero width is refused."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle.update(89, 0)

    def test_negative_y(self):
        """Test that a negative y is refused."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rectangle.update(89, 2, 3, 4, -5)

    def test_args_before_kwargs(self):
        """Test that kwargs are skipped when args exists."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(89, 2, height=7)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/10")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Test the update method of the Rectangle class with kwargs."""

    def test_one_kwarg(self):
        """Test that one keyword argument is assigned."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(height=1)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 10/10 - 10/1")

    def test_two_kwargs(self):
        """Test that two keyword arguments are assigned."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(width=1, x=2)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 2/10 - 1/10")

    def test_all_kwargs(self):
        """Test that the order of keyword arguments is irrelevant."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(y=1, width=2, x=3, id=89, height=4)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 3/1 - 2/4")

    def test_unknown_kwarg(self):
        """Test that an unknown keyword argument is still assigned."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(name="rectangle")
        self.assertEqual(rectangle.name, "rectangle")

    def test_unknown_kwarg_keeps_attributes(self):
        """Test that an unknown keyword leaves the attributes alone."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(name="rectangle")
        self.assertEqual(str(rectangle), "[Rectangle] (1) 10/10 - 10/10")

    def test_invalid_width(self):
        """Test that an invalid width is refused."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle.update(width="invalid")

    def test_negative_height(self):
        """Test that a negative height is refused."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle.update(height=-1)

    def test_negative_x(self):
        """Test that a negative x is refused."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rectangle.update(x=-1)


class TestRectangleToDictionary(unittest.TestCase):
    """Test the to_dictionary method of the Rectangle class."""

    def test_type(self):
        """Test that the returned value is a dictionary."""
        self.assertIs(type(Rectangle(10, 2, 1, 9).to_dictionary()), dict)

    def test_keys(self):
        """Test the keys of the returned dictionary."""
        self.assertEqual(sorted(Rectangle(10, 2).to_dictionary().keys()),
                         ["height", "id", "width", "x", "y"])

    def test_values(self):
        """Test the values of the returned dictionary."""
        rectangle = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(rectangle.to_dictionary(),
                         {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_used_as_update(self):
        """Test that the dictionary can update another rectangle."""
        first = Rectangle(10, 2, 1, 9, 1)
        second = Rectangle(1, 1)
        second.update(**first.to_dictionary())
        self.assertEqual(str(first), str(second))

    def test_not_equal_after_update(self):
        """Test that two updated rectangles are still different objects."""
        first = Rectangle(10, 2, 1, 9, 1)
        second = Rectangle(1, 1)
        second.update(**first.to_dictionary())
        self.assertNotEqual(first, second)

    def test_args(self):
        """Test that to_dictionary takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
