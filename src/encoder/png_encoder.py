import click
import png

from src.grid import Grid

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
    red_pixel = [255, 0, 0]
    for row in grid.each_row():
        for cell in row:
            # check east neighbour; if linked, ...
            if cell.linked(cell.east):
                # remove east wall
                y, x = cell_size * cell.row + 1, 3 * cell_size * (cell.column + 1)
                for yOffset in range(cell_size - 1):
                    rows[y + yOffset][x:x + 3] = white_pixel

            # check south neighbour; if linked, ...
            if cell.linked(cell.south):
                # remove south wall
                y, x = cell_size * (cell.row + 1), 3 * cell_size * cell.column + 3
                rows[y][x:x + (3 * (cell_size - 1))] = white_pixel * (cell_size - 1)

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
