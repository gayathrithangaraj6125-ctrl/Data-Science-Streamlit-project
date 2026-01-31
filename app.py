import pandas as pd
import streamlit as st

st.set_page_config(page_title="Cricket Player Stats", layout="centered")

st.title("🏏 Cricket Player Statistics Dashboard")

# Load data
data = pd.read_csv("data/matches.csv")

# Player selector
players = sorted(data["Player"].unique())
selected_player = st.selectbox("Select a Player", players)

# Filter player data
player_data = data[data["Player"] == selected_player]

st.subheader("Player Details")
st.dataframe(player_data)

# Extract values
runs = int(player_data["Runs"].values[0])
average = float(player_data["Ave"].values[0])
strike_rate = float(player_data["SR"].values[0])
matches = int(player_data["Mat"].values[0])

# Display metrics
st.subheader("Performance Summary")
st.metric("Matches", matches)
st.metric("Runs", runs)
st.metric("Average", average)
st.metric("Strike Rate", strike_rate)

# Simple bar chart
st.subheader("Runs Visualization")
st.bar_chart(player_data.set_index("Player")["Runs"])
