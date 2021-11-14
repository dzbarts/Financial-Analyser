import pandas as pd
from Plots import *
import yfinance as yf


def set_recom(risk, uni_var):
    recom = pd.DataFrame(index=uni_var[2])
    recom['Stocks'] = uni_var[2]
    recom['SMA'] = list(map(lambda x: plot_SMA(300, x, risk)[0], uni_var[7]))
    recom['twoSMA'] = list(map(lambda x: plot_twoSMA(300, x, risk)[0], uni_var[7]))
    recom['EMA'] = list(map(lambda x: plot_EMA(300, x, risk)[0], uni_var[7]))
    recom['DEMA'] = list(map(lambda x: plot_DEMA(300, x, risk)[0], uni_var[7]))
    recom['TEMA'] = list(map(lambda x: plot_TEMA(300, x, risk)[0], uni_var[7]))
    recom['MACD'] = list(map(lambda x: plot_MACD(300, x)[0], uni_var[7]))
    recom['CHV'] = list(map(lambda x: plot_CHV(300, x, risk)[0], uni_var[7]))
    recom['RSI'] = list(map(lambda x: plot_RSI(300, x, risk)[0], uni_var[7]))
    recom['bulls'] = list(map(lambda x: plot_bulls(300, x, risk)[0], uni_var[7]))
    recom['bears'] = list(map(lambda x: plot_bears(300, x, risk)[0], uni_var[7]))
    recom['ER'] = list(map(lambda x: plot_ER(300, x, risk)[0], uni_var[7]))
    recom['MI'] = list(map(lambda x: plot_MI(300, x)[0], uni_var[7]))

    agg1 = recom[recom.columns[1:8]].sum(axis=1)
    agg = []

    for i in range(len(agg1)):
        if agg1[i] > 7 and recom['RSI'][i] != 4 \
                and recom['ER'][i] != 4 \
                and recom['MI'][i] != 6:
            agg.append("BUY")
        elif agg1[i] < 7 and recom['RSI'][i] != 3 \
                and recom['ER'][i] != 3 \
                and recom['MI'][i] != 6:
            agg.append("SELL")
        else:
            agg.append("WAIT")

    recom['Agg'] = agg

    recom = recom.replace(to_replace=1, value='WAIT', regex=True)
    recom = recom.replace(to_replace=0, value='SELL', regex=True)
    recom = recom.replace(to_replace=2, value='BUY', regex=True)
    recom = recom.replace(to_replace=3, value='NSELL', regex=True)
    recom = recom.replace(to_replace=4, value='NBUY', regex=True)
    recom = recom.replace(to_replace=5, value='OK', regex=True)
    recom = recom.replace(to_replace=6, value='NT', regex=True)

    return recom


def final_plot(period, data, risk, x):
    data = yf.download(data)
    if x == 1:
        return plot_SMA(period, data, risk)[1:3]
    elif x == 2:
        return plot_twoSMA(period, data, risk)[1:4]
    elif x == 3:
        return plot_EMA(period, data, risk)[1:3]
    elif x == 4:
        return plot_DEMA(period, data, risk)[1:3]
    elif x == 5:
        return plot_TEMA(period, data, risk)[1:3]
    elif x == 6:
        return plot_MACD(period, data)[1:4]
    elif x == 7:
        return plot_CHV(period, data, risk)[1:3]
    elif x == 8:
        return plot_RSI(period, data, risk)[1:4]
    elif x == 9:
        return plot_bulls(period, data, risk)[1:3]
    elif x == 10:
        return plot_bears(period, data, risk)[1:3]
    elif x == 11:
        return plot_ER(period, data, risk)[1:5]
    else:
        return plot_MI(period, data, risk)[1:4]
