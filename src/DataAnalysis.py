'''
Created on 06-Jul-2017

@author: kaybr
'''
from sklearn import svm
import Build_Data_Set as bdatas

def Analysis():
    test_size = 500
    invest_amount = 10000
    total_invests = 0
    if_market = 0
    if_strat = 0
    
    X,y,Z = bdatas.Build_data_set()
    print("Length",len(X))
    
    clf = svm.SVC(kernel = "linear", C = 1.0)
    clf.fit(X[:-test_size],y[:-test_size])
    
    correct_count = 0
    predictions = clf.predict(X)
    for x in range(1,test_size+1):
        if predictions[-x] == y[-x]:
            correct_count += 1
        if predictions[-x] == 1:
            invest_return = invest_amount + invest_amount * Z[-x][0] / 100
            market_return = invest_amount + invest_amount * Z[-x][1] / 100
            
            total_invests += 1
            if_market += market_return
            if_strat += invest_return
        
               
    print("Accuracy: ", correct_count * 100.00 /test_size)
    print("Total Trades: ", total_invests)
    print("Ending With Strategy: ", if_strat)
    print("Ending With Market: ", if_market)
    
    compared = ((if_strat - if_market) / if_market) * 100
    do_nothing = total_invests * invest_amount
    
    avg_market = ((if_market - do_nothing) / do_nothing) * 100
    avg_strat = ((if_strat - do_nothing) / do_nothing) * 100
    
    print("Compared to the market we earn: "+ str(compared) + "% more")
    print("Average investment return: "+ str(avg_strat) + "%")
    print("Average market return: "+ str(avg_market) + "%")

Analysis()