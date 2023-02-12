import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import altair as alt

days = 20
tickers = {
    'Apple': 'AAPL',
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
  
days = 30
tickers = {
    'Apple': 'AAPL',
    'Meta': 'META',
    'MicroSoft': 'msft',
    'google': 'GOOGL',
    'Netflix': 'NFLX',
    'Amazon': 'AMZN'
}

stock_data = pd.DataFrame(get_data(days, tickers))
stock_data = stock_data.T.reset_index()
stock_data = pd.melt(stock_data, id_vars=['Date']
st.stock_data
