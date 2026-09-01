from enum import Enum
import random

from src.grid import Grid

State = Enum('State', [('FRONTIER', 1), ('IN', 2)])


def prims(grid: Grid) -> Grid:
    """
    Prim's algorithm
    """
    explored = []
    frontier = []

    # init w/ random cell
    frontier.append(grid[random.randint(0, grid.rows - 1), random.randint(0, grid.columns - 1)])

    # expand into a random `frontier` cell, and grow frontier into neighbour(s)
    while frontier:
        next = random.choice(frontier)
        # print(f'expand into [{next.row}, {next.column}]')

        # rather than tracking `explored`, use a property on the Cell (cell.state = FRONTIER | IN)
        neighbours = filter(lambda c: c in explored, [next.north, next.east, next.south, next.west])
        if neighbours:
            previous = random.choice(neighbours)
            previous.link(next)

        explored.append(next)
        frontier.remove(next)

        for neighbour in filter(None, [next.north, next.east, next.south, next.west]):
            if neighbour not in explored:
                if neighbour not in frontier:
                    # print(f'add [{neighbour.row}, {neighbour.column}] into frontier')
                    frontier.append(neighbour)

    return grid
