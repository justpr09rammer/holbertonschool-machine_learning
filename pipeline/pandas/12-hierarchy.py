#!/usr/bin/env python3
"""
Module that creates a hierarchical (MultiIndex) DataFrame from two sources
"""

import pandas as pd
index = __import__('10-index').index

def hierarchy(df1, df2):
    """
    Creates a MultiIndex DataFrame with Timestamp as first level and
    source (bitstamp/coinbase) as second level.

    Steps:
    - Index both dataframes on 'Timestamp'
    - Select rows from both dataframes between timestamps 1417411980 and 1417417980
    - Concatenate with keys
    - Ensure Timestamp is the first level of the MultiIndex
    - Sort chronologically

    Args:
        df1 (pd.DataFrame): Coinbase DataFrame
        df2 (pd.DataFrame): Bitstamp DataFrame

    Returns:
        pd.DataFrame: Hierarchical (MultiIndex) concatenated DataFrame
    """
    # Set Timestamp as index
    df1 = index(df1)
    df2 = index(df2)

    # Select the timestamp range
    start_ts = 1417411980
    end_ts = 1417417980
    df1_sel = df1[(df1.index >= start_ts) & (df1.index <= end_ts)]
    df2_sel = df2[(df2.index >= start_ts) & (df2.index <= end_ts)]

    # Concatenate with keys
    df_concat = pd.concat([df2_sel, df1_sel], keys=['bitstamp', 'coinbase'])

    # Swap levels to make Timestamp the first level
    df_concat = df_concat.swaplevel(0, 1)

    # Sort by Timestamp to ensure chronological order
    df_concat = df_concat.sort_index(level=0)

    return df_concat

