import streamlit as st
import pandas as pd
import plotly.express as px
import time

df = st.cache_data(pd.read_csv)("data/nhl.csv", encoding='ISO-8859-1')

st.snow()

# Progress bar

bar_p = st.progress(0)

for percentage_complete in range(100):
    time.sleep(0.001)
    bar_p.progress(percentage_complete + 1)

# Status message
# display a temporary message when executing a block of code

with st.spinner('Please wait...'):
    time.sleep(1)
st.write('Complete!')


st.write(
        """
        # NHL Player Stats 2004 - 2018
        """
    )

st.image('data/nhl_players.jpg')


team = st.sidebar.multiselect(
    "Select a team:",
    df['Tm'].unique()
)

position = st.sidebar.multiselect(
    "Select player's position:",
    df['Pos'].unique()
)

season = st.sidebar.multiselect(
    "Select the NHL season:",
    df['Season'].unique()
)

filtred = df[(df['Tm'].isin(team)) & (df['Pos'].isin(position)) & (df['Season'].isin(season))]

st.write(
        """
        ## Filtered data
        """
    )

st.write(filtred)

fig = px.scatter(filtred, x='PTS', y='G', color='Player')

# Plot!
st.write(
        """
        ## NHL players and their goal and point statistics
        """
    )
st.plotly_chart(fig)

st.write(
        """
        ## Goals by selected teams
        """
    )
fig2 = px.pie(filtred, values='G', names='Tm')
st.plotly_chart(fig2, use_container_width=True)

st.write(
        """
        ## The plus–minus stats of the players by team and other selected options
        """
    )


st.bar_chart(filtred, x="Tm", y="plusminus", color="Player")

