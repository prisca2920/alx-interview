#!/usr/bin/python3
"""rotating a 2d matrix 90 degrees"""


def rotate_2d_matrix(matrix):
    """rotating a 2d matrix 90 degrees"""
    left_col, right_col = 0, len(matrix) - 1

    while left_col < right_col:
        for i in range(right_col - left_col):
            up_row, down_row = left_col, right_col

            # Save the up-left value
            up_left_value = matrix[up_row][left_col + i]

            # Move the down-left value to the up-left position
            matrix[up_row][left_col + i] = matrix[down_row - i][left_col]

            # Move the down-right value to the down-left position
            matrix[down_row - i][left_col] = matrix[down_row][right_col - i]

            # Move the up-right value to the down-right position
            matrix[down_row][right_col - i] = matrix[up_row + i][right_col]

            # Move the saved up-left value to the up-right position
            matrix[up_row + i][right_col] = up_left_value

        right_col -= 1
        left_col += 1
