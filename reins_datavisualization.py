import streamlit as st
import pandas as pd
import numpy as np

repo_url = 'https://github.com/KimuraRyuji/repository'
csv_path = 'main/reins_used_202003.csv'

def load_data():
  df = pd.read_csv(csv_path)
  return df

data = load_data()

st.bar_chart(data)
