import math

from DATA.tradeBot_parser_static import get_quotes_list
import Indicators


# window from 200 for better result
# dt.datetime(2020, 5, 1)
def Strategy_SMA(ticker, start, end, capital, window):
    global lastI
    data = get_quotes_list(ticker, start, end)
    lengthOfData = len(data)

    startUpCapital = capital
    amountOfStocks = 0

    sma = Indicators.SMA(data, window)

    for i in range(lengthOfData - 1):

        # sell
        if (sma[i + 1] >= data[i + 1] and sma[i] < data[i]):
            if (i < lengthOfData - 2 and amountOfStocks != 0):
                capital += amountOfStocks * data[i + 2]
                amountOfStocks = 0

        # buy
        if (sma[i + 1] <= data[i + 1] and sma[i] > data[i]):
            if capital >= data[i + 1]:
                amountOfStocks = math.floor(capital / data[i + 1])
                capital -= amountOfStocks * data[i + 1]
                lastI = i + 1
    totalCapital = capital + amountOfStocks * data[lastI]

    print(f'start-up capital = {startUpCapital}\ntotal capital = {totalCapital}')
    return


def Strategy_byeAndHold(ticker, start, end, capital):
    data = get_quotes_list(ticker, start, end)
    lengthOfData = len(data)

    startUpCapital = capital
    amountOfStocks = math.floor(capital / data[0])
    capital -= amountOfStocks * data[0]

    for i in range(lengthOfData - 1):

        if data[i + 1] > data[0]:
            capital += amountOfStocks * data[i + 1]
            break

    print(f'start-up capital = {startUpCapital}\ntotal capital = {capital}')


def Strategy_twoSMA(ticker, start, end, capital):
    global lastI
    data = get_quotes_list(ticker, start, end)
    lengthOfData = len(data)

    startUpCapital = capital
    amountOfStocks = math.floor(capital / data[0])
    startUpAmountOfStocks = amountOfStocks
    capital -= amountOfStocks * data[0]
    startCapitalAfterBuy = capital

    smaShort = Indicators.SMA(data, 70)
    smaLong = Indicators.SMA(data, 140)

    for i in range(lengthOfData - 1):

        # sell
        if (smaLong[i + 1] >= smaShort[i + 1] and smaLong[i] < smaShort[i]):
            if i < lengthOfData - 2:
                capital += amountOfStocks * data[i + 2]
                amountOfStocks = 0

        # buy
        if (smaLong[i + 1] <= smaShort[i + 1] and smaLong[i] > smaShort[i]):
            if capital >= data[i + 1]:
                amountOfStocks = math.floor(capital / data[i + 1])
                capital -= amountOfStocks * data[i + 1]
                lastI = i + 1
    totalCapital = capital + amountOfStocks * data[lastI]

    print(f'start-up capital = {startUpCapital}\ntotal capital = {totalCapital}')
    print(f'there were {startUpAmountOfStocks} stocks and {startCapitalAfterBuy} rubles at the start')
    print(f'became {amountOfStocks} stocks and {capital} rubles at the end')


def Strategy_EMA(ticker, start, end, capital):
    data = get_quotes_list(ticker, start, end)
    lengthOfData = len(data)

    startUpCapital = capital
    amountOfStocks = math.floor(capital / data[0])
    startUpAmountOfStocks = amountOfStocks
    capital -= amountOfStocks * data[0]
    startCapitalAfterBuy = capital

    ema5 = Indicators.EMA(data, 5)
    ema10 = Indicators.EMA(data, 10)
    ema = Indicators.EMA(data, 90)

    for i in range(lengthOfData - 1):

        # sell
        if (ema10[i + 1] >= ema5[i + 1] and ema10[i] < ema5[i] and ema[i + 1] < data[i + 1]):
            if i < lengthOfData - 2:
                capital += amountOfStocks * data[i + 2]
                amountOfStocks = 0

        # buy
        if (ema10[i + 1] <= ema5[i + 1] and ema10[i] > ema5[i] and ema[i + 1] > data[i + 1]):
            if capital >= data[i + 1]:
                amountOfStocks = math.floor(capital / data[i + 1])
                capital -= amountOfStocks * data[i + 1]
                lastI = i + 1
    totalCapital = capital + amountOfStocks * data[lastI]

    print(f'start-up capital = {startUpCapital}\ntotal capital = {totalCapital}')
    print(f'there were {startUpAmountOfStocks} stocks and {startCapitalAfterBuy} rubles at the start')
    print(f'became {amountOfStocks} stocks and {capital} rubles at the end')