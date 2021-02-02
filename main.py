import pandas as pd
import numpy as np
import strategies
import data
import visualize
#############################
##1. Sample 3 moving averages
symbol = 'AAPL'
df = data.get_daily(symbol)

long=26 #63
mid=19 #29
short=12 #5
#Calculating 3 moving averages
#1. short/fast exponential moving average
short_ema = df['4. close'].ewm(span=short, adjust=False).mean()
#2. long/slow exponential moving average
long_ema = df['4. close'].ewm(span=long, adjust=False).mean()
#3. medium exponential moving average
mid_ema = df['4. close'].ewm(span=mid, adjust=False).mean()

#Strategy is to look at intersection of moving average lines
#Append moving averages to dataframe
df['Short'] = short_ema
df['Middle'] = mid_ema
df['Long'] = long_ema

#Store buy/sell data in dataframe
df['Buy'] = strategies.strategy_3ma(df)[0]
df['Sell'] = strategies.strategy_3ma(df)[1]

#Profit calculation
print(strategies.unit_net(df))

visualize.buy_sell_plot(symbol, df)

#############################
##1. Sample Moving averages






