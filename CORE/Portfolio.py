import yfinance as yf
import datetime


def get_sector(el):
    return el.info['sector']


def get_country(el):
    return el.info['country']


def get_yfinance_download(ticker):
    return yf.download(ticker, start=datetime.date.today() - datetime.timedelta(days=361), end=datetime.date.today())


def set_port_and_portfolio(port):
    port = list(map(str.upper, port))
    # portfolio = list(map(yf.Ticker, port))
    portfolio = 0
    flatten_port = list(set(port))
    flatten_portfolio = list(map(yf.Ticker, flatten_port))
    stock = list(map(get_yfinance_download, flatten_port))
    length_of_flatten_port = len(flatten_port)
    length_of_stock = len(stock)
    weight_of_stocks = []

    for i in range(len(flatten_port)):
        weight_of_stocks.append((port.count(flatten_port[i])))

    dividends = []
    for i in range(length_of_flatten_port):
        dividends.append(flatten_portfolio[i].info['dividendRate'])

    list_of_all_countries = list(map(get_country, flatten_portfolio))
    list_of_all_sectors = list(map(get_sector, flatten_portfolio))
    list_of_sectors = list(set(list_of_all_sectors))
    list_of_countries = list(set(list_of_all_countries))

    return port, portfolio, flatten_port,\
           flatten_portfolio, weight_of_stocks,\
           length_of_flatten_port, length_of_stock,\
           stock, dividends, list_of_all_countries,\
           list_of_all_sectors, list_of_sectors, list_of_countries
