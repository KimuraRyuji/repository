import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_excel('https://github.com/KimuraRyuji/repository/blob/main/reins_used_202003.xlsx')

df = pd.DataFrame(data, columns=["年月", "件数"])

st.bar_chart(data=df, x="年月", y="件数", width=0, height=0, use_container_width=True,)
