import pandas as pd
import matplotlib.pyplot as plt
from Portfolio import *


def get_country(el):
    return el.info['country']


list_of_all_countries = list(map(get_country, flatten_portfolio))
list_of_countries = list(set(list_of_all_countries))

weight_for_plot_c = [0] * len(list_of_countries)

t_port_capa = pd.DataFrame({
    'Stocks': flatten_port,
    'Number': weight_of_stocks,
    'Countries': list_of_all_countries
})

# CAPA index Pandas DataFrame
# index was taken on 6/30/21
tcapa = pd.DataFrame({'Nation': ['Canada', 'US', 'UK', 'Italy', 'Spain', 'Russia',
                                 'India', 'Japan', 'China', 'Hong Kong', 'Australia'],
                      'Calculated Using': ['S&P/TSX Composite', 'S&P', 'FTSE', 'FTSE MIB',
                                           'IBEX', 'MOEX', 'NIFTY', 'All public companies, (uncons.)',
                                           'SSE Composite', 'Hang Seng', 'ASX All Ordinaries'],
                      'Index': [25.49, 37.73, 15.05, 24.17, 18.22, 10.96, 33.38, 33.16, 18.43, 14.62, 19.83]
                      })

# cycle of getting weight_for_plot_c
for i in range(len(weight_of_stocks)):
    weight_for_plot_c[list_of_countries.index(list_of_all_countries[i])] += weight_of_stocks[i]


# pie plot for countries
def plot_c():
    fig1, ax1 = plt.subplots()
    ax1.pie(weight_for_plot_c, labels=list_of_countries)
    plt.show()