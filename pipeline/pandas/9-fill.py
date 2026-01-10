#!/usr/bin/env python3
"""
Module that fills missing values in a DataFrame
"""


def fill(df):
    """
    Fills missing values in a DataFrame according to specific rules:
      - Removes 'Weighted_Price' column if it exists
      - Fills missing 'Close' values with the previous row's 'Close'
      - Fills missing 'Open', 'High', 'Low' with the same row's 'Close'
      - Sets missing 'Volume_(BTC)' and 'Volume_(Currency)' to 0

    Args:
        df (pd.DataFrame): The input dataframe

    Returns:
        pd.DataFrame: The modified dataframe
    """
    # Remove 'Weighted_Price' column if present
    if 'Weighted_Price' in df.columns:
        df = df.drop(columns=['Weighted_Price'])

    # Fill missing 'Close' values with previous row
    df['Close'] = df['Close'].fillna(method='ffill')

    # Fill missing 'Open', 'High', 'Low' with the corresponding 'Close' value
    for col in ['Open', 'High', 'Low']:
        df[col] = df[col].fillna(df['Close'])

    # Fill missing volumes with 0
    for col in ['Volume_(BTC)', 'Volume_(Currency)']:
        df[col] = df[col].fillna(0)

    return df
