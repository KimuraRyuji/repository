import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_excel('https://github.com/KimuraRyuji/repository/blob/main/reins_used_202003.xlsx')

df = pd.DataFrame(data, columns=["年月", "件数"])

st.dataframe(df)
