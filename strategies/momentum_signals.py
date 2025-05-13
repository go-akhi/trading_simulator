import pandas as pd 
from indicators import momentum
import matplotlib.pyplot as plt 

stock_data = pd.read_json('./market_data/apple_stock_data.json', orient='split', compression='infer')

stock_data.columns = stock_data.columns.map(lambda x : x[0] )

momentum_bucket = ["RSI", "MACD histogram heights", "ROC", "Stochastic Oscillator", "MFI"]

def calculate_rsi_strength(output_df, lower_limit = 30, upper_limit = 80 , stock_data):
    """
    Generates signal and strength based on the RSI value and the threshold set by the user
    """
