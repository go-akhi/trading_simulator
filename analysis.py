import pandas as pd 

stock_data = pd.read_json('apple_stock_data.json', orient='split', compression='infer')

print(stock_data)
