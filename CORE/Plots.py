import matplotlib.pyplot as plt
import matplotlib
from pandas import Series
from Indicators import *


def plot_SMA(lenData, data, risk=2, st=0):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    data = data[7][st]['Close']
    data = Series.to_list(data)

    sma = SMA(data, window)
    sma = sma[(-lenData):]

    data = data[(-lenData):]

    plt.style.use('dark_background')
    fig_c, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    ax1.plot(data)
    ax1.plot(sma)
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Price, $')
    ax1.set_title('SMA Strategy')
    fig_c.set_facecolor('#19232D')
    return fig_c


def plot_twoSMA(lenData, data, risk=2, st=0):
    if risk == 1:  # низкий риск
        window1 = 70
        window2 = 140
    elif risk == 3:  # высокий риск
        window1 = 25
        window2 = 50
    else:  # средний риска
        window1 = 5
        window2 = 10

    data = data[7][st]['Close']
    data = Series.to_list(data)

    smaShort = SMA(data, window1)
    smaLong = SMA(data, window2)
    smaShort = smaShort[(-lenData):]
    smaLong = smaLong[(-lenData):]
    data = data[(-lenData):]

    plt.style.use('dark_background')
    fig_c, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    ax1.plot(data)
    ax1.plot(smaShort)
    ax1.plot(smaLong)
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Price, $')
    ax1.set_title('twoSMA Strategy')
    fig_c.set_facecolor('#19232D')
    return fig_c


def plot_EMA(lenData, data, risk=2, st=0):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    data = data[7][st]['Close']
    data = Series.to_list(data)

    ema = EMA(data, window)
    ema = ema[(-lenData):]

    data = data[(-lenData):]

    plt.style.use('dark_background')
    fig_c, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    ax1.plot(data)
    ax1.plot(ema)
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Price, $')
    ax1.set_title('EMA Strategy')
    fig_c.set_facecolor('#19232D')
    return fig_c


def plot_DEMA(lenData, data, risk=2, st=0):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    data = data[7][st]['Close']
    data = Series.to_list(data)

    dema = DEMA(data, window)
    dema = dema[(-lenData):]

    data = data[(-lenData):]

    plt.style.use('dark_background')
    fig_c, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    ax1.plot(data)
    ax1.plot(dema)
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Price, $')
    ax1.set_title('DEMA Strategy')
    fig_c.set_facecolor('#19232D')
    return fig_c


def plot_TEMA(lenData, data, risk=2, st=0):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    data = data[7][st]['Close']
    data = Series.to_list(data)

    tema = TEMA(data, window)
    tema = tema[(-lenData):]

    data = data[(-lenData):]

    plt.style.use('dark_background')
    fig_c, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    ax1.plot(data)
    ax1.plot(tema)
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Price, $')
    ax1.set_title('TEMA Strategy')
    fig_c.set_facecolor('#19232D')
    return fig_c


def plot_RSI(lenData, data, risk=2, st=0):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    data = data[7][st]['Close']
    data = Series.to_list(data)

    rsi = RSI(data, window)
    rsi = rsi[(-lenData):]

    data = data[(-lenData):]

    plt.style.use('dark_background')
    fig_c, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    ax1.plot([30] * len(data))
    ax1.plot([70] * len(data))
    ax1.plot(rsi)
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Index, unit')
    ax1.set_title('RSI Strategy')
    fig_c.set_facecolor('#19232D')
    return fig_c


def plot_MACD(lenData, data, risk=2, st=0):
    if risk == 1:  # низкий риск
        shortwindow = 12
        longwindow = 26
        signalwindow = 9
    else:  # высокий риск
        shortwindow = 5
        longwindow = 35
        signalwindow = 5

    date = data[7][st].index[(-lenData):]
    data = data[7][st]['Close']
    data = Series.to_list(data)

    macd_all = MACD(data, shortwindow, longwindow, signalwindow)

    macd = macd_all[0]
    macdsignal = macd_all[1]
    macdhist = macd_all[2]

    macd = macd[(-lenData):]
    macdsignal = macdsignal[(-lenData):]
    macdhist = macdhist[(-lenData):]

    plt.style.use('dark_background')
    fig_c, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    ax1.bar(date, macd)
    ax1.bar(date, macdhist, color='#F5D27A')
    ax1.plot(date, macdsignal, color='#F2EEAC')
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Index, unit')
    ax1.set_title('MACD Strategy')
    fig_c.set_facecolor('#19232D')
    return fig_c


def plot_bulls(lenData, data, risk=2, st=0):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    date = data[7][st].index[(-lenData):]
    data = data[7][st]

    bulls = Bulls_power(data, window)

    bulls = bulls[(-lenData):]
    # data = data['Close'][(-lenData):]

    plt.style.use('dark_background')
    fig_c, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    # ax1.plot(date, data)
    ax1.bar(date, bulls)
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Index, unit')
    ax1.set_title('Bulls Strategy')
    fig_c.set_facecolor('#19232D')
    return fig_c


def plot_bears(lenData, data, risk=2, st=0):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    date = data[7][st].index[(-lenData):]
    data = data[7][st]

    bears = Bears_power(data, window);

    bears = bears[(-lenData):]
    # data = data['Close'][(-lenData):]

    plt.style.use('dark_background')
    fig_c, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    # ax1.plot(date, data)
    ax1.bar(date, bears)
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Index, unit')
    ax1.set_title('Bears Strategy')
    fig_c.set_facecolor('#19232D')
    return fig_c


def plot_ER(lenData, data, risk=2, st=0):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    date = data[7][st].index[(-lenData):]
    data = data[7][st]

    er = Elder_Rays(data, window)
    ema = er[0]
    bulls = er[1]
    bears = er[2]

    # ema = ema[(-lenData):]
    bears = bears[(-lenData):]
    bulls = bulls[(-lenData):]

    plt.style.use('dark_background')
    fig_c, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    ax1.bar(date, bulls)
    ax1.bar(date, bears)
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Index, unit')
    ax1.set_title('Elder Rays Strategy')
    fig_c.set_facecolor('#19232D')
    return fig_c


def plot_MI(lenData, data, risk=2, st=0):
    date = data[7][st].index[(-lenData):]
    data = data[7][st]

    mi = MI(data, 9)

    result = []
    for i in range(len(mi) - 49):
        result.append(sum(mi[i + 25:i + 50]))

    mi = result

    mi = mi[(-lenData):]

    plt.style.use('dark_background')
    fig_c, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    ax1.plot(date, [27] * lenData)
    ax1.plot(date, [26.5] * lenData)
    ax1.plot(date, mi)
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Index, unit')
    ax1.set_title('Mass Index Strategy')
    fig_c.set_facecolor('#19232D')
    return fig_c


def plot_CHV(lenData, data, risk=2, st=0):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    date = data[7][st].index[(-lenData):]
    data = data[7][st]

    chv = CHV(data, window)
    chv = chv[(-lenData):]

    data = data['Close'][(-lenData):]

    plt.style.use('dark_background')
    fig_c, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    ax1.plot(date, data)
    ax1.plot(date, chv)
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Index/Price, unit/$')
    ax1.set_title('Chaikin Volatility Strategy')
    fig_c.set_facecolor('#19232D')
    return fig_c
