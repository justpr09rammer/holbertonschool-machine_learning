#!/usr/bin/env python3
"""
Module that sets the Timestamp column as index of a DataFrame
"""


def index(df):
    """
    Sets the 'Timestamp' column as the index of the DataFrame.

    Args:
        df (pd.DataFrame): The input dataframe

    Returns:
        pd.DataFrame: The modified dataframe with 'Timestamp' as index
    """
    df = df.set_index('Timestamp')
    return df
