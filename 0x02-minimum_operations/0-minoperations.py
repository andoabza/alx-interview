#!/usr/bin/env python3
"""minimum operations"""


def minOperations(n):
    """return number to rech N"""
    if n <= 1:
        return 0
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return minOperations(n // i) + i
        