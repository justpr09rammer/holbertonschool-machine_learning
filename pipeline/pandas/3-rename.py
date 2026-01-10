#!/usr/bin/env python3
"""
Function that renames the Timestamp column to Datetime,
converts it to datetime objects, and keeps only Datetime and Close
"""

import pandas as pd


def rename(df):
    """
    Args:
        df (pd.DataFrame): input dataframe containing 'Timestamp' column
    Returns:
        pd.DataFrame: modified dataframe with 'Datetime' and 'Close' columns
    """
    # 1. Rename column
    df = df.rename(columns={'Timestamp': 'Datetime'})

    # 2. Convert to datetime (timestamps in seconds)
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')

    # 3. Keep only Datetime and Close
    df = df[['Datetime', 'Close']]

    return df
