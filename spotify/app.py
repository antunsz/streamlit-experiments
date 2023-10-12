import streamlit as st
import pandas as pd

st.set_page_config(
        layout='wide',
        page_title='spotfy songs'
        )

@st.cache_data
def load_data():
    df = pd.read_csv('./data/01 Spotify.csv')
    return df


df = load_data()
st.session_state['df_spotify'] = df

df.set_index('Track', inplace=True)

artist = st.sidebar.selectbox('Artista', df.Artist.value_counts().index)
df_filtered = df[df['Artist'] == artist]

album = st.sidebar.selectbox('Album', df_filtered.Album.value_counts().index)
show_artist_graph = st.checkbox('Mostrar')

col1, col2 = st.columns(2)

if show_artist_graph:
    var1 = col1.selectbox('Variável 1', df.columns)
    col1.bar_chart(df_filtered[df_filtered['Album'] == album][var1])
    var2 = col2.selectbox('Variável 2', df.columns)
    col2.line_chart(df_filtered[df_filtered['Album'] == album][var2])

