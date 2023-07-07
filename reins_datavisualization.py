import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv('https://github.com/KimuraRyuji/repository/blob/main/reins_used_202003.csv')

df = pd.DataFrame(data, columns=[0, 1])

st.dataframe(df)
