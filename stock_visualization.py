import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

days = 20
tickers = {
    'apple': 'AAPL',
    'Meta': 'META',
    'MicroSoft': 'msft',
    'google': 'GOOGL',
    'Netflix': 'NFLX',
    'Amazon': 'AMZN'
}

def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'NAME'
        df = pd.concat([df, hist])
    return df
  
  days = 20
tickers = {
    'apple': 'AAPL',
    'Meta': 'META',
    'MicroSoft': 'msft',
    'google': 'GOOGL',
    'Netflix': 'NFLX',
    'Amazon': 'AMZN'
}

get_data(days, tickers)
