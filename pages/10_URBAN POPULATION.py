import pandas as pd
import streamlit as st
import plotly.express as px
# File uploader to allow users to update data from the web
uploaded_file = st.file_uploader("Update your data", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv(r"GOD'sDATA.csv")

# Sidebar for user input
st.sidebar.header('User Input Parameters')

default_countries = df['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect('Country', default_countries, default=default_countries)

default_years = df['Year'].unique().tolist()
selected_years = st.sidebar.slider('Year', min_value=min(default_years), max_value=max(default_years), value=[min(default_years),max(default_years)])

# Filter the data based on the user inputs
filtered_data = df[df['Country'].isin(selected_countries) & df['Year'].isin(range(selected_years[0], selected_years[1]+1))]

# Create interactive bar plot
fig = px.bar(filtered_data, x='Year', y='Urban_population', color='Country', title="Total Urban Population in Selected Countries\nData Source: World Bank", labels={'Urban_population': 'Urban Population (Million People)', 'Year': 'Year'})
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})

st.plotly_chart(fig)
