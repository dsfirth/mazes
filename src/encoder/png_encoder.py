import click
import png

from src.grid import Grid

# define some constants
cell_size = 10
margin = 5


def png_encoder(grid: Grid, output: click.File) -> None:
    black_pixel = [0, 0, 0]
    white_pixel = [255, 255, 255]
    width, height = cell_size * grid.columns + 1, cell_size * grid.rows + 1

    # initialize an empty canvas
    rows = []
    for y in range(height):
        row = []
        for x in range(width):
            # Generate pixel values based on position
            if y % cell_size == 0 or x % cell_size == 0:
                # idea: use modulo (%) and int(x / cell_size) to get grid cell
                row.extend(black_pixel)
            else:
                row.extend(white_pixel)

        rows.append(row)

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
