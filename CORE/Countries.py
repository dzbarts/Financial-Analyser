#https://www.starcapital.de/fileadmin/user_upload/files/publikationen/Kapitalmarktforschung/2020-04_KMF_Update_EN_www.html
#https://vse-dengy.ru/pro-investitsii/fondovye-koeffitsienty.html
#https://smart-lab.ru/blog/562256.php
#https://journal.tinkoff.ru/cape/

import yfinance as yf
import matplotlib.pyplot as plt

msft = yf.Ticker('MSFT')
aapl = yf.Ticker('AAPL')
tsla = yf.Ticker('TSLA')
yndx = yf.Ticker('YNDX')

portfolio = [msft, aapl, tsla, yndx]
countries = []
weight = []

for i in range(len(portfolio)):
    el = portfolio[i].info["country"]
    if el not in countries:
        countries.append(el)
        weight.append(1)
        print(countries, weight)
    else:
        weight[countries.index(el)] += 1
        print(countries, weight)

fig1, ax1 = plt.subplots()
ax1.pie(weight, labels=countries)
plt.show()