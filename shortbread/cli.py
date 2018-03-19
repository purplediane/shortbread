# -*- coding: utf-8 -*-

"""Console script for shortbread."""
import sys
import click
from shortbread.shortbread import shortbread


@click.command()
@click.argument('count', type=int, default=1)
@click.option('--long', '-l', is_flag=True,
              help='Print the longer version with directions.')
@click.option('--choc', '-c', is_flag=True,
              help='Print the Chocolate Chip Shortbread version.')
def main(count, long, choc):
    """Script to print shortbread recipe for COUNT dozen cookies.
       If COUNT is omitted, then a recipe for 1 dozen is printed.
    """
    shortbread(count, long, choc)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
