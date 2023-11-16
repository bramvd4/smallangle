import click
import numpy as np
import pandas as pd
from numpy import pi


@click.group()
def smallangle():
    pass


@smallangle.command("sin")
@click.option(
    "-n",
    "--number",
    default=10,
    help="number of steps between 0 and 2 pi",
    show_default=True,
)
def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return


@smallangle.command("tan")
@click.option(
    "-n",
    "--number",
    default=10,
    help="number of steps between 0 and 2 pi",
    show_default=True,
)
def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    smallangle()
