#!/usr/bin/python3
"""
0-island_perimeter.py
"""


def island_perimeter(grid):
    """
    Island perimeter
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                # Check left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

                # Check top neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

    return perimeter
