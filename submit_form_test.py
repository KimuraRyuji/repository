import streamlit as st
import time
from PIL import Image

with st.form("test_form", clear_on_submit=False):
  name = st.text_input('訪問先を入力してください')
