#!/usr/bin/env python3
"""
Module that concatenates two DataFrames (bitstamp on top of coinbase)
"""

import pandas as pd
index = __import__('10-index').index

def concat(df1, df2):
    """
    Concatenates two DataFrames with keys and limited timestamp selection.

    Steps:
    - Index both dataframes on 'Timestamp'
    - Select rows from df2 with Timestamp <= 1417411920
    - Concatenate df2 on top of df1
    - Add keys to differentiate rows

    Args:
        df1 (pd.DataFrame): Coinbase DataFrame
        df2 (pd.DataFrame): Bitstamp DataFrame

    Returns:
        pd.DataFrame: Concatenated DataFrame with keys
    """
    # Set Timestamp as index for both
    df1 = index(df1)
    df2 = index(df2)

    # Select df2 rows up to timestamp 1417411920
    df2_sel = df2[df2.index <= 1417411920]

    # Concatenate with keys
    df_concat = pd.concat([df2_sel, df1], keys=['bitstamp', 'coinbase'])

    return df_concat

