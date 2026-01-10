#!/usr/bin/env python3
import pandas as pd

def from_numpy(array):
     """
    function to create a dataframe
    Args:
        array: np.ndarray from which you should create the pd.DataFrame
    Returns: newly created pd.DataFrame
    """

    m = array.shapre[1]
    cols = list(string.ascii_uppercase[:m])
    return pd.DataFrame(array, columns=cols)
