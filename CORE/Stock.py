import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from Portfolio import *
import matplotlib

plt.style.use('seaborn')

stck = yf.Ticker('MSFT')

def plot_stock(period):
    fig, ax1 = plt.subplots()
    ax1.plot(yf.download('MSFT').Close[-period:])

    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    return fig


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
