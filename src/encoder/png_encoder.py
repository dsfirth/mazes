import click
import png

from src.grid import Grid

cell_size = 10

def png_encoder(grid: Grid, output: click.File) -> None:
    white_pixel = [255, 255, 255]
    width, height = cell_size * grid.columns + 1, cell_size * grid.rows + 1

    # initialize an empty canvas
    rows = []
    for y in range(height):
        row = []
        for x in range(width):
            # Generate pixel values based on position
            row.extend(white_pixel)
        rows.append(row)

    # idea: use modulo (%) and int(x / cell_size) to get grid cell

    # # Create from array
    # image_2d = [[255, 0, 0],    # Red pixel
    #             [0, 255, 0],    # Green pixel
    #             [0, 0, 255]]    # Blue pixel
    # for row in grid.each_row():
    #     # initialize pixel rows for the grid row
    #     pixel_rows = [[]] * cell_size

    #     for cell in row:
    #         for y in range(cell_size):
    #             for x in range(cell_size):


    writer = png.Writer(width, height, bitdepth=8, greyscale=False)
    writer.write(output, rows)
