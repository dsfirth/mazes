from random import choice
import click

from src.grid import Grid

from src.binary_tree import binary_tree
from src.algorithm.prims import prims
from src.sidewinder import sidewinder


@click.group()
def main():
    pass


@main.command()
@click.option('--size', '-s', nargs=2, default=(4, 4))
@click.option('--algorithm', '--alg', '-a', type=click.Choice(['binary_tree', 'prims', 'sidewinder'], case_sensitive=False), default='sidewinder')
def grid(size, algorithm) -> None:
    rows, columns = size
    grid = Grid(rows, columns)

    algorithm_map = {
        'binary_tree': binary_tree,
        'prims': prims,
        'sidewinder': sidewinder
    }

    algorithm_map.get(algorithm)(grid)
    print(grid)


if __name__ == '__main__':
    main()
