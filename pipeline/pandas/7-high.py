#!/usr/bin/env python3
"""
Function that sorts a DataFrame by the High price in descending order
"""


def high(df):
    """
    Args:
        df (pd.DataFrame): input dataframe
    Returns:
        pd.DataFrame: dataframe sorted by High in descending order
    """
    # Sort by 'High' in descending order
    df_sorted = df.sort_values(by='High', ascending=False)

    return df_sorted
