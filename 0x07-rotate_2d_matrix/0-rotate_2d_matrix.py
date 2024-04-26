#!/usr/bin/python3

"""Clockwise rotation 2 dimensional"""


def rotate_2d_matrix(matrix):
    """ Function for clockwise rotation"""

    n = len(matrix[0])

    for i in range(n - 1, -1, -1):
        for j in range(0, n):
            matrix[j].append(matrix[i].pop(0))
