import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime


if 'data' not in st.session_state:
    df = pd.read_csv('./data/CLEAN_FIFA23_official_data.csv', index_col=0)
    df = df[df['Contract Valid Until'] >= datetime.today().year]
    df = df[df['Value (£)'] > 0].sort_values(by='Overall', ascending=False)

    st.session_state['data'] = df

st.markdown("""
            # FIFA Project (Official Dataset)

            Developed by Carlos Antunes during the [ASIMOV ACADEMY](https://asimov.academy) course about Streamlit
            """)

btn = st.button("Kaggle data used in this project")

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
