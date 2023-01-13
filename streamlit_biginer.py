import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('AI開発・運用')

st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('AISmiley_BDSP_Point1.jpg')
    st.image(img, caption='CRISP-DM', use_column_width=True)

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)

#st.table(df.style.highlight_max(axis=0))
