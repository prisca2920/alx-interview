#!/usr/bin/python3
"""
N Queens Problem Solver
"""

import sys

# Validate command line arguments
if len(sys.argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    board_size = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if board_size < 4:
    print('N must be at least 4')
    exit(1)


def solve_nqueens(n):
    '''Recursive solver for the N Queens problem'''
    if n == 0:
        return [[]]
    smaller_solutions = solve_nqueens(n - 1)
    return [solution + [(n, i + 1)]
            for i in range(board_size)
            for solution in smaller_solutions
            if is_safe_placement((n, i + 1), solution)]


def is_under_attack(square, queen):
    '''Check if two queens attack each other'''
    (row1, col1) = square
    (row2, col2) = queen
    return (row1 == row2) or (col1 == col2) or\
        abs(row1 - row2) == abs(col1 - col2)


def is_safe_placement(new_queen, queens):
    '''Check if a new queen can be placed safely'''
    for queen in queens:
        if is_under_attack(new_queen, queen):
            return False
    return True


# Print solutions in reversed order
for solution in reversed(solve_nqueens(board_size)):
    formatted_solution = []
    for pos in [list(position) for position in solution]:
        formatted_solution.append([i - 1 for i in pos])
    print(formatted_solution)
