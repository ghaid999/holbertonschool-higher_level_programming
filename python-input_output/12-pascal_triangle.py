#!/usr/bin/python3
""" Pascal's Triangle."""


def pascal_triangle(n):
    """Return a list of lists ."""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Create a row of all 1
        row = [1] * (i + 1)

        # Fill the middle values
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
