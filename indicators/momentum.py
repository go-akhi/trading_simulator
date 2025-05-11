import pandas as pd

def is_column(df, col):
    if col not in df.columns:
        raise ValueError(f"The data you provided does not have the column name you provided. No column named {col} in DataFrame")

#MOMENTUM INDICATORS
def calculate_rsi(df, col = "Adj Close", period = 14):
    """
    Calculates the relative strength index that indicates whether an asset is overbought or oversold.
    An RSI of more than 70 means the asset is overbought, indicates a potential reversal of or a pullback in prices.
    An RSI of less than 30 suggest the asset is oversold, signalling a potential upward reversal as the asset maybe undervalued.

    Divergence: 
    Bullish Divergence: a rising RSI and a falling stock price indicates a potential upward reversal
    Bearish Divergence: a falling RSI with rising prices suggests a potential downward reversal

    This function returns the RSI of default 14-periods, a second numeric argument can be given to
    obtain the RSI of a different period

    Parameters:
        df (pd.DataFrame): DataFrame with a stock data 
        col (str): Column name of the values to be used to calculate RSI (default = "Adj Close").
        period (int): Number of periods for calculating RSI.(default = 14)

    Returns:
        pd.Series: RSI values.
    """
    
    # Ensure if column exists
    is_column(df, col)

    # Calculate the price changes for consecutive days
    delta = df[col].diff()

    # Separate the gains and losses
    gains = delta.where(delta > 0, 0)
    losses = -delta.where(delta < 0, 0)

    # Calculate rolling average
    avg_gain = gains.rolling(window = period).mean()
    avg_losses = losses.rolling(window = period).mean()

    # Calculate relative strength and the relative strength index
    rs = avg_gain/avg_losses
    rsi = 100 - (100 / (1 + rs))

    return(rsi)

def calculate_macd(df, col = "Adj Close", fast_period = 12, slow_period = 26, signal_period = 9):
    """Captures momentum shifts and trend strength

    MACD is the difference of the 12-period EMA and the 26-period EMA
    Signal line is the 9-period EMA

    MACD is a hybrid indicator that captures trends and momentum faster than EMA

    When the MACD crosses above the signal line, it suggests a bullish trend 
    When the MACD crosses below the signal line, it suggests a bearish trend

    This function returns the difference between the MACD and the signal line
    when delta changes from negative to positive, suggests a bullish trend
    when delta changes from positive to negative, suggests a bearish trend

    Parameters:
        df (pd.DataFrame): DataFrame with a 'Close' column.
        col (str) : Column name of the value to be used for calculating MACD (default = "Adj Close").
        fast_period (int) : Number of periods to calculate the fast (short) EMA (default = 12).
        slow_period (int) : Number of period to calculate the slow (long) EMA d(efault = 26).
        signal_period (int) : Number of periods to calculate the signal line of the MACD oscillator (default = 9).
        
    Returns:
        pd.Series: MACD histogram height values.
    """
    # Ensure if column exists
    is_column(df, col)

    # Calculate exponential moving averages
    ema_fast = df[col].ewm(span=fast_period, adjust=False).mean()
    ema_slow = df[col].ewm(span=slow_period, adjust=False).mean()

    # Calculate MACD
    macd = ema_fast - ema_slow
    # Calculate the signal line
    signal = macd.ewm(span=signal_period, adjust=False).mean()

    #MACD histogram data
    delta = macd - signal

    return(delta)

def calculate_roc(df, col = "Adj Close", period = 15):
    """
    Rate of Change
    Positive ROC: Indicates upward momentum (prices rising).
    Negative ROC: Indicates downward momentum (prices falling).
    Using a 15-day period here for an intermediate analysis

    Parameters:
        df (pd.DataFrame): Stock market data.
        col (str): Column name of the value to calculate ROC of(default = "Adj Close").
        period (int): Time period over change ROC is to be calculated (default = 15)
    
    Returns:
        pd.Series: ROC values
    """
    # Ensure if column exists
    is_column(df, col)

    # Calculate ROC
    roc = (df[col] - df[col].shift(period)) * 100 / df[col].shift(period) 

    return(roc)

def calculate_stochastic_oscillator(df, period = 14):
    """
    - Values above 80 suggest overbought conditions
    - Below 20 indicates oversold.

    Parameters:
        df (pd.DataFrame): Stock market data with "High", "Low", "Adj Close" columns
        period (int): The period over which the oscillator is to be calculated
    
    Return:
        pd.Series: Stochastic Oscillator signal values
    """
    # Ensure columns exist in the dataset 
    is_column(df, "High")
    is_column(df, "Low")
    is_column(df, "Adj Close")

    # Calculate rolling highest high and lowest low
    rolling_high = df["High"].rolling(window = period).max()
    rolling_low = df["Low"].rolling(window = period).min()

    # Calculate the stochastic oscillator line %K
    k = (df["Adj Close"] - rolling_low) * 100 / (rolling_high - rolling_low)

    # Calculate the signal line, %D which is the 3-day simple moving average
    d = k.rolling(window = 3).mean()

    return(d)

def calculate_money_flow_index(df, period = 14):
    """
    - Above 80: Overbought (watch for reversals).
    - Below 20: Oversold (potential buying opportunity).

    Parameters:
        df (pd.DataFrame): Stock market data with "High", "Low", "Adj Close" and "Volume" columns
        period (int): Lookback window for calculating the MFI(default = 14)

    Returns:
        pd.Series: MFI values
    """
    # Ensure columns exist in the dataset 
    is_column(df, "High")
    is_column(df, "Low")
    is_column(df, "Adj Close")
    is_column(df, "Volume")

    # Calculate typical value
    typical_price = (df["High"] + df["Low"] + df["Adj Close"])/3

    # Calculate the raw money flow and separate positive and negative money flows
    money_flow = typical_price * df["Volume"]

    positive_mf = money_flow.where(money_flow > money_flow.shift(1), 0)
    negative_mf = money_flow.where(money_flow < money_flow.shift(1), 0)

    # Calculate Money Flow Index
    money_flow_ratio = positive_mf.rolling(window = period).sum() / negative_mf.rolling(window = period).sum()
    mfi = 100 - (100 / (1 + money_flow_ratio))

    return(mfi)


