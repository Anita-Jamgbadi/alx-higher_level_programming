#!/usr/bin/python3
""" returns a list of lists of ints representing a
pascal's triangle of n """


def pascal_triangle(n):
    """ As above """

    triangle = [[1]]

    if n <= 0:
        return []

    while len(triangle) != n:
        tier = triangle[-1]
        temp = [1]
        for i in range(len(tier) - 1):
            temp.append(tier[i] + tier[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
