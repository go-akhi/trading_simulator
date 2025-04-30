import pandas as pd 
import indicator

stock_data = pd.read_json('./market_data/apple_stock_data.json', orient='split', compression='infer')

stock_data.columns = stock_data.columns.map(lambda x : x[0] )


print(indicator.calculate_rsi(stock_data,"Close"))
