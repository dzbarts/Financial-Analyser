import pandas as pd
import matplotlib.pyplot as plt
from CORE.Portfolio import *


flatten_port = list(set(port))
flatten_portfolio = list(map(yf.Ticker, flatten_port))
sectors = []
t_sectors = []
weight_portfolio = [0] * len(flatten_port)


# function for column 'sectors'
for i in range(len(flatten_port)):
    el = flatten_portfolio[i].info['sector']
    t_sectors.append(el)
    # print(el)
    if el not in sectors:
        sectors.append(el)
        # print(flatten_portfolio[i], flatten_portfolio[i].info['sector'])


weight = [0] * len(sectors)


# function for weights
for i in range(len(portfolio)):
    el = portfolio[i].info['sector']
    weight[sectors.index(el)] += 1
    weight_portfolio[flatten_port.index(port[i])] += 1
    # print(weight_portfolio)


# pie plot
fig1, ax1 = plt.subplots()
ax1.pie(weight, labels=sectors)
plt.show()


# buying advice depending on the stage of the economic cycle
tsectors = pd.DataFrame({'Ранняя фаза': ['Финансы', 'Недвижимость',
                                      'Товары второй необходимости',
                                      'Информационные технологии',
                                      'Промышленность, логистика', 'Сырье', '',
                                         '"NEM", "AMZN", "BAC", "SBER", "NKE"'],
                      'Средняя фаза': ['IT-сфера', 'Услуги телекоммуникации и связи',
                                       '', '', '', '', '',
                                       '"AAPL", "MSFT", "MA", "VZ", "CMCSA"'],
                      'Закат': ['Здравоохранение', 'Коммунальные услуги',
                                'Товары первой необходимости', '', '', '','',
                                '"JNJ", "AMGN", "PFE", "PG", "KO"'],
                      'Рецессия': ['Коммунальные услуги', '', '', '', '', '', '',
                                   '"EXC", "DRE", "D", "NEE", "NG"']
                      })


# table below the graph
t_port_sect = pd.DataFrame({
    'Stocks': flatten_port,
    'Number': weight_portfolio,
    'Sectors': t_sectors
})

# for show
print(tsectors)
print(t_port_sect)