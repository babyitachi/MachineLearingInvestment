'''
Created on 09-Jul-2017

@author: kaybr
'''
import urllib
import os
import time

path = "/home/kaybr/python/MachineLearningInvesting/intraQuarter"

def Parse_Yahoo():
    statspath = path + '/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    counter = 0
    
    for e in stock_list[1:]:
        try:
            e = e.replace("/home/kaybr/python/MachineLearningInvesting/intraQuarter/_KeyStats/","")
            link = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/"+e.upper()+"?modules=assetProfile,financialData,defaultKeyStatistics,calendarEvents,incomeStatementHistory,cashflowStatementHistory,balanceSheetHistory"
            resp = urllib.urlopen(link).read()
            
            save = "YaParse/" + str(e) + ".json"
            store = open(save,"w")
            store.write(str(resp))
            store.close()
            counter += 1
            print("Stored " + e + ".json " + "SN. " + str(counter))
            
            
        except Exception as e:
            print(str(e),"Exception")
            time.sleep(2)
            
Parse_Yahoo()
print("Done parsing")