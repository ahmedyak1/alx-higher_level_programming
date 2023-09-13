#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    a = list(map(lambda k: list(map(lambda m: m**2, k)), matrix))
    return (a)

