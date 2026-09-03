from enum import Enum
import random

from src.grid import Grid


def prims(grid: Grid) -> Grid:
    """
    Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted
    undirected graph:
    1. Choose an arbitrary vertex (cell) from G (the maze) and add it to some (initially empty) set V,
    2. Choose a random edge that connects a cell in V with another vertex (cell) _not_ in V,
    3. Add that edge to the minimal spanning tree, and the edge's other vertex (cell) to V,
    4. Repeat steps 2 and 3 until V includes every vertex (cell) in G (the maze).
    """
    State = Enum('State', [('FRONTIER', 1), ('IN', 2)])

    # track `state` on each cell
    for cell in grid.each_cell():
        cell.state = None

    # init w/ random cell
    start = grid[random.randint(0, grid.rows - 1), random.randint(0, grid.columns - 1)]
    start.state = State.FRONTIER

    frontier = [start]

    # expand into a random `frontier` cell, and grow frontier into neighbour(s)
    while frontier:
        next = random.choice(frontier)
        next.state = State.IN

        # rather than tracking `explored`, use a property on the Cell (cell.state = FRONTIER | IN)
        neighbours = list(filter(None, [next.north, next.east, next.south, next.west]))
        frontierNeighbours = list(filter(lambda c: c is not None and c.state is State.IN, neighbours))
        if frontierNeighbours:
            previous = random.choice(frontierNeighbours)
            previous.link(next)

        frontier.remove(next)

        # map the frontier cells
        for neighbour in filter(lambda c: c.state is None, neighbours):
            neighbour.state = State.FRONTIER
            frontier.append(neighbour)

    return grid
