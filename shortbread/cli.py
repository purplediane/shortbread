# -*- coding: utf-8 -*-

"""Console script for shortbread."""
import sys
import click
from shortbread.shortbread import shortbread


@click.command()
@click.argument('count', type=int)
def main(count):
    """Console script for shortbread."""
    shortbread(count)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
