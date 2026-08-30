import random

from src.grid import Grid

# Prim's algorithm
def prims(grid: Grid) -> Grid:
    grid = [[0 for _ in range(grid.columns)] for _ in range(grid.rows)]
    frontier = []

    # init w/ random cell
    frontier.append([random(range(grid.columns)), random(range(grid.rows))])

    # grow into a random `frontier` cell


    return grid