import streamlit as st
import pandas as pd
import plotly.express as px


uploaded_file = st.file_uploader("Update your data", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv(r"GOD'sDATA.csv")

# Create a sidebar for user inputs
st.sidebar.header('User Input Parameters')
rating_selection = st.sidebar.selectbox('Choose Rating Economy Category', ['low income', 'lower middle income', 'upper middle income', 'high income'])

# Filter the data based on the user inputs
df = df[df['Rating_economy'] == rating_selection]

# Group data
Rating_counts = df['Country'].value_counts().reset_index()
Rating_counts.columns = ['Country', 'Count']

# Create an interactive bar chart
fig = px.bar(Rating_counts, x='Country', y='Count', color='Country', 
             title=f"RATING ECONOMY OF SOUTHEAST ASIAN COUNTRIES - {rating_selection.upper()} \nData source: World Bank")

# Display chart
st.plotly_chart(fig)
