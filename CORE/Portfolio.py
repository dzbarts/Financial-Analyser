import yfinance as yf
import matplotlib.pyplot as plt

port = ['msft', 'msft', 'aapl', 'TSLA',
        'YNDX', 'RY', 'RY', 'RY', 'RY',
        'RY', 'SBER.ME', 'SBER.ME', 'SBER.ME']
portfolio = []

port = list(map(str.upper, port))
portfolio = list(map(yf.Ticker, port))



stock = list(map(yf.download, port))
stock1 = list(map(yf.Ticker, port))

# print(stock)
sum = 0
for i in range(len(port)):
    sum += stock[i].Close[-1]
sum = round(float(sum), 2)
print(sum)


def plot_common(period):
    for i in range(len(stock)):
        plt.plot(stock[i].Close[-period:])

    plt.show()


plot_common(200)

# Выделение скорректированой цены закрытия
# all_adj_close = stock[['Adj Close']]
# print(all_adj_close)
# print(stock[['Sector']])


# dividends = []
#
# for i in range(len(portfolio)):
#     el = portfolio[i].dividends
#     dividends.append(el)
#
# print(dividends)
