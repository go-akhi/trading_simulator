import pandas as pd 

stock_data = pd.read_json('./market_data/apple_stock_data.json', orient='split', compression='infer')

print(stock_data)
