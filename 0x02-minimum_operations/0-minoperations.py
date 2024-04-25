#!/usr/bin/python3
"""
Tasks 0: write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    if n == 1:
        return 0

    ops = 0
    H = 1
    while H < n:
        if n % H == 0:
            H_copy = H
            ops += 1
        H += H_copy
        ops += 1

    if H == n:
        return ops
    else:
        return 0
