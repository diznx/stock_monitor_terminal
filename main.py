import yfinance

tickersymbol1 = 'AMC'
tickersymbol2 = 'GME'

tickerData1 = yfinance.Ticker(tickersymbol1)
tickerData2 = yfinance.Ticker(tickersymbol2)

tickerDf1 = tickerData1.info['regularMarketPrice']
tickerDf2 = tickerData2.info['regularMarketPrice']

print("Current Ticker Price")
print("AMC $" + str(round(tickerDf1)))
print("GME $" + str(round(tickerDf2)))
print()
print("Total Current Value")
print("AMC $" + str(round(tickerDf1) * 10))
print("GME $" + str(round(tickerDf2) * 10))
