import yfinance as yf
import pandas as pd

#This commmand allows me to view more rows of the data
pd.set_option('display.max_rows', None)

# This will download the S&P 500 index data
# The index data is represented by the ticker symbol "^GSPC"
# A ticker is a unique identifier for a particular stock or index on the stock market
sp500 = yf.Ticker("^GSPC")

# Next well find the history of the data from the S&P 500 index
sp500 = sp500.history(period="max") 

df = pd.DataFrame(sp500)
print(df)

