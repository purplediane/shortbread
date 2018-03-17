#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `shortbread` package."""

import pytest

from click.testing import CliRunner

from shortbread import shortbread
from shortbread import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface_simple():
    """Test the CLI in the simplest version."""
    runner = CliRunner()

    result = runner.invoke(cli.main, ['4'])
    assert result.exit_code == 0
    assert 'Shortbread Cookies - makes approx. 4 doz.' in result.output
    assert '4 cups flour' in result.output
    assert '1.0 cups sugar' in result.output
    assert '2.0 cups salted butter' in result.output
    assert '1.0 teaspoons vanilla (optional)' in result.output
    assert 'Bake cookies at 350 degrees for 10-12 minutes' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    # assert 'Usage: shortbread [OPTIONS] COUNT' in help_result.output
    # Can't use that ^^^ because it says Usage: main here.
    assert '--help      Show this message and exit.' in help_result.output


def test_command_line_interface_long():
    """Test the CLI in the simplest version."""
    runner = CliRunner()

    result = runner.invoke(cli.main, ['4', '-l'])
    assert result.exit_code == 0
    assert 'Shortbread Cookies - makes approx. 4 doz.' in result.output
    assert '- Preheat oven to 350 degrees F.' in result.output
    assert '- Bake 10 to 12 minutes at 350 degrees' in result.output


def test_command_line_interface_chocolate():
    """Test the CLI in the simplest version."""
    runner = CliRunner()

    result = runner.invoke(cli.main, ['4', '-c'])
    assert ('Chocolate Chip Shortbread Cookies - makes approx. 4 doz.'
            in result.output)
    assert result.exit_code == 0


def test_command_line_interface_chocolate_long():
    """Test the CLI in the simplest version."""
    runner = CliRunner()

    result = runner.invoke(cli.main, ['4', '-l', '-c'])
    assert ('Chocolate Chip Shortbread Cookies - makes approx. 4 doz.'
            in result.output)
    assert result.exit_code == 0
    assert '- Sift together baking powder and flour.' in result.output
    assert '- Stir in the chocolate chips.' in result.output
    assert '- Flatten cookie balls slightly.' in result.output
    assert ('- Bake 15 to 20 minutes at 350 degrees until golden brown.'
            in result.output)


def test_shortbread(capsys):
    """Test the output from shortbread"""
    # shortbread() only prints; returns nothing
    assert shortbread.shortbread(4) is None
    # Capture the result of the arepas.ingredients() function call.
    captured = capsys.readouterr()
    # If we check captured, we can see that the ingredients have been printed.
    assert 'Shortbread Cookies - makes approx. 4 doz.' in captured.out
    assert "4 cups flour" in captured.out
    assert "1.0 cups sugar" in captured.out
    assert "2.0 cups salted butter" in captured.out
    assert "Bake cookies at 350 degrees for 10-12 minutes" in captured.out
