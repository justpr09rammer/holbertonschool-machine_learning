#!/usr/bin/env python3
"""
Function that flips a DataFrame:
- sorts in reverse chronological order
- transposes the sorted DataFrame
"""


def flip_switch(df):
    """
    Args:
        df (pd.DataFrame): input dataframe
    Returns:
        pd.DataFrame: transformed dataframe
    """
    # 1. Sort in reverse chronological order by index
    df_sorted = df.sort_index(ascending=False)

    # 2. Transpose the DataFrame
    df_transposed = df_sorted.T

    return df_transposed
