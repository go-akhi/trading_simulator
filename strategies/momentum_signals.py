import pandas as pd 
from indicators import momentum
import matplotlib.pyplot as plt 

stock_data = pd.read_json('./market_data/apple_stock_data.json', orient='split', compression='infer')

stock_data.columns = stock_data.columns.map(lambda x : x[0] )

momentum_bucket = ["RSI", "MACD histogram heights", "ROC", "Stochastic Oscillator", "MFI"]

def is_column(df,col):
    if col not in df.columns():
        raise ValueError(f"The DataFrame does not contain the required column. The DataFrame does not have the {col} column.")

def rsi_signal(output_df, buy_limit = 30, sell_limit = 70 , stock_data):
    """
    Generates signal and strength based on the RSI value and the threshold set by the user

    Parameters:
        output_df(pd.DataFrame): The dataframe to which the signals and strengths will be 
            written to
        buy_limit(int): The oversold limit below which the function generates a buy signal
        sell_imit(int): The overbought limit over which the function makes a sell signal
        stock_data(pd.DataFrame): DataFrame with a RSI column

    Returns:
        output_df(pd.DataFrame): A DataFrame with appended signal and strength columns
    """
    # Ensure the data exists
    is_column(stock_data, "RSI")

    #Compare the RSI values and generate signals and calculate strengths
    for rsi in stock_data["RSI"]:
        if rsi < buy_limit:
            output_df["RSI signal"] = 1
            output_df["RSI signal strength"] = (buy_limit - rsi) * 100 / buy_limit
        elif rsi > sell_limit:
            output_df["RSI signal"] = -1
            output_df["RSI signal strength"] = (rsi - sell_limit) * 100 / (100 - sell_limit)
        else:
            output_df["RSI signal"] = 0
            
    return(output_df)

def macd_signal(output_df, stock_data):
