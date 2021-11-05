import pandas as pd
import matplotlib.pyplot as plt
from Portfolio import *
from Countries import *

plt.style.use('seaborn')


def get_sector(el):
    return el.info['sector']


# some base variants
list_of_all_sectors = list(map(get_sector, flatten_portfolio))
list_of_sectors = list(set(list_of_all_sectors))

weight_for_plot_s = [0] * len(list_of_sectors)

# sectors Pandas DataFrame
t_port_sect = pd.DataFrame({
    'Stocks': flatten_port,
    'Number': weight_of_stocks,
    'Sectors': list_of_all_sectors,
    'Countries': list_of_all_countries
})

# cycle of getting weight_for_plot_s
for i in range(len(weight_of_stocks)):
    weight_for_plot_s[list_of_sectors.index(list_of_all_sectors[i])] += weight_of_stocks[i]

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
                                   'Товары первой необходимости', '', '', '', '',
                                   '"JNJ", "AMGN", "PFE", "PG", "KO"'],
                         'Рецессия': ['Коммунальные услуги', '', '', '', '', '', '',
                                      '"EXC", "DRE", "D", "NEE", "NG"']
                         }, index=['1', '2', '3', '4', '5', '6', '', 'Рекомендации'])


def plot_s():
    fig_s, ax1 = plt.subplots()
    ax1.pie(weight_for_plot_s, labels=list_of_sectors)
    fig_s.set_facecolor('#19232D')
    return fig_s