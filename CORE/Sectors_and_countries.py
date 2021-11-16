import pandas as pd
import matplotlib.pyplot as plt


def get_sector(el):
    return el.info['sector']


def get_country(el):
    return el.info['country']


# sectors Pandas DataFrame
def set_t_port_sect(uni_var):
    list_of_all_countries = list(map(get_country, uni_var[3]))
    list_of_all_sectors = list(map(get_sector, uni_var[3]))

    t_port_sect = pd.DataFrame({
        'Stocks': uni_var[2],
        'Number': uni_var[4],
        'Countries': list_of_all_countries,
        'Sectors': list_of_all_sectors
    }, index=uni_var[2])
    return t_port_sect


def plot_s(uni_var):
    list_of_all_sectors = list(map(get_sector, uni_var[3]))

    list_of_sectors = list(set(list_of_all_sectors))

    weight_for_plot_s = [0] * len(list_of_sectors)

    # cycle of getting weight_for_plot_s
    for i in range(len(uni_var[4])):
        weight_for_plot_s[list_of_sectors.index(list_of_all_sectors[i])] += uni_var[4][i]

    fig_s, ax1 = plt.subplots()
    ax1.pie(weight_for_plot_s, labels=list_of_sectors)
    plt.style.use('dark_background')
    fig_s.set_facecolor('#19232D')
    ax1.set_title('Share by Sectors')
    return fig_s


# pie plot for countries
def plot_c(uni_var):
    plt.style.use('dark_background')
    list_of_all_countries = list(map(get_country, uni_var[3]))
    list_of_countries = list(set(list_of_all_countries))
    weight_for_plot_c = [0] * len(list_of_countries)

    # cycle of getting weight_for_plot_c
    for i in range(len(uni_var[4])):
        weight_for_plot_c[list_of_countries.index(list_of_all_countries[i])] += uni_var[4][i]

    fig_c, ax1 = plt.subplots()
    ax1.pie(weight_for_plot_c, labels=list_of_countries)
    fig_c.set_facecolor('#19232D')
    ax1.set_title('Share by Countries')
    return fig_c
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


# buying advice depending on the stage of the economic cycle
tsectors = pd.DataFrame({'Ранняя фаза': ['Financial Services', 'Real Estate',
                                         'Consumer Discretionary',
                                         'Technology',
                                         'Industrials', 'Materials', '',
                                         '"NEM", "AMZN", "BAC", "NKE"'],
                         'Средняя фаза': ['Technology', 'Communication Services',
                                          '', '', '', '', '',
                                          '"AAPL", "MSFT", "VZ", "CMCSA"'],
                         'Закат': ['Healthcare', 'Utilities',
                                   'Consumer Staples', '', '', '', '',
                                   '"JNJ", "AMGN", "PFE", "PG", "KO"'],
                         'Рецессия': ['Utilities', '', '', '', '', '', '',
                                      '"EXC", "DRE", "D", "NEE", "NG"']
                         }, index=['1', '2', '3', '4', '5', '6', '', 'Рекомендации'])

