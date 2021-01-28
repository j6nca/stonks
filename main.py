import config
import requests
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import pandas as pd
import matplotlib.pyplot as plt

company='MSFT'

ts = TimeSeries(key=config.AV_KEY, output_format='pandas')
data_ts, metadata_ts = ts.get_intraday(symbol=company, interval='1min', outputsize='full')

period = 60
ti = TechIndicators(key=config.AV_KEY, output_format='pandas')
data_ti, metadata_ti = ti.get_sma(symbol=company, interval='1min', time_period=period, series_type='close')

df1 = data_ti
df2 = data_ts['4. close'].iloc[period-1::]

df2.index = df1.index
total_df = pd.concat([df1,df2], axis=1)
print(total_df)

total_df.plot()
plt.show()


