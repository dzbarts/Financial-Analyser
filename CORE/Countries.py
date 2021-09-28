import pandas as pd
import matplotlib.pyplot as plt
from Portfolio import *


weight_portfolio = [0] * len(flatten_port)
countries = []
t_countries = []
weight = []


# function for column 'countries'
for i in range(len(flatten_port)):
    t_countries.append(flatten_portfolio[i].info['country'])
    # print(flatten_portfolio[i], flatten_portfolio[i].info['country'])


# main function
for i in range(len(portfolio)):
    el = portfolio[i].info['country']
    weight_portfolio[flatten_port.index(port[i])] += 1
    # print(weight_portfolio)
    if el not in countries:
        countries.append(el)
        weight.append(1)
        # print(countries, weight)
    else:
        weight[countries.index(el)] += 1
        # print(countries, weight)

# pli plot
# fig1, ax1 = plt.subplots()
# ax1.pie(weight, labels=countries)
# plt.show()

# CAPA index Pandas DataFrame
# index was taken on 6/30/21
tcapa = pd.DataFrame({'Nation': ['Canada', 'US', 'UK', 'Italy', 'Spain', 'Russia',
                                 'India', 'Japan', 'China', 'Hong Kong', 'Australia'],
                      'Calculated Using': ['S&P/TSX Composite', 'S&P', 'FTSE', 'FTSE MIB',
                                           'IBEX', 'MOEX', 'NIFTY', 'All public companies, (uncons.)',
                                           'SSE Composite', 'Hang Seng', 'ASX All Ordinaries'],
                      'Index': [25.49, 37.73, 15.05, 24.17, 18.22, 10.96, 33.38, 33.16, 18.43, 14.62, 19.83]
                      })


# recommendation function
def cape_advice():
    if max(weight) / sum(weight) >= 0.4 and \
            countries[weight.index(max(weight))] in \
            ['Canada', 'US', 'Italy', 'India', 'Japan']:
        return "It is recommended to invest in stocks of countries such as Russia, UK or China"
    else:
        return "Diversification by country according to CAPE is quite good"


# table below the graph
t_port_capa = pd.DataFrame({
    'Stocks': flatten_port,
    'Number': weight_portfolio,
    'Countries': t_countries
})
