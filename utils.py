from typing import List
import pandas as pd


def load_data(path: str) -> List:
    # Get puzzle data
    return pd.read_csv(path, header=None, sep=" ")[0].values.tolist()
