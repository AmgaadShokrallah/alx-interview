#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate two dimension matrix 90 degrees clockwise
    """
    n = len(matrix)
    for r in range(int(n / 2)):
        y = (n - r - 1)
        for j in range(r, y):
            x = (n - 1 - j)
            tmp = matrix[r][j]
            matrix[r][j] = matrix[x][r]
            matrix[x][r] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tmp
