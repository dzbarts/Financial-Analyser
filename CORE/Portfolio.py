import yfinance as yf


def set_port_and_portfolio(port):
    port = list(map(str.upper, port))
    portfolio = list(map(yf.Ticker, port))
    flatten_port = list(set(port))
    flatten_portfolio = list(map(yf.Ticker, flatten_port))
    stock = list(map(yf.download, flatten_port))
    length_of_flatten_port = len(flatten_port)
    length_of_stock = len(stock)
    weight_of_stocks = []

    for i in range(len(flatten_port)):
        weight_of_stocks.append((port.count(flatten_port[i])))

    return port, portfolio, flatten_port,\
           flatten_portfolio, weight_of_stocks,\
           length_of_flatten_port, length_of_stock, stock
