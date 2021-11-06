import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from Portfolio import *
import matplotlib

plt.style.use('seaborn')

stck = yf.Ticker('MSFT')

def plot_stock(stock, period):  # передаю не только период, но и акцию,
    # чтобы можно было выводить график по определенной акции
    fig_st, ax1 = plt.subplots()
    ax1.plot(yf.download(stock).Close[-period:])
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    fig_st.set_facecolor('#19232D')  # меняю background графика
    return fig_st
    #plt.show()


# show actions (dividends, splits)
stck_actions = stck.actions
stck_actions = stck_actions.reset_index()


# show quarterly_financials
stck_quarterly_financials = stck.quarterly_financials
stck_quarterly_financials = stck_quarterly_financials.rename_axis('Quarterly financials')
stck_quarterly_financials = stck_quarterly_financials.reset_index()


# show quarterly_balance_sheet
stck_quarterly_balance_sheet = stck.quarterly_balance_sheet
stck_quarterly_balance_sheet = stck_quarterly_balance_sheet.rename_axis('Quarterly balance sheet')
stck_quarterly_balance_sheet = stck_quarterly_balance_sheet.reset_index()


# show quarterly_cashflow
stck_quarterly_cashflow = stck.quarterly_cashflow
stck_quarterly_cashflow = stck_quarterly_cashflow.rename_axis('Quarterly cashflow')
stck_quarterly_cashflow = stck_quarterly_cashflow.reset_index()


# show quarterly_earnings
stck_quarterly_earnings = stck.quarterly_earnings
stck_quarterly_earnings = stck_quarterly_earnings.reset_index()


# show sustainability
stck_sustainability = stck.sustainability
stck_sustainability = stck_sustainability.reset_index()


# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
stck_isin = stck.isin
