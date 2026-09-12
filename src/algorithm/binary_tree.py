import random

from src.grid import Grid


def binary_tree(grid: Grid) -> Grid:
    for cell in grid.each_cell():
        neighbors = list(filter(None, [cell.north, cell.east]))

        if neighbors:
            cell.link(random.choice(neighbors))

    return grid
