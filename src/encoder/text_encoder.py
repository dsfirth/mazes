import click

from src.grid import Direction, Grid


def text_encoder(grid: Grid, output: click.File) -> None:
    out = '+'
    for column in range(grid.columns):
        cell = grid[0, column]
        boundary = '   ' if grid.passage_open(cell, Direction.NORTH) else '---'
        out += boundary + '+'
    out += '\n'

    for row in grid.each_row():
        top = ' ' if grid.passage_open(row[0], Direction.WEST) else '|'
        bottom = '+'

        for cell in row:
            body = '   '  # that's THREE (3) spaces!
            east_boundary = ' ' if grid.passage_open(cell, Direction.EAST) else '|'
            top += body + east_boundary

            # three spaes below, too
            south_boundary = '   ' if grid.passage_open(cell, Direction.SOUTH) else '---'
            corner = '+'
            bottom += south_boundary+corner

        out += top + '\n'
        out += bottom + '\n'

    output.write(out.encode('utf-8'))
