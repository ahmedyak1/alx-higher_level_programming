#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cop = matrix.copy()
        matrix_cop = [[k**2 for k in row] for row in matrix]
    return (matrix_cop)

