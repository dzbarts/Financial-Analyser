import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

port = ['msft', 'msft', 'aapl', 'TSLA',
        'YNDX', 'RY', 'RY', 'RY', 'RY',
        'RY', 'SBER.ME', 'SBER.ME', 'SBER.ME']
portfolio = []

port = list(map(str.upper, port))
portfolio = list(map(yf.Ticker, port))

flatten_port = list(set(port))
flatten_portfolio = list(map(yf.Ticker, flatten_port))


weight_of_stocks = []
for i in range(len(flatten_port)):
    # weight.append(list_of_sectors.count(flatten_port[i]))
    weight_of_stocks.append((port.count(flatten_port[i])))