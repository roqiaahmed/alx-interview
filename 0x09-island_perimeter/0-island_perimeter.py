#!/usr/bin/python3

"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """Island Perimeter method"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                for dr, dc in dir:
                    new_row, new_col = row + dr, col + dc
                    if (
                        not (0 <= new_row < rows and 0 <= new_col < cols)
                        or grid[new_row][new_col] == 0
                    ):
                        perimeter += 1
    return perimeter
