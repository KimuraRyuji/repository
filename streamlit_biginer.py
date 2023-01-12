import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit TEST')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.bar_chart(df)

#st.table(df.style.highlight_max(axis=0))
