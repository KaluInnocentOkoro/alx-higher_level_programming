#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_sq = [[x ** 2 for x in rows] for rows in matrix]
    return matrix_sq