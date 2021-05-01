import yfinance as yf
import os
import datetime
import math
from stockalarm import StockAlarm 

def gradient(current, previous):

    gradient = current/previous

    return gradient

now = datetime.datetime.now().date()

monday = "2021-03-29"
stonkList = "GME AMC PLTR TSLA"
data = yf.download(tickers = stonkList, interval = "1m",start = monday)

print(data)

NXE = yf.Ticker("NXE")
GME = yf.Ticker("GME")
AMC = yf.Ticker("AMC")
APHA = yf.Ticker("APHA")

previousMarketPrice = {"NXE": NXE.info["regularMarketPrice"], "GME": GME.info["regularMarketPrice"], "AMC": AMC.info["regularMarketPrice"], "APHA": APHA.info["regularMarketPrice"]}


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

currentNXE = NXE.info["regularMarketPrice"]
currentGME = GME.info["regularMarketPrice"]
currentAMC = AMC.info["regularMarketPrice"]
currentAPHA = APHA.info["regularMarketPrice"]

previousNXE = previousMarketPrice["NXE"]
previousGME = previousMarketPrice["GME"]
previousAMC = previousMarketPrice["AMC"]
previousAPHA = previousMarketPrice["APHA"]

gradients = {"NXE": gradient(currentNXE, previousNXE), "GME": gradient(currentGME, previousGME), "AMC": gradient(currentAMC, previousAMC), "APHA": gradient(currentAPHA, previousAPHA)}

for key in gradients:

    if(gradients[key] > 1):

        print("Stock Name: " + key)
        StockAlarm.rocketTrend

    elif(gradients[key] < 1):

        print("Stock Name: " + key)
        StockAlarm.crashingTrend

previousMarketPrice = {"NXE": NXE.info["regularMarketPrice"], "GME": GME.info["regularMarketPrice"], "AMC": AMC.info["regularMarketPrice"], "APHA": APHA.info["regularMarketPrice"]}