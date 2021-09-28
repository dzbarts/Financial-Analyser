import yfinance as yf
import pandas as pd

a = yf.Ticker('MSFT')

print(a.info['dividendRate'])

port = ['msft', 'msft', 'aapl', 'TSLA',
        'YNDX', 'RY', 'RY', 'RY', 'RY',
        'RY', 'SBER.ME', 'SBER.ME', 'SBER.ME']
portfolio = []

port = list(map(str.upper, port))
portfolio = list(map(yf.Ticker, port))

flatten_port = list(set(port))
flatten_portfolio = list(set(portfolio))


dividends = []

for i in range(len(flatten_portfolio)):
    el = flatten_portfolio[i].info['dividendRate']
    dividends.append(el)

print(flatten_portfolio)
print(dividends)
print(flatten_port)

t_dividends = pd.DataFrame({'Stocks': flatten_port,
                      'Dividents (per year)': dividends
                      })
print(t_dividends)