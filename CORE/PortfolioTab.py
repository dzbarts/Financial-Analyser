import pandas as pd
import matplotlib.pyplot as plt
from Portfolio import *

stock = list(map(yf.download, flatten_port))

summa = 0

for i in range(len(flatten_port)):
    summa += stock[i].Close[-1] * weight_of_stocks[i]
summa = round(float(summa), 2)


def plot_common(period):
    for i in range(len(stock)):
        plt.plot(stock[i].Close[-period:])

    plt.show()


#plot_common(200)

# Выделение скорректированой цены закрытия
# all_adj_close = stock[['Adj Close']]
# print(all_adj_close)
# print(stock[['Sector']])


dividends = []

for i in range(len(flatten_portfolio)):
    dividends.append(flatten_portfolio[i].info['dividendRate'])
#
# t_dividends = pd.DataFrame({'Stocks': flatten_port,
#                       'Dividents (per year)': dividends
#                       })


assets = []

for i in range(len(stock)):
    assets.append(stock[i].tail(1))

assets = pd.concat(assets)

assets.index = flatten_port

assets['Dividents (per year)'] = dividends

assets.insert(0, 'Number', weight_of_stocks)

# holders = []
#
# for i in range(len(flatten_portfolio)):
#     holders.append(flatten_portfolio[i].major_holders)

# holders = pd.concat(holders)

# assets['Major holders'] = holders


# print(holders)
print(assets)


def plot_p():
    fig1, ax1 = plt.subplots()
    ax1.pie(weight_of_stocks, labels=flatten_port)
    plt.show()