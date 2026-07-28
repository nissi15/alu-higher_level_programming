#!/usr/bin/python3
"""Defines a matrix division function.

The module holds a single function that divides every element of a matrix
by a number and returns the result rounded to two decimal places.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with all elements divided by div.

    Args:
        matrix: A list of lists of integers or floats.
        div: The number used to divide every element.

    Raises:
        TypeError: If matrix is not a matrix of numbers, if the rows have
            different sizes, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(error)
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(error)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error)
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
