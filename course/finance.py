import yfinance as yf

# Create a ticker object
ticker = yf.Ticker("N=F")

# Download historical data
data = ticker.history(period="1y")
#data = ticker.download(period="1y")
print(data)
