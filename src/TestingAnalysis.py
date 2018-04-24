'''
Created on 13-Jul-2017

@author: kaybr
'''
from sklearn import svm,preprocessing
import Build_Data_Set as bdatas
import pandas as pd
import numpy as np
from collections import Counter

def Test():
    test_size = 1
    invest_amount = 10000
    total_invests = 0
    if_market = 0
    if_strat = 0
    
    X,y,Z = bdatas.Build_data_set()
    #print("Length: " + str(len(X)))
    
    clf = svm.SVC(kernel = "linear", C = 1.0)
    clf.fit(X[:-test_size], y[:-test_size])
    
    correct_count = 0
    predictions = clf.predict(X)
    for x in range(1, test_size + 1):
        if predictions[-x] == y[-x]:
            correct_count += 1
        if predictions[-x] == 1:
            invest_return = invest_amount + invest_amount * Z[-x][0] / 100
            market_return = invest_amount + invest_amount * Z[-x][1] / 100
            
            total_invests += 1
            if_market += 1
            if_strat += 1

            
    data_df = pd.DataFrame.from_csv("YaParse_sample_NO_NA.csv")
    data_df = data_df.replace("N/A",0).replace("NaN",0)
    X = np.array(data_df[bdatas.FEATURES].values)
    X = preprocessing.scale(X)
    
    Z = data_df["Ticker"].values.tolist()
    
    invest_list = []
    
    for i in range(len(X)):
        p = predictions[i]
        if p == 1:
#             print(Z[i])
            invest_list.append(Z[i])
            
#     print(len(invest_list))
#     print(invest_list)
    
    return invest_list


final_list = []
loops = 10

for x in range(loops):
    stock_list = Test()
    for e in stock_list:
        final_list.append(e)
        
print(final_list)
x = Counter(final_list)
print(15*"_")
count = 0
Cut_off = loops - (loops/3)
print("Cut-off: " + str(Cut_off))
for each in x:
    print("X[each]: ",x[each], "each: ", each)
    if x[each] > Cut_off:
        print(each)
        count += 1

print("Count: " + str(count)) 