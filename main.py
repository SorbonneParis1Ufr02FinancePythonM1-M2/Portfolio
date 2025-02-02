import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from model import (
    portfolio_return,
    portfolio_variance,
    portfolio_standard_dev,
    portfolio_cumulative_returns,
)
from repository import get_data, get_weights


def main():
    # https://campus.datacamp.com/courses/introduction-to-portfolio-analysis-in-python/introduction-to-portfolio-analysis?ex=6

    # 1. Get data
    data = get_data()
    weights = get_weights()

    # --------------------------------------------------------------------------------
    # 2. Process the data
    daily_cum_ret = portfolio_cumulative_returns(weights, data)
    port_return = portfolio_return(weights, data)
    port_variance = portfolio_variance(weights, data)
    port_standard_dev = portfolio_standard_dev(weights, data)

    # --------------------------------------------------------------------------------
    # 3. Display the results

    # Print the portfolio return
    print(port_return)

    # Plot the portfolio cumulative returns only
    fig, ax = plt.subplots()
    ax.plot(
        daily_cum_ret.index, daily_cum_ret["Portfolio"], color="purple", label="portfolio"
    )
    ax.xaxis.set_major_locator(matplotlib.dates.YearLocator())
    plt.legend()
    plt.show()

    # Print the result
    print(str(np.round(port_variance, 4) * 100) + "%")

    # Print the results
    print(str(np.round(port_standard_dev, 4) * 100) + "%")


if __name__ == "__main__":
    main()
