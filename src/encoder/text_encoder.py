import click

from src.grid import Grid


def text_encoder(grid: Grid, output: click.File) -> None:
    out = '+' + '---+' * grid.columns + '\n'

    for row in grid.each_row():
        top = '|'
        bottom = '+'

        for cell in row:
            body = '   '  # that's THREE (3) spaces!
            east_boundary = ' ' if cell.linked(cell.east) else '|'
            top += body + east_boundary

            # three spaes below, too
            south_boundary = '   ' if cell.linked(cell.south) else '---'
            corner = '+'
            bottom += south_boundary+corner

        out += top + '\n'
        out += bottom + '\n'

    output.write(out.encode('utf-8'))
