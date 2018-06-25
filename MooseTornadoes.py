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
    # sp500_df = pd.read_csv("SP.csv")

    ticker_list = []
   
    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        #get ticker
        ticker = each_dir.split("\\")[3]
        ticker_list.append(ticker)
        starting_stock_value = False
        # starting_sp500_value = False
        #need to print each dir to determine what index i am calling ie 1 or 7
        # print(each_dir)
        # print(ticker)
        
        if len(each_file) >0:
            #get datestamp for each file
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_file_path = each_dir+'\\' + file
                source = open(full_file_path, 'r').read()
                try:             
                #converting value to float so that if it isnt a # or if there is some other issue we just pass
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    # try: 
                    #     sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%D')
                    #     row = sp500_df[sp500_df["Date"] == sp500_date]
                    #     sp500_value = float(row["Adj Close"])
                        
                    # except: #for weekday weekend error sakes subtract 3 days from unix time. this should aso fix any holidays
                    #     sp500_date = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%D')
                    #     row = sp500_df[sp500_df["Date"] == sp500_date]
                    #     sp500_value = float(row["Adj Close"])
                        

                    stock_price = float(source.split('</small><big><b>')[1].split("</b></big>")[0])
                    # print("stock_prices:", stock_price, "ticker:", ticker)
                    if not starting_stock_value:
                        starting_stock_value = stock_price
                    # if not starting_sp500_value:
                    #     starting_sp500_value = sp500_value
                    stock_p_change = ((stock_price - starting_stock_value) / starting_stock_value)*100
                    # sp500_p_change = ((sp500_value - starting_sp500_value) / starting_sp500_value)*100
                    df = df.append({'Date':date_stamp,
                    'Unix':unix_time,
                    'Ticker':ticker,
                    'Debt Equity Ratio':value,#}, ignore_index = True)
                    'Price': stock_price,
                    'stock_p_change': stock_p_change,
                    'Difference': stock_p_change}, ignore_index=True)
                    # 'Difference': stock_p_change-sp500_p_change)}, ignore_index=True)
                    # 'SP500': sp500_value,
                    # 'sp500_p_change': sp500_p_change}, ignore_index = True)
                except Exception as e:
                    print(str(e))
                #lets print the ticker and the debt to equity ratio
                # print(ticker+":", value)
            #now save. we will save based on 'gather' but we need to change some things. change spaces to nothing, single quote to nothing
            for each_ticker in ticker_list:
                try:
                    plot_df = df[(df['Ticker'] == each_ticker)]
                    plot_df = plot_df.set_index(['Date'])
                    plot_df['Difference'].plot(label=each_ticker)
                    plt.legend
                    plt.show()
                except:
                    pass
            save = gather.replace(" ","").replace(')',"").replace('(','').replace("/", "")+str('.csv')
            print(save)
            df.to_csv(save)





            # time.sleep(15)
#at this point we have the stock name and the time stamp for the data we are about to collect



Key_Stats()
