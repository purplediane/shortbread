# -*- coding: utf-8 -*-

"""Main module."""


def shortbread(unit):
    """Prints ingredients for making `unit` dozen shortbread cookies."""
    print('{} cups flour'.format(unit))
    print('{} cups sugar'.format(.25 * unit))
    print('{} cups butter'.format(.5 * unit))
    print('Bake at 350 degrees for 10-12 minutes')
