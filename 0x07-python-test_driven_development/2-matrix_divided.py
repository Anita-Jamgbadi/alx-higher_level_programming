#!/usr/bin/python3
""" This modules is built to divide all elements of a matrix """


def matrix_divided(matrix, div):
    """ divides a matrix of integers """

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError('matrix must be a matrix(list of lists)\
                of integers/float')

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix(list of lists) \
                    of integers/float')
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError('matrix must be a matrix(list of lists) \
                        of integers/float')

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return ([list(map(lambda i: round(i / div, 2), row)) for row in matrix])
