from src.cell import Cell

import dataclasses
import enum


class Direction(enum.Enum):
    NORTH = "north"
    EAST = "east"
    SOUTH = "south"
    WEST = "west"


class Grid:
    def __init__(self, rows, columns):
        if not (1 <= rows <= 200 and 1 <= columns <= 200):
            raise ValueError('rows and columns must each be between 1 and 200')

        self.rows = rows
        self.columns = columns

        self.__entrance = Opening(0, 0, Direction.NORTH)
        self.__exit = Opening(rows - 1, columns - 1, Direction.SOUTH)

        self.__grid = self.prepare_grid()
        self.configure_cells()

    def __getitem__(self, tuple):
        row, column = tuple
        return self.__grid[row][column] if 0 <= row < self.rows and 0 <= column < self.columns else None

    def passage_open(self, cell: Cell, side: Direction) -> bool:
        neighbour = getattr(cell, side.value)

        if neighbour is not None:
            return cell.linked(neighbour)

        opening = Opening(cell.row, cell.column, side)
        return opening == self.__entrance or opening == self.__exit

    def prepare_grid(self):
        grid = list()

        for i in range(self.rows):
            grid.append(list())

            for j in range(self.columns):
                grid[i].append(Cell(i, j))

        return grid

    def configure_cells(self):
        for cell in self.each_cell():
            row, col = cell.row, cell.column

            cell.north = self[row - 1, col]
            cell.east = self[row, col + 1]
            cell.south = self[row + 1, col]
            cell.west = self[row, col - 1]

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                yield cell

    def each_row(self):
        for row in self.__grid:
            yield row


@dataclasses.dataclass(frozen=True)
class Opening:
    row: int
    column: int
    side: Direction
