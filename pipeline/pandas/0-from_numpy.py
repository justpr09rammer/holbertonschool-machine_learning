#!/usr/bin/env python3
"""
Defines function that creates a Pandas DataFrame from a Numpy ndarray
"""
import pandas as pd


def from_numpy(array):
    """
    Creates a pandas DataFrame from a numpy array
    Args:
        array (np.ndarray): input array
    Returns:
        pd.DataFrame: dataframe with columns named A, B, C, ...
    """
    m = array.shape[1]  # number of columns

    # generate column names manually: A=65, B=66, ...
    cols = [chr(65 + i) for i in range(m)]

    return pd.DataFrame(array, columns=cols)

