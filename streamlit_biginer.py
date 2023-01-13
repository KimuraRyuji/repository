import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('AI開発・運用')

st.write('Display Image')

st.write('Interactive Widgets')

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

text = st.text_input('あなたの趣味を教えてください')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味：', text,'です。'
'コンディション：', condition

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'
#if st.checkbox('Show Image'):
#    img = Image.open('AISmiley_BDSP_Point1.jpg')
#    st.image(img, caption='CRISP-DM', use_column_width=True)

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)

#st.table(df.style.highlight_max(axis=0))
