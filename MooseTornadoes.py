import pandas as pd
import os
import time
from datetime import datetime

#create a variable that holds the path to our data 
path = 'C:\\Users\\Carre\\Desktop\\intraQuarter\\intraQuarter'

#create a function that is going to gather our key stats
#in this case our key stats is going to be debt/equity ratio
#gather is going to be what we want to gather, specifically the name of the data in the table


def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'\\_KeyStats'
    #get the list of stocks. this gathers just the name for the directory of contents
    stock_list = [x[0] for x in os.walk(statspath)]
    # print(stock_list)
    #create pandas dataframe
    df = pd.DataFrame(columns = ['Date','Unix','Ticker','Debt Equity Ratio'])
    #now lets get the list without the root directory attached
    #create S&P dataframe that we will compare against
    sp500_df = pd.DataFrame.from_csv("SP.csv")

    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir) #this is listing out all the directories under the first director 'a'
        #get ticker
        ticker = each_dir.split("\\")[7]
        #need to print each dir to determine what index i am calling ie 1 or 7
        # print(each_dir)
        # print(ticker)
        # time.sleep(15)
        #so now we have all the file name
        #weed out files with no data or incorrect data
        if len(each_file) >0:
            #get datestamp for each file
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                # status check
                # print(date_stamp, unix_time)
                #open up the file plath + stats path + file
                full_file_path = each_dir+'\\' + file
                # print(full_file_path)
                source = open(full_file_path, 'r').read()
                try:
                    
                # status check
                # print(source)
                #print the value we are looking for 
                #parsing the table with one line of code
                #converting value to float so that if it isnt a # or if there is some other issue we just pass
                    value = float(source.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    
                    # try: 
                    #     sp500_date = datetime.fromtimestamp(unix_time).strftime("%Y-%m-%D")
                    #     row = sp500_df[sp500_df["Date"] == sp500_date]
                    #     sp500_value = float(row["Adj Close"])
                    # except: #for weekday weekend error sakes subtract 3 days from unix time. this should aso fix any holidays
                    #     sp500_date = datetime.fromtimestamp(unix_time-259200).strftime("%Y-%m-%D")
                    #     row = sp500_df[sp500_df["Date"] == sp500_date]
                    #     sp500_value = float(row["Adj Close"])

                    stock_price = float(source.split('</small><big><b>')[1].split("</b></big>")[0])
                    print("stock_prices:", stock_price, "ticker:", ticker)
                    df = df.append({'Date':date_stamp,'Unix':unix_time,'Ticker':ticker,'Debt Equity Ratio':value,}, ignore_index = True)
                except Exception as e:
                    pass
                #lets print the tickere and the debt to equity ratio
                # print(ticker+":", value)
            #now save. we will save based on 'gather' but we need to change some things. change spaces to nothing, single quote to nothing
            save = gather.replace(" ","").replace(')',"").replace('(','').replace("/", "")+str('.csv')
            print(save)
            df.to_csv(save)





            # time.sleep(15)
#at this point we have the stock name and the time stamp for the data we are about to collect



Key_Stats()
