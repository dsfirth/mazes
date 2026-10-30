from src.cell import Cell
from src.grid import Grid

import enum
import random


def __mazefy(cell: Cell, field: list[Cell], state: any):
    cell.state = state
    field.remove(cell)


def wilsons(grid: Grid) -> Grid:
    """
    Wilson's algorithm generates a uniform random spanning tree of a connected graph:
    1. Choose an arbitrary vertex (cell) and add it to the tree (maze),
    2. Choose a vertex not yet in the tree and perform a random walk from it,
    3. When the walk reaches a vertex already in the tree, erase any loops from the walk and add the resulting path to the tree,
    4. Repeat steps 2 and 3 until every vertex (cell) is in the tree.
    """
    State = enum.Enum('State', [('MAZE', 1), ('WALK', 2)])

    field = list(grid.each_cell())

    # track `state` on each cell
    for cell in field:
        cell.state = None

    # init w/ random cell
    __mazefy(random.choice(field), field, State.MAZE)

    while field:
        # do a random walk
        start = random.choice(field)
        path = [start]  # ordered cells in the current walk
        head = start

        while head.state is not State.MAZE:
            head.state = State.WALK # do this _after_ confirming cell is not already in the maze
            next = random.choice(
                list(filter(None, [head.north, head.east, head.south, head.west])))

            if next.state is State.WALK:
                # erase everything in path after next
                path = path[:path.index(next)]
            else:
                path.append(next)

            head = next

        # The walk has reached the existing maze.
        for i in range(len(path) - 1):
            path[i].link(path[i + 1])

        for cell in path:
            __mazefy(cell, field, State.MAZE)

    return grid
