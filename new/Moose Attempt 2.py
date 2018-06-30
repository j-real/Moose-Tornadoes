import pandas as pd
import os
import time
from datetime import datetime
from time import mktime
import matplotlib
import matplotlib.pyplot as plt

#create a variable that holds the path to our data 
path = 'intraQuarter\\intraQuarter'

#create a function that is going to gather our key stats
#in this case our key stats is going to be debt/equity ratio

def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'\\_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    #create pandas dataframe
    df = pd.DataFrame(columns = ['Date',
    'Unix',
    'Ticker',
    'Debt Equity Ratio',
    'Price',
    'stock_p_change', 
    'SP500',
    'sp500_p_change',
    'Difference'])
    sp500_df = pd.read_csv("./YAHOO-INDEX_GSPC.csv", index_col=False, sep=";|,")
    sp500_df = pd.DataFrame(sp500_df)


    ticker_list = []
   
    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        #get ticker
        ticker = each_dir.split("\\")[3]
        ticker_list.append(ticker)
        starting_stock_value = False
        starting_sp500_value = False

        if len(each_file) >0:
            
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                date = date_stamp.strftime('%m/%d/%Y')
                unix_time = time.mktime(date_stamp.timetuple())
                full_file_path = each_dir+'\\' + file
                source = open(full_file_path, 'r').read()
                try:             
                #converting value to float so that if it isnt a # or if there is some other issue we just pass
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    
                    for i in range (0,16604):
         
                        if date == sp500_df['Date'][i]:
                            
                            Adj_Close = sp500_df['Adj Close'][i]
                            sp500_value = Adj_Close
                            stock_price = float(source.split('</small><big><b>')[1].split("</b></big>")[0])
                            if not starting_stock_value:
                                starting_stock_value = stock_price
                            if not starting_sp500_value:
                                starting_sp500_value = sp500_value
                            stock_p_change = ((stock_price - starting_stock_value) / starting_stock_value)*100
                            sp500_p_change = ((sp500_value - starting_sp500_value) / starting_sp500_value)*100
                            df = df.append({'Date':date_stamp,
                            'Unix':unix_time,
                            'Ticker':ticker,
                            'Debt Equity Ratio':value,
                            'Price': stock_price, 
                            'stock_p_change': stock_p_change,
                            'Difference': stock_p_change,
                            'Difference stock': stock_p_change-sp500_p_change,
                            'SP500': sp500_value,
                            'sp500_p_change': sp500_p_change}, ignore_index = True)
                        else:
                            pass
                        
                except Exception as e:
                    print(str(e))
                    
                
                
            
            save = gather.replace(" ","").replace(')',"").replace('(','').replace("/", "")+str('.csv')
            # print(save)
            df.to_csv(save)

        


Key_Stats()

