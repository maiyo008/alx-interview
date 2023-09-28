#!/usr/bin/python3
"""
"""


def island_perimeter(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4  # Initialize with 4 sides

                # Check left neighbor
                if col > 0 and grid[row][col - 1] == 1:
                    # Subtract 2 because both sides are connected
                    perimeter -= 2

                # Check top neighbor
                if row > 0 and grid[row - 1][col] == 1:
                    # Subtract 2 because both sides are connected
                    perimeter -= 2

    return perimeter
