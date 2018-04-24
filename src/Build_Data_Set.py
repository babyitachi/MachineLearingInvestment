'''
Created on 06-Jul-2017

@author: kaybr
'''
import numpy as np
import pandas as pd
from sklearn import preprocessing

how_much_better = 5

FEATURES =  ['DE Ratio',
             'Trailing P/E',
             'Price/Sales',
             'Price/Book',
             'Profit Margin',
             'Operating Margin',
             'Return on Assets',
             'Return on Equity',
             'Revenue Per Share',
             'Market Cap',
             'Enterprise Value',
             'Forward P/E',
             'PEG Ratio',
             'Enterprise Value/Revenue',
             'Enterprise Value/EBITDA',
             'Revenue',
             'Gross Profit',
             'EBITDA',
             'Net Income Avl to Common ',
             'Diluted EPS',
             'Earnings Growth',
             'Revenue Growth',
             'Total Cash',
             'Total Cash Per Share',
             'Total Debt',
             'Current Ratio',
             'Book Value Per Share',
             'Cash Flow',
             'Beta',
             'Held by Insiders',
             'Held by Institutions',
             'Shares Short (as of',
             'Short Ratio',
             'Short % of Float',
             'Shares Short (prior ']

def Status_Calc(stock, sp500):
    difference = stock - sp500
    
    if difference > how_much_better:
        return 1
    else:
        return 0

def Build_data_set():
    data_df = pd.DataFrame.from_csv("key_stats_acc_perf_NO_NA_enhanced.csv")
    data_df = data_df.reindex(np.random.permutation(data_df.index))
    data_df = data_df.replace("NaN",0).replace("N/A",0)
    
    data_df["Status2"] = list(map(Status_Calc, data_df["stock_p_change"], data_df["sp500_p_change"]))
    
    X = np.array(data_df[FEATURES].values)
    X = preprocessing.scale(X)
    y = (data_df["Status2"].replace("Underperform",0).replace("Outperform",1).values.tolist())
    Z = np.array(data_df[["stock_p_change","sp500_p_change"]])
    
    return X,y,Z