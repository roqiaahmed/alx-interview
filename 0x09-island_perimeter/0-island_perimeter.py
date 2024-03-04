#!/usr/bin/python3

"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """Island Perimeter method"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    dir = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    hash = []

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                hash.append((row, col))
                print(f"out side =====>  {row} {col}")
                break
        if len(hash) != 0:
            break
    while hash:
        row, col = hash.pop()
        grid[row][col] = "A"
        for n_row, n_col in dir:
            new_row = row + n_row
            new_col = col + n_col
            if not (0 <= new_row < rows) or not (0 <= new_col < cols):
                continue
            if grid[new_row][new_col] == 1:
                hash.append((new_row, new_col))
            if grid[new_row][new_col] == 0:
                print(
                    f"in side =====> [new_row][new_col]  {new_row}  {new_col}  {perimeter}"
                )
                perimeter += 1
    return perimeter
