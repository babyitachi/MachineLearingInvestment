'''
Created on 08-Jul-2017

@author: kaybr
'''
import pandas as pd
import os
import quandl
import time

quandl.ApiConfig.api_key = "SK3ZQVgbJkEwVxwDH36T"
path = "/home/kaybr/python/MachineLearningInvesting/intraQuarter"

def Stock_Prices():
    df = pd.DataFrame()
    statspath = path + '/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    
    for each_dir in stock_list[1:]:
        try:
            ticker = each_dir.split("/")[-1]
            print(ticker)
            name = "WIKI/" + ticker.upper()
            data = quandl.get(name, start_date = "2000-12-12", end_date = "2014-12-31")
            data[ticker.upper()] = data["Adj. Close"]
            df = pd.concat([df, data[ticker.upper()]], axis = 1)
        except Exception as e:
            print("Starting 2nd pass:",str(e))
            time.sleep(5)
            try:
                ticker = each_dir.split("/")[-1]
                print(ticker)
                name = "WIKI/" + ticker.upper()
                data = quandl.get(name, start_date = "2000-12-12", end_date = "2014-12-31")
                data[ticker.upper()] = data["Adj. Close"]
                df = pd.concat([df, data[ticker.upper()]], axis = 1)
            except Exception as e:
                print("Something is wrong:",str(e))
                
    df.to_csv("stock_prices.csv")
    
Stock_Prices()