import yfinance as yf
import os
import datetime
import math
from stockalarm import StockAlarm 
import time


now = datetime.datetime.now().date()

friday = "2021-04-9"
stonkList = "GME AMC PLTR TSLA"
data = yf.download(tickers = stonkList, period='1d', interval = "1m",start = friday)

print(data)

test_list = "PLTR GME CRSR AMD INTC NVDA"
while True:
    refresh_Data = yf.download(tickers = test_list, period='1d', interval = "1m")
    print(refresh_Data.loc[refresh_Data.index[-1], 'Close'])
    time.sleep(10)
    # To-do: Break down dataframe information into lists per stock
    # To-do: Save a local csv file periodically with timestamps (one file per stock?)
    # To-do: Filter out NaNs from latest downloads and only print out real numbers
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