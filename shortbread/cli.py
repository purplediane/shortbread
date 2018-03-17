# -*- coding: utf-8 -*-

"""Console script for shortbread."""
import sys
import click
from shortbread.shortbread import shortbread


@click.command()
@click.argument('count', type=int)
@click.option('--long', '-l', is_flag=True)
@click.option('--choc', '-c', is_flag=True)
def main(count, long, choc):
    """Console script for shortbread."""
    shortbread(count, long, choc)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
