import click

# algorithms
from src.algorithm.binary_tree import binary_tree
from src.algorithm.sidewinder import sidewinder

# encoders
from src.encoder.png_encoder import png_encoder
from src.encoder.text_encoder import text_encoder

from src.grid import Grid


@click.group()
def main():
    pass


@main.command()
@click.option('--size', '-s', nargs=2, default=(4, 4), help='Number of rows columns in the grid (default: 4 4)')
@click.option('--algorithm', '--alg', '-a', type=click.Choice(['binary_tree', 'sidewinder'], case_sensitive=False), default='sidewinder',
              help='Maze generation algorithm (default: sidewinder).')
@click.option('--output', '--out', '-o', type=click.File('wb'), default='-')
def grid(size, algorithm, output: click.File) -> None:
    rows, columns = size
    grid = Grid(rows, columns)

    algorithm_map = {
        'binary_tree': binary_tree,
        'sidewinder': sidewinder
    }

    encoder_map = {
        'png': png_encoder,
        'text': text_encoder
    }

    encoder = 'png'

    algorithm_map.get(algorithm.lower())(grid)
    encoder_map.get(encoder.lower())(grid, output)


if __name__ == '__main__':
    main()
