import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# This will download the S&P 500 index data
# The index data is represented by the ticker symbol "^GSPC"
# A ticker is a unique identifier for a particular stock or index on the stock market
sp500 = yf.Ticker("^GSPC")
GOLD = yf.Ticker("GLD")

# Next well find the history of the data from the S&P 500 index
sp500 = sp500.history(period="max")
GOLD = GOLD.history(period="max") 

df = pd.DataFrame(sp500)
print(df)

df2 = pd.DataFrame(GOLD)
print(df2)

sp500.plot.line(y="Close", use_index=True)
plt.show()

GOLD.plot.line(y="Close", use_index=True)
plt.show()


