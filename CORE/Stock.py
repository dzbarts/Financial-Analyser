import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib
import datetime

def get_stock(stock):
    return yf.Ticker(stock)


def plot_stock(stock, period):  # передаю не только период, но и акцию,
    # чтобы можно было выводить график по определенной акции
    plt.style.use('dark_background')
    fig_st, ax1 = plt.subplots()
    ax1.grid(linewidth=0.5, linestyle='--')
    ax1.plot(yf.download(stock, start=datetime.date.today() - datetime.timedelta(days=361),
                         end=datetime.date.today()).Close[-period:])
    ax1.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d/%m"))
    fig_st.set_facecolor('#19232D')  # меняю background графика
    ax1.set_xlabel('Date, d/m')
    ax1.set_ylabel('Price, $')
    ax1.set_title('Price of Stock')
    return fig_st
    # plt.show()


# show actions (dividends, splits)
def get_stock_actions(stock):
    stock_actions = stock.actions
    stock_actions = stock_actions.reset_index()
    return stock_actions


# show quarterly_financials
def get_stock_quarterly_financials(stock):
    stock_quarterly_financials = stock.quarterly_financials
    stock_quarterly_financials = stock_quarterly_financials.rename_axis('Quarterly financials')
    stock_quarterly_financials = stock_quarterly_financials.reset_index()
    return stock_quarterly_financials


# show quarterly_balance_sheet
def get_stock_quarterly_balance_sheet(stock):
    stock_quarterly_balance_sheet = stock.quarterly_balance_sheet
    stock_quarterly_balance_sheet = stock_quarterly_balance_sheet.rename_axis('Quarterly balance sheet')
    stock_quarterly_balance_sheet = stock_quarterly_balance_sheet.reset_index()
    return stock_quarterly_balance_sheet


# show quarterly_cashflow
def get_stock_quarterly_cashflow(stock):
    stock_quarterly_cashflow = stock.quarterly_cashflow
    stock_quarterly_cashflow = stock_quarterly_cashflow.rename_axis('Quarterly cashflow')
    stock_quarterly_cashflow = stock_quarterly_cashflow.reset_index()
    return stock_quarterly_cashflow


# show quarterly_earnings
def get_stock_quarterly_earnings(stock):
    stock_quarterly_earnings = stock.quarterly_earnings
    stock_quarterly_earnings = stock_quarterly_earnings.reset_index()
    return stock_quarterly_earnings


# show sustainability
def get_stock_sustainability(stock):
    stock_sustainability = stock.sustainability
    stock_sustainability = stock_sustainability.reset_index()
    return stock_sustainability


# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
def get_stock_isin(stock):
    return stock.isin


def get_list_of_stock(stock):
    data = yf.download(stock, start=datetime.date.today() - datetime.timedelta(days=361),
                         end=datetime.date.today())
    price = data['Close'][-1]
    date = datetime.date.today()
    gr1 = round(price - data['Close'][-2], 2)
    if gr1 > 0:
        gr1 = str('+' + gr1)
    else:
        gr1 = str(gr1)
    gr2 = round((price / data['Close'][-2] - 1) * 100, 2)
    gr2 = str(gr2) + '%'

    return str.upper(stock), round(price, 2), date, gr1, gr2

# import time
# start_time = time.time()
# print(get_list_of_stock('poly'))
# print("--- %s seconds ---" % (time.time() - start_time))