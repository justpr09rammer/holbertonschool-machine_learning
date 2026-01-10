#!/usr/bin/env python3
"""
Function that slices a DataFrame:
- keeps only High, Low, Close, Volume_BTC
- selects every 60th row
"""


def slice(df):
    """
    Args:
        df (pd.DataFrame): input dataframe
    Returns:
        pd.DataFrame: sliced dataframe
    """
    # 1. Select required columns
    df_selected = df[['High', 'Low', 'Close', 'Volume_(BTC)']]
    # 2. Select every 60th row
    df_sliced = df_selected.iloc[::60]
    return df_sliced
