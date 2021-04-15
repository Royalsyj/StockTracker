import yfinance as yf
import os
import datetime
import math
from stockalarm import StockAlarm 
import time
import numpy as np


now = datetime.datetime.now().date()

friday = "2021-04-9"
stonkList = "GME AMC PLTR TSLA"
data = yf.download(tickers = stonkList, period='1d', interval = "1m",start = friday)

print(data)

test_list = "PLTR GME CRSR AMD INTC NVDA"
split_test_list = test_list.split()
while True:
    refresh_Data = yf.download(tickers = test_list, period='1d', interval = "1m")
    print(str(refresh_Data.iloc[-1].name))      # Print timestamp
    for stonk in split_test_list:
        # Check if Open value of stonk is real number
        if not np.isnan(refresh_Data.iloc[-1]["Open"][stonk]):
            print("Stonk: {} -> Open  : {}".format(str(stonk), str(refresh_Data.iloc[-1]["Open"][stonk])))
        # Check if Close value of stonk is real number
        if not np.isnan(refresh_Data.iloc[-1]["Close"][stonk]):
            print("Stonk: {} -> Close : {}".format(str(stonk), str(refresh_Data.iloc[-1]["Close"][stonk])))
    time.sleep(10)
    # To-do: Break down dataframe information into lists per stock
    # To-do: Save a local csv file periodically with timestamps (one file per stock?)
    # To-do: Filter out NaNs from latest downloads and only print out real numbers
    # # Sub-task: Find most recent real number if latest is nan
#-------------- Example --------------#

# NXE = yf.Ticker("NXE")
# GME = yf.Ticker("GME")
# AMC = yf.Ticker("AMC")
# APHA = yf.Ticker("APHA")

# # get historical market data
# hist = NXE.history(period="max")

# print(NXE.info["regularMarketPrice"])
# print(GME.info["regularMarketPrice"])
# print(AMC.info["regularMarketPrice"])
# print(APHA.info["regularMarketPrice"])

# print("Ask: " + str(NXE.info["ask"]))
# print("Ask: " + str(GME.info["ask"]))
# print("Ask: " + str(AMC.info["ask"]))
# print("Ask: " + str(APHA.info["ask"]))