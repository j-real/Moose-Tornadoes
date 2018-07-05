import pandas as pd
import os
import quandl as quandl
import time

auth_tok = "xHAiXN62tDgD5svgDwkc"
quandl.ApiConfig.api_key = auth_tok
# mydata = quandl.get("WIKI/KO", start_date="2001-12-31", end_date="2005-12-31")

# print(mydata["Adj. Close"])

path = 'intraQuarter\\intraQuarter'

def StockPrices():
    df = pd.DataFrame()
    statspath = path+'\\_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    
    for each_dir in stock_list[1:]:
        try:
            ticker = each_dir.split("\\")[3]
            print(ticker)
            name = "WIKI/"+ticker.upper()
            data = quandl.get(name, trim_start = "2000-12-12",
            trim_end = "2014-12-30")
            data[ticker.upper()]=data["Adj. Close"]
            df = pd.concat ([df, data[ticker.upper()]], axis = 1)
        except:
            pass
    df.to_csv("stock.csv")

StockPrices()

