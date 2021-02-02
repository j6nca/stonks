#Description: The 3 moving average strategy for b/s
import pandas as pd
import numpy as np
import visualize
import data

###Functions
##Strategies

#3 Moving Averages Strategy
def strategy_3ma(data):
    buy_list = []
    sell_list = []
    #managing buy signals
    flag_long = False
    flag_short = False

    #buy/sell logic
    for i in range(0, len(data)):
        if data['Middle'][i] < data['Long'][i] and data['Short'][i] < data['Middle'][i] and flag_long == False and flag_short == False:
            #buy
            buy_list.append(data['4. close'][i])
            sell_list.append(np.nan)
            flag_short = True
        elif flag_short == True and data['Short'][i] > data['Middle'][i]:
            #sell
            sell_list.append(data['4. close'][i])
            buy_list.append(np.nan)
            flag_short = False
        elif data['Middle'][i] > data['Long'][i] and data['Short'][i] > data['Middle'][i] and flag_long == False and flag_short == False:
            #buy
            buy_list.append(data['4. close'][i])
            sell_list.append(np.nan)
            flag_long = True
        elif flag_long == True and data['Short'][i] < data['Middle'][i]:
            #sell
            sell_list.append(data['4. close'][i])
            buy_list.append(np.nan)
            flag_long = False
        else:
            buy_list.append(np.nan)
            sell_list.append(np.nan)

    return (buy_list, sell_list)

##Profit Calculation
def unit_net(data):
    net=0
    #remove endpts
    firstbuy = False
    lastsell = False
    for i in range(0, len(data)):
        if firstbuy and not pd.isna(data['Buy'][i]):
            net = net - data['Buy'][i]
            print("Bought: ", data['Buy'][i])

            if (len((data['Buy'][i:len(data) - 1].dropna())) == 1):
                lastsell = True
        elif not lastsell and not pd.isna(data['Sell'][i]):
            net = net + data['Sell'][i]
            print("Sold: ", data['Sell'][i])
            firstbuy = True
    return net




