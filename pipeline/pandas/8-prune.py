#!/usr/bin/env python3
"""
Function that removes rows where Close is NaN
"""


def prune(df):
    """
    Args:
        df (pd.DataFrame): input dataframe
    Returns:
        pd.DataFrame: dataframe with rows containing NaN in 'Close' removed
    """
    # Remove rows where 'Close' is NaN
    df_clean = df.dropna(subset=['Close'])

    return df_clean
