#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix"""
    n = len(matrix)

    for r in range(n):
        for c in range(r, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    for r in range(n):
        matrix[r].reverse()
