import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit TEST')

st.write('Display Image')

img = Image.open('C:\Users\rykimura\Downloads\AISmiley_BDSP_Point1.jpg')
st.image(img, caption='rykimura', use_column_width=True)

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)

#st.table(df.style.highlight_max(axis=0))
