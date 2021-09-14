import math
import pandas_datareader as web
import datetime as dt


# usually close data

# Simple moving average
# https://en.wikipedia.org/wiki/Moving_average
def SMA(data, period):
    if len(data) == 0:
        raise Exception("Empty data")
    if period <= 0:
        raise Exception("Invalid period")

    interm = 0
    result = []
    for i, v in enumerate(data):
        interm += v
        if (i + 1) < period:
            result.append(math.nan)
        else:
            result.append(interm / float(period))
            interm -= data[i + 1 - period]
    return result


# Exponential moving average
# https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average
def EMA(data, period):
    if period <= 1:
        raise Exception("Invalid period")

    sma = SMA(data, period)
    multiplier = 2 / (float(period + 1))
    result = []

    for k, v in enumerate(sma):
        if math.isnan(v):
            result.append(math.nan)
        else:
            prev = result[k - 1]
            if math.isnan(prev):
                result.append(v)
                continue
            ema = (data[k] - prev) * multiplier + prev
            result.append(ema)
    return result


# Moving average convergence/divergence
# https://en.wikipedia.org/wiki/MACD
# usually take 12,26,9, but u can take 5,35,5 for more risky trading
def MACD(data, shortperiod, longperiod, signalperiod):
    macd, macdsignal, macdhist = [], [], []

    short_ema = EMA(data, shortperiod)
    long_ema = EMA(data, longperiod)

    diff = []

    for k, short in enumerate(short_ema):
        if math.isnan(short) or math.isnan(long_ema[k]):
            macd.append(math.nan)
            macdsignal.append(math.nan)
        else:
            macd.append(short - long_ema[k])
            diff.append(macd[k])

    diff_ema = EMA(diff, signalperiod)
    macdsignal += diff_ema

    for k, ms in enumerate(macdsignal):
        if math.isnan(ms) or math.isnan(macd[k]):
            macdhist.append(math.nan)
        else:
            macdhist.append(macd[k] - macdsignal[k])

    return macd, macdsignal, macdhist


# Relative strength index
# https://en.wikipedia.org/wiki/Relative_strength_index
def RSI(data, period):
    u_days = []
    d_days = []

    for i, _ in enumerate(data):
        if i == 0:
            u_days.append(0)
            d_days.append(0)
        else:
            if data[i] > data[i - 1]:
                u_days.append(data[i] - data[i - 1])
                d_days.append(0)
            elif data[i] < data[i - 1]:
                d_days.append(data[i - 1] - data[i])
                u_days.append(0)
            else:
                u_days.append(0)
                d_days.append(0)

    ema_u = EMA(u_days, period)
    ema_d = EMA(d_days, period)

    result = []

    for k, _ in enumerate(data):
        if ema_d[k] == 0:
            result.append(100)
        else:
            result.append(100 - (100 / (1 + ema_u[k] / ema_d[k])))

    return result


# Double Exponential Moving Average
# https://en.wikipedia.org/wiki/Exponential_smoothing#Double_exponential_smoothing
def DEMA(data, period):
    ema = EMA(data, period)
    ema_slice = ema[(period - 1):]
    ema2 = EMA(ema_slice, period)
    ema2 = [math.nan] * (period - 1) + ema2
    e2 = list(map(lambda x: x * 2, ema))

    result = []

    for i in range(len(data)):
        result.append(e2[i] - ema2[i])
    return result


# Triple Exponential Moving Average
def TEMA(data, period):
    e1 = EMA(data, period)
    e1_slice = e1[(period - 1):]
    e2 = EMA(e1_slice, period)
    e2_slice = e2[(period - 1):]
    e3 = EMA(e2_slice, period)
    e2 = [math.nan] * (period - 1) + e2
    e3 = [math.nan] * 2 * (period - 1) + e3

    e1 = list(map(lambda x: x * 3, e1))
    e2 = list(map(lambda x: x * 3, e2))

    result = []
    for i in range(len(data)):
        result.append(e1[i] - e2[i] + e3[i])

    return result


def Bulls_power(data, period):
    result = data['High'] - EMA(data['Close'], period)
    return result


def Bears_power(data, period):
    result = data['Low'] - EMA(data['Close'], period)
    return result


def Elder_Rays(data, period):
    ema = EMA(data['Close'], period)
    bulls = Bulls_power(data, period)
    bears = Bears_power(data, period)
    return ema, bulls, bears


# https://ru.wikipedia.org/wiki/Индекс_массы_(технический_анализ)
def MI(data, period):
    dataHL = data['High'] - data['Low']
    ema = EMA(dataHL, period)
    dema = DEMA(dataHL, period)
    result = []

    for i in range(len(dataHL)):
        result.append(ema[i] / dema[i])
    return result


# Индикатор волатильности Чайкина
# https://equity.today/indikator-volatilnosti-chajkina.html
def CHV(data, period):
    dataHL = data['High'] - data['Low']
    ema = EMA(dataHL, period)
    result = []

    for i in range(len(dataHL) - period):
        result.append((ema[i + period] - ema[i]) / ema[i] * 100)
    return result