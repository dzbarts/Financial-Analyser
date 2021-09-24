import yfinance as yf

port = ['msft', 'msft', 'aapl', 'TSLA',
        'YNDX', 'RY', 'RY', 'RY', 'RY',
        'RY', 'SBER.ME', 'SBER.ME', 'SBER.ME']
portfolio = []

port = list(map(str.upper, port))
portfolio = list(map(yf.Ticker, port))

ticker = ['AFLT.ME', 'IMOEX.ME']
stock = yf.download(ticker)

# Выделение скорректированой цены закрытия
all_adj_close = stock[['Adj Close']]
#print(all_adj_close)
#print(stock[['Sector']])


# dividends = []
#
# for i in range(len(portfolio)):
#     el = portfolio[i].dividends
#     dividends.append(el)
#
# print(dividends)

# msft1 = yf.download('MSFT', period='1d')
# aapl1 = yf.download('AAPL', period='1d')
# tsla1 = yf.download('TSLA', period='1d')
# yndx1 = yf.download('YNDX', period='1d')
#
#
# value = 0
# port = [msft1, aapl1, tsla1, yndx1]
#
# for i in range(4):
#     value += port[i].Close
# print(round(float(value),2))
#

wallet = 10000

spent = 0

