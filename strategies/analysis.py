import pandas as pd 
import indicators.momentum as momentum
import matplotlib.pyplot as plt 

stock_data = pd.read_json('./market_data/apple_stock_data.json', orient='split', compression='infer')

stock_data.columns = stock_data.columns.map(lambda x : x[0] )


stock_data['RSI'] = momentum.calculate_rsi(stock_data)
stock_data['MACD Histogram'] = momentum.calculate_macd(stock_data)

print(stock_data)

def print_graph(df, cols):

    lines = len(cols) - 2
    fig, axs = plt.subplots(lines, 1, sharex=True)

    for i,col in enumerate(cols):
        axs[i].plot(df['Date'], df[col], label=col)
        axs[i].set_title(col)
    
    axs[lines + 1].bar(df['Date'], df['MACD Histogram'], label='MACD Histogram')
    axs[lines + 1].set_title('MACD Histogram')

    plt.show()

    

print_graph(stock_data, ["Adj Close", "RSI", "MACD Histogram"])
