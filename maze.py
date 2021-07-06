from random import choice
import click

from src.grid import Grid

from src.binary_tree import binary_tree
from src.sidewinder import sidewinder


@click.group()
def main():
    pass


@main.command()
@click.option('--size', '-s', nargs=2, default=(4, 4))
@click.option('--algorithm', '--alg', '-a', type=click.Choice(['binary_tree', 'sidewinder'], case_sensitive=False), default='sidewinder')
def grid(size, algorithm) -> None:
    rows, columns = size
    grid = Grid(rows, columns)

    alg = {
        'binary_tree': binary_tree,
        'sidewinder': sidewinder
    }

    alg.get(algorithm)(grid)
    print(grid)


if __name__ == '__main__':
    main()
