#!/usr/bin/env python3
"""minimum operations"""


def minOperations(N):
    """return number to rech N"""
    if N <= 1:
        return 0
    else:
        for i in range(2, N + 1):
            if N % i == 0:
                return minOperations(N // i) + i
        