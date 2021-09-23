import pandas as pd
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
