import yfinance as yf
import os
import datetime
import math
from stockalarm import StockAlarm 


now = datetime.datetime.now().date()

friday = "2021-02-19"
stonkList = "GME AMC PLTR TSLA"
data = yf.download(tickers = stonkList, interval = "1m",start = friday)

print(data)


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