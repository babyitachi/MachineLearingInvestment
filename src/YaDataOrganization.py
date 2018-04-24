'''
Created on 25-Jun-2017

@author: kaybr
'''
import pandas as pd
import os
import re
import time
import sys
from yahoo_finance import Share

def YaOrg(gather = ['debtToEquity',
                    'Trailing P/E',
                    'Price/Sales',
                    'priceToBook',
                    'profitMargins',
                    'operatingMargins',
                    'returnOnAssets',
                    'returnOnEquity',
                    'revenuePerShare',
                    'Market Cap',
                    'enterpriseValue',
                    'forwardPE',
                    'pegRatio',
                    'enterpriseToRevenue',
                    'enterpriseToEbitda',
                    'totalRevenue',
                    'grossProfit',
                    'ebitda',
                    'netIncomeToCommon',
                    'trailingEps',
                    'earningsGrowth',
                    'revenueGrowth',
                    'totalCash',
                    'totalCashPerShare',
                    'totalDebt',
                    'currentRatio',
                    'bookValue',
                    'operatingCashflow',
                    'beta',
                    'heldPercentInsiders',
                    'heldPercentInstitutions',
                    'sharesShort',
                    'shortRatio',
                    'shortPercentOfFloat',
                    'sharesShortPriorMonth',
                    'currentPrice',
                    'sharesOutstanding']):
    
    df = pd.DataFrame(columns = ['Date',
                                 'Unix',
                                 'Ticker',
                                 'Price',
                                 'stock_p_change',
                                 'SP500',
                                 'sp500_p_change',
                                 'Difference',
                                 'DE Ratio',
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
                                 'Shares Short (prior ',                                
                                 'Status'])
    
    #time.sleep(2)
    
    file_list = os.listdir("YaParse")
    counter = 0
    passfiles = 0
    for each_file in file_list:
        ticker = each_file.split(".json")[0]
        full_file_path = "YaParse/" + each_file
        source = open(full_file_path, "r").read()
        data = Share(ticker.upper())
        counter += 1
        print("File No: " +  str(counter))
        try:
            value_list = []
            
            for each_data in gather:
                try:
                    #value = float(source.split(gather + ':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])
                    regex = re.escape(each_data) + r'.*?(\d{1,8}\.\d{1,8}M?B?K?|N/A)%?'
                    value = re.search(regex, source)
                    value = (value.group(1))
                    
                    if "B" in value:
                        value = float(value.replace("B",'')) * 1000000000
                    elif "M" in value:
                        value = float(value.replace("M",'')) * 1000000
                        
                    value_list.append(value)
                    
                except Exception as e:
                    if not(each_data == 'Trailing P/E' or each_data == 'Price/Sales' or each_data == 'Market Cap'):
                        print("Exception1: " + str(e))
                        print("Data: " + str(each_data) + " File: " + str(each_file))
                    #time.sleep(5)
                    value = "N/A"
                    
                    if each_data == 'Price/Sales':
                        value = data.get_price_sales()
                        
                    if each_data == 'Market Cap':
                        value = data.get_market_cap()
                    
                    if each_data == 'Trailing P/E':
                        value = data.get_price_earnings_ratio()
                        
                    try:
                        
                        if "B" in value:
                            value = float(value.replace("B",'')) * 1000000000
                        elif "M" in value:
                            value = float(value.replace("M",'')) * 1000000
                    except Exception as e:
                        value = "N/A"
                    
                    value_list.append(value)
                    
            #print(value_list)
            #time.sleep(5)
            
            
            if value_list.count("N/A") > 0:
                print("Passing on this file: " + str(each_file) + " ::::Count of N/A: " + str(value_list.count("N/A")))
                passfiles +=1
                pass
            
            else:
                try:
                    df = df.append({'Date':"N/A",
                                    'Unix':"N/A",
                                    'Ticker':ticker,
                                    'Price':"N/A",
                                    'stock_p_change':"N/A",
                                    'SP500':"N/A",
                                    'sp500_p_change':"N/A",
                                    'Difference':"N/A",
                                    'DE Ratio':value_list[0],
                                    'Trailing P/E':value_list[1],
                                    'Price/Sales':value_list[2],
                                    'Price/Book':value_list[3],
                                    'Profit Margin':value_list[4],
                                    'Operating Margin':value_list[5],
                                    'Return on Assets':value_list[6],
                                    'Return on Equity':value_list[7],
                                    'Revenue Per Share':value_list[8],
                                    'Market Cap':value_list[9],
                                    'Enterprise Value':value_list[10],
                                    'Forward P/E':value_list[11],
                                    'PEG Ratio':value_list[12],
                                    'Enterprise Value/Revenue':value_list[13],
                                    'Enterprise Value/EBITDA':value_list[14],
                                    'Revenue':value_list[15],
                                    'Gross Profit':value_list[16],
                                    'EBITDA':value_list[17],
                                    'Net Income Avl to Common ':value_list[18],
                                    'Diluted EPS':value_list[19],
                                    'Earnings Growth':value_list[20],
                                    'Revenue Growth':value_list[21],
                                    'Total Cash':value_list[22],
                                    'Total Cash Per Share':value_list[23],
                                    'Total Debt':value_list[24],
                                    'Current Ratio':value_list[25],
                                    'Book Value Per Share':value_list[26],
                                    'Cash Flow':value_list[27],
                                    'Beta':value_list[28],
                                    'Held by Insiders':value_list[29],
                                    'Held by Institutions':value_list[30],
                                    'Shares Short (as of':value_list[31],
                                    'Short Ratio':value_list[32],
                                    'Short % of Float':value_list[33],
                                    'Shares Short (prior ':value_list[34],
                                    'Current Price': value_list[35],
                                    'Shares Outstanding': value_list[36],
                                    'Status':"N/A"}, ignore_index = True)
                
                except Exception as e:
                    print("Problem in DF Append: " + str(e))
                    print("Data: " + str(each_data) + "File: " + str(each_file))
                    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
                    time.sleep(5)
                
                #print("DataFrame: ", df)
                    
        except Exception as e:
            print("Problem as a whole: " + str(e))
            print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)
            pass
        
    df.to_csv('YaParse_sample_NO_NA.csv')
    print("Done making csv")
    print("No. of files passed: " + str(passfiles))
            
YaOrg()
