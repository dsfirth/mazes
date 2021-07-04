from src.cell import Cell


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.__grid = self.prepare_grid()
        self.configure_cells()

    def __getitem__(self, tuple):
        row, column = tuple
        return self.__grid[row][column] if 0 <= row < self.rows and 0 <= column < self.columns else None

    def __str__(self):
        output = "+" + "---+" * self.columns + "\n"

        for row in self.each_row():
            top = "|"
            bottom = "+"

            for cell in row:
                body = "   "  # that's THREE (3) spaces!
                east_boundary = " " if cell.linked(cell.east) else "|"
                top += body + east_boundary

                # three spaes below, too
                south_boundary = "   " if cell.linked(cell.south) else "---"
                corner = "+"
                bottom += south_boundary+corner

            output += top + "\n"
            output += bottom + "\n"

        return output

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
