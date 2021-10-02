import pandas as pd
import matplotlib.pyplot as plt
from Portfolio import *


def get_sector(el):
    return el.info['sector']


list_of_all_sectors = list(map(get_sector, flatten_portfolio))
list_of_sectors = list(set(list_of_all_sectors))

weight_for_plot_s = [0] * len(list_of_sectors)


t_port_sect = pd.DataFrame({
    'Stocks': flatten_port,
    'Number': weight_of_stocks,
    'Sectors': list_of_all_sectors
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
                                'Товары первой необходимости', '', '', '','',
                                '"JNJ", "AMGN", "PFE", "PG", "KO"'],
                      'Рецессия': ['Коммунальные услуги', '', '', '', '', '', '',
                                   '"EXC", "DRE", "D", "NEE", "NG"']
                      })


def plot_s():
    fig1, ax1 = plt.subplots()
    ax1.pie(weight_for_plot_s, labels=list_of_sectors)
    plt.show()