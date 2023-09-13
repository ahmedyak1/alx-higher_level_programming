#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixnew = matrix.copy()
    for k in range(len(matrix)):
        matrixnew[k] = list(map(lambda m: m**2, matrix[k]))
    return (matrixnew)

