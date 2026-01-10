#!/usr/bin/env python3
"""
Module that analyzes a DataFrame and returns descriptive statistics
"""


def analyze(df):
    """
    Computes descriptive statistics for all columns except 'Timestamp'.

    Args:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: Descriptive statistics of numeric columns
    """
    # Exclude Timestamp column if it exists
    df_numeric = df.drop(columns=['Timestamp'], errors='ignore')

    # Compute descriptive statistics
    stats = df_numeric.describe()

    return stats
