import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib


def set_assets(uni_var):
    # column of dividends
    dividends = []

    for i in range(uni_var[5]):
        dividends.append(uni_var[3][i].info['dividendRate'])

    assets = []

    for i in range(uni_var[6]):
        assets.append(uni_var[7][i].tail(1))

    assets = pd.concat(assets)
    assets.index = uni_var[2]
    assets = assets.round(2)
    assets['Dividends (per year)'] = dividends
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
    fig_p.set_facecolor('#19232D')

    return fig_p


# plot of time series
def plot_common(period, uni_var):
    fig_c, ax1 = plt.subplots()
    for i in range(uni_var[6]):
        ax1.plot(uni_var[7][i].Close[-period:])

    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    fig_c.set_facecolor('#19232D')
    plt.style.use('dark_background')

    return fig_c
