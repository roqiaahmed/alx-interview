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
    # stack = []
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
    # for row in range(rows):
    #     for col in range(cols):
    #         if grid[row][col] == 1:
    #             stack.append((row, col))
    #             break
    #     if len(stack) != 0:
    #         break
    # while stack:
    #     row, col = stack.pop()
    #     grid[row][col] = "A"
    #     for n_row, n_col in dir:
    #         new_row = row + n_row
    #         new_col = col + n_col
    #         if (0 <= new_row < rows) and (0 <= new_col < cols):
    #             if grid[new_row][new_col] == 1:
    #                 stack.append((new_row, new_col))
    #             if grid[new_row][new_col] == 0:
    #                 perimeter += 1
    #         else:
    #             perimeter += 1
    return perimeter
