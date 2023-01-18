import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(
  np.random.randn(1000, 2)/[50, 50] + [35.69, 139.70],
  columns=['lat', 'lon']
)
st.map(df)
