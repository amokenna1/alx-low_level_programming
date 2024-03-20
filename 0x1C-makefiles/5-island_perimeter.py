#!/usr/bin/python3
"""Defines a function to calculate the perimeter of an island."""


def calculate_island_perimeter(grid):
    """
    Calculate the perimeter of an island described in a grid.

    Args:
        grid: A list of lists of integers:
            - 0 represents a water zone
            - 1 represents a land zone
            - Each cell is a square with side length 1
            - Grid cells are connected horizontally/vertically (not diagonally)
            - Grid is rectangular, width and height don’t exceed 100
            - Grid is completely surrounded by water, and there is one island (or nothing)
            - The island doesn’t have “lakes” (water inside that isn’t connected to the water around the island)

    Returns:
        The perimeter of the island.
    """
    width = len(grid[0])
    height = len(grid)
    total_edges = 0
    total_cells = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                total_cells += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    total_edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    total_edges += 1

    return total_cells * 4 - total_edges * 2
