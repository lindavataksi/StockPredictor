import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import yfinance as yf

# Fetch more historical data
ticker = "AAPL"  # Example: Apple stock
data = yf.download(ticker, start="2010-01-01", end="2023-01-01")

# Reset index to get 'Date' as a column
data.reset_index(inplace=True)

# Selecting the relevant columns (for example, we'll use the 'Close' price)
data = data[['Date', 'Close']]

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Sorting the data by date
data = data.sort_values(by='Date')

# Prepare the data
X = np.array(data.index).reshape(-1, 1)  # Using index as feature
y = np.array(data['Close'])

# Build the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict future stock prices 
future_index = np.arange(len(X), len(X) + 365).reshape(-1, 1)
future_prices = model.predict(future_index)

# Storing variables for comparing current and future prices (future = after 365 days)
current_price = data['Close'].iloc[-1]
future_price = future_prices[364]  

if future_price > current_price:
    print("future price is greater")
else:
    print("current price is greater")

# Visualize historical and predicted future prices
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], label='Historical Prices', color='blue')
plt.plot(pd.date_range(start=data['Date'].iloc[-1], periods=365, freq='D'), future_prices, label='Predicted Future Prices', color='red')
plt.title('Historical and Predicted Future Stock Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()

# Scatter plot to visualize relationship between index and closing prices
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Linear Regression')
plt.title('Scatter Plot of Index vs Closing Price')
plt.xlabel('Index')
plt.ylabel('Closing Price')
plt.legend()
plt.grid(True)
plt.show()

# Residual plot to check the distribution of residuals
residuals = y - model.predict(X)
plt.figure(figsize=(10, 6))
plt.scatter(X, residuals, color='green')
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Residual Plot')
plt.xlabel('Index')
plt.ylabel('Residuals')
plt.grid(True)
plt.show()



