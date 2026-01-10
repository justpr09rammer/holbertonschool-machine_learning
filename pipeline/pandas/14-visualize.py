#!/usr/bin/env python3
"""
Visualize Coinbase data at daily intervals with proper cleaning and aggregation
"""

from_file = __import__('2-from_file').from_file

# Load the data
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# 1. Remove Weighted_Price
if 'Weighted_Price' in df.columns:
    df = df.drop(columns=['Weighted_Price'])

# 2. Rename Timestamp to Date
df = df.rename(columns={'Timestamp': 'Date'})

# 3. Convert timestamp to datetime
df['Date'] = pd.to_datetime(df['Date'], unit='s')

# 4. Set Date as index
df = df.set_index('Date')

# 5. Fill missing values
df['Close'] = df['Close'].fillna(method='ffill')
for col in ['Open', 'High', 'Low']:
    df[col] = df[col].fillna(df['Close'])
for col in ['Volume_(BTC)', 'Volume_(Currency)']:
    df[col] = df[col].fillna(0)

# 6. Filter from 2017 onward
df = df[df.index >= '2017-01-01']

# 7. Resample by day and aggregate
agg_dict = {
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
}
df_daily = df.resample('D').agg(agg_dict)

# 8. Plot (optional)
df_daily[['Close']].plot(title='Coinbase Daily Close Price (2017+)', figsize=(12, 6))
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.show()

# Return the transformed daily dataframe
df_daily
