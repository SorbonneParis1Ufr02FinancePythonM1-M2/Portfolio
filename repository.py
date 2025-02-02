import os
from typing import Dict

import numpy as np
import yfinance as yf

from constants import CONFIG_FILE
from helpers_serialize import get_serialized_data


def get_config() -> Dict:
    path: str = os.path.join(os.getcwd(), CONFIG_FILE)
    return get_serialized_data(path)


def get_weights() -> np.array:
    config: Dict = get_config()
    return np.array(list(config["portfolio"].values()))


def get_data():
    config: Dict = get_config()
    tickers = list(config["portfolio"].keys())
    data = yf.download(
        tickers,
        start=config["initialisation"]["begin_date"],
        end=config["initialisation"]["end_date"],
    )
    return data[config["initialisation"]["field_to_keep"]]
