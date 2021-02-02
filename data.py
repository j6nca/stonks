# import config
# import pandas as pd
# from alpha_vantage.timeseries import TimeSeries
#
# def main(symbol: str) -> pd.DataFrame:
#     ts = TimeSeries(key=config.AV_KEY, output_format="pandas")
#     data, _ = ts.get_intraday(symbol, interval='1min')
#     return data

import config
import requests
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import pandas as pd
import matplotlib.pyplot as plt

def get_day(symbol: str):
    ts = TimeSeries(key=config.AV_KEY, output_format="pandas")
    data, _ = ts.get_intraday(symbol, interval='1min')
    return data

def get_daily(symbol: str):
    ts = TimeSeries(key=config.AV_KEY, output_format="pandas")
    data, _ = ts.get_daily(symbol)
    return data

def get_weekly(symbol: str):
    ts = TimeSeries(key=config.AV_KEY, output_format="pandas")
    data, _ = ts.get_weekly(symbol)
    return data

def get_monthly(symbol: str):
    ts = TimeSeries(key=config.AV_KEY, output_format="pandas")
    data, _ = ts.get_monthly(symbol)
    return data