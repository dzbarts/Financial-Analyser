import matplotlib.pyplot as plt
import numpy as np
import datetime as dt


# я обозначил дата за 0, тк не обозначать нельзя
# мне ее оставить пустой, чтобы она как глобальная переменная была,или добавить как аргумент?

# параметр n отвечает за покупку - продажу акций
# если n = 2 - покупать (SELL)
#      n = 1 - ничего (WAIT)
#      n = 0 - продавать (SELL)
#      n = 3 - не продавать (NSELL)
#      n = 4 - не покупать  (NBUY)
#      n = 5 - индикатор не против торговли (OK)
#      n = 6 - не торговать (NT)
from Indicators import EMA, SMA, DEMA, TEMA, RSI, MACD, Bulls_power, Bears_power, Elder_Rays, MI, CHV


def rec_SMA(lenData, data, risk=2):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50
    sma = SMA(data['Close'], window)

    sma = sma[(-lenData):]
    data = data[(-lenData):]

    if (data['Close'].values[-1] <= sma[-1] and data['Close'].values[-2] > sma[-2]):
        n = 0
    elif (data['Close'].values[-1] >= sma[-1] and data['Close'].values[-2] < sma[-2]):
        n = 2
    else:
        n = 1

    return n


def rec_twoSMA(lenData, data, risk=2):
    if risk == 1:  # низкий риск
        window1 = 70
        window2 = 140
    elif risk == 3:  # высокий риск
        window1 = 25
        window2 = 50
    else:  # средний риска
        window1 = 5
        window2 = 10

    smaShort = SMA(data['Close'], window1)
    smaLong = SMA(data['Close'], window2)

    smaShort = smaShort[(-lenData):]
    smaLong = smaLong[(-lenData):]
    data = data[(-lenData):]

    if (smaShort[-1] <= smaLong[-1] and smaShort[-2] > smaLong[-2]):
        n = 0
    elif (smaShort[-1] >= smaLong[-1] and smaShort[-2] < smaLong[-2]):
        n = 2
    else:
        n = 1

    return n



def rec_EMA(lenData, data, risk=2):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    ema = EMA(data['Close'], window)

    ema = ema[(-lenData):]
    data = data[(-lenData):]

    if (data['Close'].values[-1] <= ema[-1] and data['Close'].values[-2] > ema[-2]):
        n = 0
    elif (data['Close'].values[-1] >= ema[-1] and data['Close'].values[-2] < ema[-2]):
        n = 2
    else:
        n = 1

    return n



def rec_DEMA(lenData, data, risk=2):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    dema = DEMA(data['Close'], window)

    dema = dema[(-lenData):]
    data = data[(-lenData):]

    if (data['Close'].values[-1] <= dema[-1] and data['Close'].values[-2] > dema[-2]):
        n = 0
    elif (data['Close'].values[-1] >= dema[-1] and data['Close'].values[-2] < dema[-2]):
        n = 2
    else:
        n = 1

    return n


def rec_TEMA(lenData, data, risk=2):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    tema = TEMA(data['Close'], window)

    tema = tema[(-lenData):]
    data = data[(-lenData):]

    if (data['Close'].values[-1] <= tema[-1] and data['Close'].values[-2] > tema[-2]):
        n = 0
    elif (data['Close'].values[-1] >= tema[-1] and data['Close'].values[-2] < tema[-2]):
        n = 2
    else:
        n = 1

    return n


def rec_RSI(lenData, data, risk=2):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    rsi = RSI(data['Close'], window)

    rsi = rsi[(-lenData):]
    data = data[(-lenData):]

    if rsi[-1] > 70:
        n = 4
    elif rsi[-1] < 30:
        n = 3
    else:
        n = 5

    return n


def rec_MACD(lenData, data, risk=1):
    if risk == 1:  # низкий риск
        shortwindow = 12
        longwindow = 26
        signalwindow = 9
    else:  # высокий риск
        shortwindow = 5
        longwindow = 35
        signalwindow = 5

    macd_all = MACD(data['Close'], shortwindow, longwindow, signalwindow)

    macd = macd_all[0]
    macdsignal = macd_all[1]
    macdhist = macd_all[2]

    macd = macd[(-lenData):]
    macdsignal = macdsignal[(-lenData):]
    macdhist = macdhist[(-lenData):]
    data = data[(-lenData):]

    if (macdhist[-1] <= macdsignal[-1] and macdhist[-2] > macdsignal[-2]):
        n = 0
    elif (macdhist[-1] >= macdsignal[-1] and macdhist[-2] < macdsignal[-2]):
        n = 2
    else:
        n = 1

    return n


def rec_bulls(lenData, data, risk=2):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    bulls = Bulls_power(data, window)

    bulls = bulls[(-lenData):]
    data = data[(-lenData):]

    if (bulls.values[-1] < bulls.values[-2] and bulls.values[-1] > 0 and bulls.values[-2] > 0):
        n = 3
    else:
        n = 5

    return n


def rec_bears(lenData, data, risk=2):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    bears = Bears_power(data, window);

    bears = bears[(-lenData):]
    data = data[(-lenData):]

    if (bears.values[-1] > bears.values[-2] and bears.values[-1] < 0 and bears.values[-2] < 0):
        n = 4
    else:
        n = 5

    return n


def rec_ER(lenData, data, risk=2):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    ema = Elder_Rays(data, window)[0]
    bulls = Elder_Rays(data, window)[1]
    bears = Elder_Rays(data, window)[2]

    ema = ema[(-lenData):]
    bears = bears[(-lenData):]
    bulls = bulls[(-lenData):]
    data = data[(-lenData):]

    if (bears.values[-1] > bears.values[-2] and bears.values[-1] < 0 and bears.values[-2] < 0):
        n = 4
    elif (bulls.values[-1] < bulls.values[-2] and bulls.values[-1] > 0 and bulls.values[-2] > 0):
        n = 3
    else:
        n = 5

    return n


def rec_MI(lenData, data):
    mi = MI(data, 9)

    result = []
    for i in range(len(mi) - 49):
        result.append(sum(mi[i + 25:i + 50]))

    mi = result

    mi = mi[(-lenData):]
    data = data[(-lenData):]

    mislice = mi[-20:-1]
    flag = 6

    for i in range(len(mislice)):
        if (mi[i] > 26.5 and mi[i] < 27):
            flag = 5

    if (flag == 5 and mi[-1] < 26.5):
        n = 5
    else:
        n = 6

    return n


def rec_CHV(lenData, data, risk=2):
    if risk == 1:
        window = 100  # низкий риск
    elif risk == 3:  # высокий риск
        window = 10
    else:  # средний риска
        window = 50

    chv = CHV(data, window)

    chv = chv[(-lenData):]
    data = data[(-lenData):]

    if all(chv[i - 1] <= chv[i] for i in range(10)):
        n = 2
    elif all(chv[i - 1] >= chv[i] for i in range(10)):
        n = 0
    else:
        n = 1

    return n