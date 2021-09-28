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
flatten_portfolio = list(set(portfolio))



stock = list(map(yf.download, port))
stock1 = list(map(yf.Ticker, port))

# print(stock)
summa = 0
for i in range(len(port)):
    summa += stock[i].Close[-1]
summa = round(float(summa), 2)
print(summa)


def plot_common(period):
    for i in range(len(stock)):
        plt.plot(stock[i].Close[-period:])

    plt.show()


plot_common(200)

# Выделение скорректированой цены закрытия
# all_adj_close = stock[['Adj Close']]
# print(all_adj_close)
# print(stock[['Sector']])


# dividends = []
#
# for i in range(len(flatten_portfolio)):
#     el = flatten_portfolio[i].info['dividendRate']
#     dividends.append(el)
#
# print(flatten_portfolio)
# print(dividends)
# print(flatten_port)
#
# t_dividends = pd.DataFrame({'Stocks': flatten_port,
#                       'Dividents (per year)': dividends
#                       })
# print(t_dividends)
