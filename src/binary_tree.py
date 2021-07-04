import random


def binary_tree(grid):
    for cell in grid.each_cell():
        neighbors = list(filter(None, [cell.north, cell.east]))

        if(neighbors):
            cell.link(random.choice(neighbors))
