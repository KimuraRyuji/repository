import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf

aapl = yf.Ticker('AAPL')

aapl.history()
yfinance.Ticker object<AAPL>
