import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")
radius = st.sidebar.slider('現在地からの距離', 0, 20, 10)

st.sidebar.write('日商 太郎様')
st.sidebar.write('日商 太郎様\ボストンテリア')

st.write('提携病院のパーソナライズドレコメンド')
df = pd.DataFrame(
  np.random.randn(50, 2)/[50, 50] + [35.69, 139.70],
  columns=['lat', 'lon']
)
st.map(df)
