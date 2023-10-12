import streamlit as st

st.set_page_config(
    page_title='Players',
    layout='wide'
)

if 'data' not in st.session_state:
    df = pd.read_csv('../data/CLEAN_FIFA23_official_data.csv', index_col=0)
    df = df[df['Contract Valid Until'] >= datetime.today().year]
    df = df[df['Value (£)'] > 0].sort_values(by='Overall', ascending=False)

    st.session_state['data'] = df

df = st.session_state['data']

clubs = df['Club'].unique()

club = st.sidebar.selectbox('Club', clubs)

df_players = df[df['Club'] == club].set_index('Name')

st.image(df_players.iloc[0]['Club Logo'])
st.markdown(f"## {club}")


columns = ['Age', 'Photo', 'Flag', 'Overall']

st.dataframe(
        df_players[columns],
        column_config={
            'Overall':st.column_config.ProgressColumn(
                'Overall', format="%d", min_value=0, max_value=100
                ),
            'Photo':st.column_config.ImageColumn(),
            'Flag':st.column_config.ImageColumn('Country')
            })
