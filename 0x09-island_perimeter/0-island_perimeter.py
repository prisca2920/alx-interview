#!/usr/bin/python3
"""perimeter of an island"""


def island_perimeter(grid):
    """calculates the perimeter of an island"""
    perimeter = 0
    for row in grid + list(map(list, zip(*grid))):
        for i1, i2 in zip([0] + row, row + [0]):
            perimeter += int(i1 != i2)
    return perimeter
