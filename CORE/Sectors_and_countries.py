import pandas as pd
import matplotlib.pyplot as plt


# sectors Pandas DataFrame
def set_t_port_sect(uni_var):
    t_port_sect = pd.DataFrame({
        'Stocks': uni_var[2],
        'Number': uni_var[4],
        'Countries': uni_var[9],
        'Sectors': uni_var[10]
    }, index=uni_var[2])
    return t_port_sect


def plot_s(uni_var):
    weight_for_plot_s = [0] * len(uni_var[11])

    # cycle of getting weight_for_plot_s
    for i in range(len(uni_var[4])):
        weight_for_plot_s[uni_var[11].index(uni_var[10][i])] += uni_var[4][i]

    fig_s, ax1 = plt.subplots()
    ax1.pie(weight_for_plot_s, labels=uni_var[11])
    plt.style.use('dark_background')
    fig_s.set_facecolor('#19232D')
    ax1.set_title('Share by Sectors')
    return fig_s


# pie plot for countries
def plot_c(uni_var):
    plt.style.use('dark_background')
    weight_for_plot_c = [0] * len(uni_var[12])

    # cycle of getting weight_for_plot_c
    for i in range(len(uni_var[4])):
        weight_for_plot_c[uni_var[12].index(uni_var[9][i])] += uni_var[4][i]

    fig_c, ax1 = plt.subplots()
    ax1.pie(weight_for_plot_c, labels=uni_var[12])
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

