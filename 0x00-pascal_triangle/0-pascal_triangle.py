#!/usr/bin/python3
"""
ip _ is for ID
ipin _ is for inner ID
Pascal triangle
"""


def pascal_triangle(n):
    """Function for Pascal triangle"""
    triangle = []

    if (n <= 0):
        return triangle

    for ip in range(n):
        row = []
        for ipin in range(ip+1):
            if ipin == 0 or ipin == ip:
                row.append(1)
            else:
                row.append(triangle[ip - 1][ipin - 1] + triangle[ip - 1][ipin])
        triangle.append(row)

    return triangle
