#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): A list of list of integers representing
        the island. 0 represents water, 1 represents land.

    Returns:
        int: The perimeter of the island.

    Constraints:
        - The grid is rectangular, width and height not exceeding 100.
        - The grid is completely surrounded by water.
        - There is only one island (or nothing).
        - The island doesn't have "lakes" (water inside not connected
          to surrounding water).
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
