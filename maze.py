import click
import os


# algorithms
from src.algorithm.binary_tree import binary_tree
from src.algorithm.prims import prims
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
@click.option('--algorithm', '--alg', '-a', type=click.Choice(['binary_tree', 'prims', 'sidewinder'], case_sensitive=False), default='sidewinder',
              help='Maze generation algorithm (default: sidewinder).')
@click.option('--output', '--out', '-o', type=click.File('wb'), default='-')
def grid(size, algorithm, output: click.File) -> None:
    rows, columns = size
    grid = Grid(rows, columns)

    algorithm_map = {
        'binary_tree': binary_tree,
        'prims': prims,
        'sidewinder': sidewinder
    }

    encoder_map = {
        'png': png_encoder,
        'text': text_encoder
    }

    # determine the encoder -- based on the `--output`` value
    encoder = 'text'
    if output.name != '<stdout>':
        # use `--output` filename extension
        _, ext = os.path.splitext(output.name)
        match ext.lower():
            case '.png':
                encoder = 'png'
            case _:
                raise click.BadParameter(
                    "Output file '% s' format not supported (expected: .png)" % output.name,
                    param_hint="'--output'"
                )

        # ensure the output doesn't exist
        # if os.path.exists(output.name):
        #     raise click.BadParameter(
        #         "File '% s' already exists!" % output.name,
        #         param_hint="'--output'"
        #     )

    algorithm_map.get(algorithm.lower())(grid)
    encoder_map.get(encoder.lower())(grid, output)


if __name__ == '__main__':
    main()