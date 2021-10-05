import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Portfolio import *


# some base variants
stock = list(map(yf.download, flatten_port))

# total cost
cost = 0

for i in range(len(flatten_port)):
    cost += stock[i].Close[-1] * weight_of_stocks[i]
cost = round(float(cost), 2)


# plot of time series
def plot_common(period):
    for i in range(len(stock)):
        plt.plot(stock[i].Close[-period:])

    plt.show()


# column of dividends
dividends = []

for i in range(len(flatten_portfolio)):
    dividends.append(flatten_portfolio[i].info['dividendRate'])


# assets Pandas DataFrame
assets = []

for i in range(len(stock)):
    assets.append(stock[i].tail(1))

assets = pd.concat(assets)
assets.index = flatten_port
assets['Dividends (per year)'] = dividends
assets.insert(0, 'Number', weight_of_stocks)


major_holders = []
for i in range(len(flatten_port)):
    major_holders.append(pd.DataFrame(np.array(flatten_portfolio[i].major_holders),
                                      columns=[flatten_port[i], 'stock']).set_index('stock').T)


assets = assets.join(pd.concat(major_holders))


# pie plot of assets
def plot_p():
    fig1, ax1 = plt.subplots()
    ax1.pie(weight_of_stocks, labels=flatten_port)
    plt.show()
