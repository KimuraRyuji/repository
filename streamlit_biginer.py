import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit TEST')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b','c']
)

st.bar_chart(df)

#st.table(df.style.highlight_max(axis=0))
