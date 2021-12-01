import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import yfinance as yf
import datetime

def set_assets(uni_var):
    assets = []

    for i in range(uni_var[6]):
        assets.append(uni_var[7][i].tail(1))

    assets = pd.concat(assets)
    assets.index = uni_var[2]
    assets = assets.round(2)
    assets['Dividends (per year)'] = uni_var[8]
    assets.insert(0, 'Number', uni_var[4])

    major_holders = []
    for i in range(uni_var[5]):
        major_holders.append(pd.DataFrame(np.array(uni_var[3][i].major_holders),
                                          columns=[uni_var[2][i], 'stock']).set_index('stock').T)

    assets = assets.join(pd.concat(major_holders))
    assets.insert(0, 'Stocks', uni_var[2])
    assets.pop('Adj Close')

    return assets


# stock growth Pandas DataFrame
def set_stock_growth(uni_var):
    list_of_stock_growth_percentages = []
    list_of_stock_growth = []
    for i in range(uni_var[5]):
        list_of_stock_growth_percentages.append(round((uni_var[7][i].Close[-1] /
                                                       uni_var[7][i].Close[-2] - 1) * 100, 2))
        list_of_stock_growth.append(round((uni_var[7][i].Close[-1] - uni_var[7][i].Close[-2]), 2))

    stock_growth = pd.DataFrame({'Stock growth, %': list_of_stock_growth_percentages,
                                 'Stock growth, RUB': list_of_stock_growth},
                                index=uni_var[2])

    stock_growth.insert(0, 'Stocks', uni_var[2])

    return stock_growth


# pie plot of assets
def plot_p(uni_var):
    fig_p, ax1 = plt.subplots()
    ax1.pie(uni_var[4], labels=uni_var[2])
    plt.style.use('dark_background')
    fig_p.set_facecolor('#19232D')
    ax1.set_title('Amount of Stocks')

    return fig_p


# plot of time series
def plot_common(period, var):
    var = list(set(var))
    fig_c, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    for i in range(len(var)):
        ax1.plot(yf.download(var[i], start=datetime.date.today() - datetime.timedelta(days=period),
                             end=datetime.date.today()).Close)
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    ax1.legend(var)
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Price, $')
    ax1.set_title('Price of Stocks')
    fig_c.set_facecolor('#19232D')
    plt.style.use('dark_background')
    return fig_c
