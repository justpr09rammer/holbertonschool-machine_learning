#!/usr/bin/env python3
"""
Function that selects the last 10 rows of High and Close columns
and returns them as a numpy.ndarray
"""

import pandas as pd


def array(df):
    """
    Args:
        df (pd.DataFrame): input dataframe with 'High' and 'Close' columns
    Returns:
        np.ndarray: last 10 rows of High and Close columns
    """
    # 1. Select last 10 rows of High and Close
    last_rows = df[['High', 'Close']].tail(10)

    # 2. Convert to NumPy array
    arr = last_rows.to_numpy()

    return arr

