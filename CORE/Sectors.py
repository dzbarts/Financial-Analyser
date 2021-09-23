import yfinance as yf
import matplotlib.pyplot as plt

msft = yf.Ticker('MSFT')
aapl = yf.Ticker('AAPL')
tsla = yf.Ticker('TSLA')
yndx = yf.Ticker('YNDX')

portfolio = [msft, aapl, tsla, yndx]
sectors = []
weight = []

for i in range(len(portfolio)):
    el = portfolio[i].info['sector']
    if el not in sectors:
        sectors.append(el)
        weight.append(1)
        print(sectors, weight)
    else:
        weight[sectors.index(el)] += 1
        print(sectors, weight)

fig1, ax1 = plt.subplots()
ax1.pie(weight, labels=sectors)
plt.show()