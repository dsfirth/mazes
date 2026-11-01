import click
import png

from src.grid import Direction, Grid

# define some constants
cell_size = 10
margin = 5


def png_encoder(grid: Grid, output: click.File) -> None:
    black_pixel = [0, 0, 0]
    white_pixel = [255, 255, 255]
    height, width = cell_size * grid.rows + 1, cell_size * grid.columns + 1

    # initialize the maze canvas w/ all walls up
    rows = []
    for y in range(height):
        row = []
        for x in range(width):
            # Generate pixel values based on position
            if y % cell_size == 0 or x % cell_size == 0:
                row.extend(black_pixel)
            else:
                row.extend(white_pixel)

        rows.append(row)

    # remove walls between linked cells
    for row in grid.each_row():
        for cell in row:
            # check for an open passage to the NORTH, if 1st row
            if cell.row == 0 and grid.passage_open(cell, Direction.NORTH):
                # remove north wall
                y, x = cell_size * cell.row, 3 * cell_size * cell.column + 3
                rows[y][x:x + (3 * (cell_size - 1))] = white_pixel * (cell_size - 1)

            # check east neighbour; if linked, ...
            if grid.passage_open(cell, Direction.EAST):
                # remove east wall
                y, x = cell_size * cell.row + 1, 3 * cell_size * (cell.column + 1)
                for yOffset in range(cell_size - 1):
                    rows[y + yOffset][x:x + 3] = white_pixel

            # check south neighbour; if linked, ...
            if grid.passage_open(cell, Direction.SOUTH):
                # remove south wall
                y, x = cell_size * (cell.row + 1), 3 * cell_size * cell.column + 3
                rows[y][x:x + (3 * (cell_size - 1))] = white_pixel * (cell_size - 1)

            # check for an open passage to the WEST, if 1st column
            if cell.column == 0 and grid.passage_open(cell, Direction.WEST):
                # remove west wall
                y, x = cell_size * cell.row + 1, 3 * cell_size * cell.column
                for yOffset in range(cell_size - 1):
                    rows[y + yOffset][x:x + 3] = white_pixel

    # add margin
    for _ in range(margin):
        row = white_pixel * width
        rows.insert(0, row)  # top margin

        row = white_pixel * width
        rows.append(row)  # bottom margin

    for row in rows:
        row[0:0] = white_pixel * margin  # left margin
        row.extend(white_pixel * margin)  # right margin

    height += 2 * margin
    width += 2 * margin

    writer = png.Writer(width, height, bitdepth=8, greyscale=False)
    writer.write(output, rows)
