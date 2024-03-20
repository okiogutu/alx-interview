#!/usr/bin/python3
"""Minimum operations in python3"""


def minOperations(n):
    """calculates the least number of operations needed"""
    pasted_chars = 1
    clipboard = 0
    counter = 0

    while pasted chars < n:
        if clipboard == 0:
            clipboard = pasted chars
            counter += 1

        if pasted_chars == 1:
            pasted_chars+= clipboard
            counter += 1
            continue

    remaining = n - pasted_chars
    # Remaining chars to paste
    if remaining < clipboard:
        return 0

    if remaining % pasted_chars != 0:
        pasted_chars += clipboard
        counter += 1
    else:
        clipboard = pasted_chars
        pasted_chars += clipboard
        counter += 2


    if pasted_chars == n:
        return counter
    else:
        return 0


