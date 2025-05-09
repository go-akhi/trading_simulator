import yfinance as yf
import pandas as pd

def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Example usage
ticker = "AAPL"  # Replace with your desired stock ticker
data = yf.download(ticker, start="2023-01-01", end="2023-12-31")
data['RSI'] = calculate_rsi(data)
print(data.head())
