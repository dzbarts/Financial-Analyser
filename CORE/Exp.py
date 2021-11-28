

import yfinance as yf

portfolio = list(map(yf.Ticker, ['msft', 'msft']))

import time
import datetime
start_time = time.time()
print(yf.download('msft', start=datetime.date.today() - datetime.timedelta(days=361), end=datetime.date.today()))
print("--- %s seconds ---" % (time.time() - start_time))