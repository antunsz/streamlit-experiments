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

df_players = df[df['Club'] == club]

players = df_players['Name'].unique()

player = st.sidebar.selectbox('Player', players)

player_stats = df[df['Name'] == player].iloc[0]

st.image(player_stats['Photo'])
st.title(player_stats['Name'])
st.markdown(f"""
            **Club**: {player_stats['Club']}

            **Position**: {player_stats['Position']}
            """)

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Age**: {player_stats['Age']}")
col2.markdown(f"**Height**: {player_stats['Height(cm.)']/100}")
col3.markdown(f"**Weight**: {player_stats['Weight(lbs.)']*0.453:.2f}")

st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label='Market value', value=f"{player_stats['Value(£)']:,}")
col2.metric(label='Wage', value=f"{player_stats['Wage(£)']:,}")
col3.metric(label='Release Clause', value=f"{player_stats['Release Clause(£)']:,}")


