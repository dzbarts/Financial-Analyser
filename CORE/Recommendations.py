import pandas as pd
import datetime
import yfinance as yf

from Plots import *
from Recs import *


def set_recom(risk, uni_var):
    recom = pd.DataFrame(index=uni_var[2])
    recom['Stocks'] = uni_var[2]
    recom['SMA'] = list(map(lambda x: rec_SMA(300, x, risk), uni_var[7]))
    recom['twoSMA'] = list(map(lambda x: rec_twoSMA(300, x, risk), uni_var[7]))
    recom['EMA'] = list(map(lambda x: rec_EMA(300, x, risk), uni_var[7]))
    recom['DEMA'] = list(map(lambda x: rec_DEMA(300, x, risk), uni_var[7]))
    recom['TEMA'] = list(map(lambda x: rec_TEMA(300, x, risk), uni_var[7]))
    recom['MACD'] = list(map(lambda x: rec_MACD(300, x), uni_var[7]))
    recom['CHV'] = list(map(lambda x: rec_CHV(300, x, risk), uni_var[7]))
    recom['RSI'] = list(map(lambda x: rec_RSI(300, x, risk), uni_var[7]))
    recom['bulls'] = list(map(lambda x: rec_bulls(300, x, risk), uni_var[7]))
    recom['bears'] = list(map(lambda x: rec_bears(300, x, risk), uni_var[7]))
    recom['ER'] = list(map(lambda x: rec_ER(300, x, risk), uni_var[7]))
    recom['MI'] = list(map(lambda x: rec_MI(300, x), uni_var[7]))

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


def final_plot(period, stck, risk, x):
    t = period + 301
    data = yf.download(stck, start=datetime.date.today() - datetime.timedelta(days=t), end=datetime.date.today())
    if x == 1:
        return plot_SMA(period, data, risk)
    elif x == 2:
        return plot_twoSMA(period, data, risk)
    elif x == 3:
        return plot_EMA(period, data, risk)
    elif x == 4:
        return plot_DEMA(period, data, risk)
    elif x == 5:
        return plot_TEMA(period, data, risk)
    elif x == 6:
        return plot_MACD(period, data)
    elif x == 7:
        return plot_CHV(period, data, risk)
    elif x == 8:
        return plot_RSI(period, data, risk)
    elif x == 9:
        return plot_bulls(period, data, risk)
    elif x == 10:
        return plot_bears(period, data, risk)
    elif x == 11:
        return plot_ER(period, data, risk)
    else:
        return plot_MI(period, data)
