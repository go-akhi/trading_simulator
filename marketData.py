import yfinance as yf
import pandas as pd
import json
from datetime import datetime, timedelta

def fetch_and_save_stock_data(stock_symbol, filename="stock_data.json"):
    try:
        # Calculate the start and end dates (6 months back from today)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=180)

        # Download the stock data using yfinance
        stock_data = yf.download(stock_symbol, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'), auto_adjust=False)
        
        if stock_data.empty:
            print(f"No data found for {stock_symbol}. Please check the stock symbol.")
            return

        # Reset the index and convert the DataFrame to JSON-friendly format
        stock_data.reset_index(inplace=True)
        stock_data = stock_data.astype(str)  # Convert all columns to string to avoid issues with JSON serialization
        # Save the data to a JSON file
        stock_data.to_json('apple_stock_data.json', orient='split', compression='infer')

        print(f"Stock data for {stock_symbol} saved to {filename}.")


    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
fetch_and_save_stock_data("AAPL", "apple_stock_data.json")
