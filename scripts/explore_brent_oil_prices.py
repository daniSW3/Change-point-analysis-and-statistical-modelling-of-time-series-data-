import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stationarity import adfuller

# Load the data
df = pd.read_csv('BrentOilPrices.csv')

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Basic exploration
print("Dataset Info:\n", df.info())
print("\nFirst few rows:\n", df.head())

# Plot price series
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Price'], label='Brent Oil Price')
plt.title('Brent Oil Prices (May-Jun 1987)')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.show()

# Calculate log returns
df['Log_Return'] = np.log(df['Price'] / df['Price'].shift(1))

# Plot log returns
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Log_Return'], label='Log Returns', color='orange')
plt.title('Brent Oil Log Returns (May-Jun 1987)')
plt.xlabel('Date')
plt.ylabel('Log Return')
plt.legend()
plt.show()

# Test stationarity (ADF test)
result = adfuller(df['Price'].dropna())
print("\nADF Test for Prices - Statistic:", result[0], "p-value:", result[1])
result_returns = adfuller(df['Log_Return'].dropna())
print("ADF Test for Log Returns - Statistic:", result_returns[0], "p-value:", result_returns[1])