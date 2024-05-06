#!/usr/bin/python3

"""Island perimeter solution module"""


def island_perimeter_old(grid):
    """module A to return perimeter"""
    island = 0

    rows, cols = len(grid), len(grid[0])

    for outer in range(rows):
        for inner in range(cols):
            if grid[outer][inner] == 1:
                island += 4

                # Check neighbors and subtract if neighbor is also land
                if outer > 0 and grid[outer - 1][inner] == 1:
                    island -= 2
                if inner > 0 and grid[outer][inner - 1] == 1:
                    island -= 2

    return island


def island_perimeter(grid):
    """Module B to help"""
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for outer in range(rows):
        for inner in range(cols):
            if grid[outer][inner] == 1:
                perimeter += 4  # Each land cell adds 4 to the perimeter

                if outer > 0 and grid[outer - 1][inner] == 1:  # Up
                    perimeter -= 1
                if outer < rows - 1 and grid[outer + 1][inner] == 1:  # Down
                    perimeter -= 1
                if inner > 0 and grid[outer][inner - 1] == 1:  # Left
                    perimeter -= 1
                if inner < cols - 1 and grid[outer][inner + 1] == 1:  # Right
                    perimeter -= 1

    return perimeter
