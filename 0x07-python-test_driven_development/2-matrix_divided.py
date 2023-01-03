#!/usr/bin/python3
"""Divides a matrix"""


def matrix_divided(matrix, div):
    """"Function divides all elements of a matrix.
    Args:
        matrix (list)
        div (int or float)
    Returns: A new matrix containing the divided elements
    """
    err_msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    err_msg2 = "Each row of the matrix must have the same size"
    # check for div
    if div != 0:
        if isinstance(div, int) or isinstance(div, float):
            pass
        else:
            raise TypeError("div must be a number")
    else:
        raise ZeroDivisionError("division by zero")
    # check for matrix
    if isinstance(matrix, list) and len(matrix):
        for row in matrix:
            if isinstance(row, list) and len(row):
                if len(row) == len(matrix[0]):
                    for ele in row:
                        if isinstance(ele, int) or isinstance(ele, float):
                            pass
                        else:
                            raise TypeError(err_msg1)
                else:
                    raise TypeError(err_msg2)
            else:
                raise TypeError(err_msg1)
    else:
        raise TypeError(err_msg1)
    new_matrix = [[round((ele / div), 2) for ele in row] for row in matrix]
    return new_matrix
