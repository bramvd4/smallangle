# Small angle assignment
# Bram van Dijk

import click
import numpy as np
import pandas as pd
from numpy import pi


# defining a command group
@click.group()
def smallangle():
    """Defines a smallangle group: passes onto sine and tangent functions"""
    pass


# defining a command for taking the sine
@smallangle.command("sin")
@click.option(
    "-n",
    "--number",
    default=10,
    help="number of steps between 0 and 2 pi",
    show_default=True,
)
def sin(number):
    """Takes the sine for a given amount of numbers between 0 and 2 pi

    Args:
        number (integer): a number of values
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


# defining a command for taking the tangent
@smallangle.command("tan")
@click.option(
    "-n",
    "--number",
    default=10,
    help="number of steps between 0 and 2 pi",
    show_default=True,
)
def tan(number):
    """Takes the tangent for a given amount of numbers between 0 and 2 pi

    Args:
        number (integer): a number of values
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    smallangle()
