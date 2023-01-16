import streamlit as st
import numpy as np
import pandas as pd

st.write('テストアプリケーション')

df = pd.DataFrame(
  np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
  columuns=['lat', 'lon']
)
st.map(df)
