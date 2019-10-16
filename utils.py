from typing import List


def load_data(path: str) -> List:
    # Get puzzle data
    with open(path) as f:
        content = f.readlines()
    return content
