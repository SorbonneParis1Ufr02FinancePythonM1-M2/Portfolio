from typing import Dict

import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from repository import get_config


def display_chart(data: pd.DataFrame) -> None:
    config: Dict = get_config()
    fig, ax = plt.subplots()
    ax.plot(
        data.index,
        data[config["chart"]["column"]],
        color=config["chart"]["color"],
        label=config["chart"]["label"],
    )
    ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
    plt.legend()
    plt.show()


def display_results(
    portfolio_return: np.float64,
    portfolio_variance: np.float64,
    portfolio_standard_dev: np.float64,
) -> None:
    config: Dict = get_config()
    print(f"{config["view"]["return"]}={portfolio_return}")
    print(f"{config["view"]["variance"]}={str(np.round(portfolio_variance, config["view"]["rounding"]) * 100)}%")
    print(f"{config["view"]["std"]}={str(np.round(portfolio_standard_dev, config["view"]["rounding"]) * 100)}%")
