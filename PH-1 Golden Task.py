import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Define the ticker symbol for the stock
ticker_symbol = 'AAPL'  # Apple Inc. in this example

# Define the start and end dates for the historical data
start_date = '2020-01-01'
end_date = '2022-01-01'

# Fetch the historical stock price data from Yahoo Finance
stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Display the first few rows of the data
print(stock_data.head())

# Plot the closing price of the stock over time
plt.figure(figsize=(10, 6))
stock_data['Close'].plot()
plt.title('Historical Stock Prices for {}'.format(ticker_symbol))
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.grid(True)
plt.show()
