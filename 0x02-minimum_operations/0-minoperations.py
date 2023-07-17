#!/usr/bin/python3
"""
0-minoperations.py
"""
def minOperations(n: int) -> int:
    """
    Minimum Operations
    """
    if n == 1:
        return 0

    operations = 0
    h_count = 1
    clipboard = 0

    while h_count < n:
        if n % h_count == 0:
            clipboard = h_count
        h_count += clipboard
        operations += 1

    return operations
