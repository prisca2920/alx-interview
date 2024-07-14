#!/usr/bin/python3
"""minimum  operations to copy paste"""


def minOperations(n):
    """minimum  operations to copy paste"""

    if (n < 2):
        return 0

    operations, chars = 0, 2
    while chars <= n:
        if n % chars == 0:
            operations += chars
            n = n / chars
            chars -= 1
        chars += 1
    return operations
