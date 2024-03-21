#!/usr/bin/python3
"""Minimum operations in python3"""


def minOperations(n):
    """calculates the least number of operations needed"""
    if not isinstance(n, int):
        return 0

    operation = 0
    iterator = 2
    while (iterator <= n):
        if not (n % iterator):
            n = int(n / iterator)
            operations += iterator
            iterator = 1
        iterator += 1
    return operations
