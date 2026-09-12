import click

from src.grid import Grid


def text_encoder(grid: Grid, output: click.File) -> None:
    output.write(str(grid).encode('utf-8'))
