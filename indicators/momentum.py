import pandas as pd

#MOMENTUM INDICATORS
def calculate_rsi(df, period = 14):
    """Calculates the relative strength index that indicates whether an asset is overbought or oversold.
    An RSI of more than 70 means the asset is overbought, indicates a potential reversal of or a pullback in prices.
    An RSI of less than 30 suggest the asset is oversold, signalling a potential upward reversal as the asset maybe undervalued.

    Divergence: 
    Bullish Divergence: a rising RSI and a falling stock price indicates a potential upward reversal
    Bearish Divergence: a falling RSI with rising prices suggests a potential downward reversal

    args
    df: stock price dataframe
    column_name: the column over which you want to calculate the RSI (usually the closing prices)
    period: the window (days) over which you want to calculate the RSI, defaults to 14"""
    
    #check if the data exists
    if df["Adj Close"].empty:
        return([f"No data"])
    else:
        delta = df["Adj Close"].diff()

    #separate the gains and losses
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)

    #calculate rolling average
    avg_gain = gains.rolling(window = period).mean()
    avg_losses = losses.rolling(window = period).mean()

    #calculate relative strength and the relative strength index
    rs = avg_gain/avg_losses
    rsi = 100 - (100 / (1 + rs))

    return(rsi)

def calculate_macd(df):
    #calculate exponnential moving averages
    ema_12 = df['Adj Close'].ewm(span=12, adjust=False).mean()
    ema_26 = df['Adj Close'].ewm(span=26, adjust=False).mean()

    #calculate macd
    macd = ema_12 - ema_26
    #calculate the signal line
    signal = macd.ewm(span=9, adjust=False).mean()

    #macd histogram data
    delta = macd - signal

    return(delta)