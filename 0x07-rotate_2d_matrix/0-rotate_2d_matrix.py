#!/usr/bin/python3
"""
Module for rotating a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
    matrix (List[List[int]]): The input n x n 2D matrix.

    Returns:
    None. The matrix is edited in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]


if __name__ == "__main__":
    # Test cases
    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    print("Original:")
    print(matrix1)
    rotate_2d_matrix(matrix1)
    print("Rotated:")
    print(matrix1)

    matrix2 = [[1]]
    print("\nOriginal:")
    print(matrix2)
    rotate_2d_matrix(matrix2)
    print("Rotated:")
    print(matrix2)

    matrix3 = [[1, 2],
               [3, 4]]
    print("\nOriginal:")
    print(matrix3)
    rotate_2d_matrix(matrix3)
    print("Rotated:")
    print(matrix3)

    matrix4 = [[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12],
               [13, 14, 15, 16]]
    print("\nOriginal:")
    print(matrix4)
    rotate_2d_matrix(matrix4)
    print("Rotated:")
    print(matrix4)
