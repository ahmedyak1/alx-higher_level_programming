#!/usr/bin/python3
"""matrix_divided function
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

	args : matrix,div
    Returns: matric division
    """
    rs = None
    erro = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(erro)

    for k in matrix:
        if not k or not isinstance(k, list):
            raise TypeError(erro)

        for m in k:
            if not isinstance(m, int) and not isinstance(m, float):
                raise TypeError(erro)

        if rs is None:
            rs = len(k)
        elif rs != len(k):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    mitrix = [[round(m / div, 2) for m in k] for k in matrix]

    return mitrix

