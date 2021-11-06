import math

import pandas as pd
import yfinance as yf
from Portfolio import *
from Indicators import *
from Plots import *

def set_recom(risk):
    recom = pd.DataFrame()
    recom['Stocks'] = flatten_port
    recom['SMA'] = list(map(lambda x: plot_SMA(300, x, risk)[0], stock))
    recom['twoSMA'] = list(map(lambda x: plot_twoSMA(300, x, risk)[0], stock))
    recom['EMA'] = list(map(lambda x: plot_EMA(300, x, risk)[0], stock))
    recom['DEMA'] = list(map(lambda x: plot_DEMA(300, x, risk)[0], stock))
    recom['TEMA'] = list(map(lambda x: plot_TEMA(300, x, risk)[0], stock))
    recom['MACD'] = list(map(lambda x: plot_MACD(300, x)[0], stock))
    recom['CHV'] = list(map(lambda x: plot_CHV(300, x, risk)[0], stock))
    recom['RSI'] = list(map(lambda x: plot_RSI(300, x, risk)[0], stock))
    recom['bulls'] = list(map(lambda x: plot_bulls(300, x, risk)[0], stock))
    recom['bears'] = list(map(lambda x: plot_bears(300, x, risk)[0], stock))
    recom['ER'] = list(map(lambda x: plot_ER(300, x, risk)[0], stock))
    recom['MI'] = list(map(lambda x: plot_MI(300, x)[0], stock))

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
