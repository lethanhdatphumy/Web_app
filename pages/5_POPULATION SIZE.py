import pandas as pd
import plotly.express as px
import streamlit as st

# Load data
uploaded_file = st.file_uploader("Update your data", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
else:
    data = pd.read_csv(r"GOD'sDATA.csv")


# Get min and max years in the data
min_year = int(data['Year'].min())
max_year = int(data['Year'].max())

# Add a sidebar selectbox to select a year
year = st.sidebar.slider('Select a Year', min_year, max_year, value=2000)

# Filter the data for the selected year
filtered_data = data[data['Year'] == year]

# Group the filtered data by Year and Country, summing the Population_size
grouped_data = filtered_data.groupby(['Country'])['Population_size'].sum().reset_index()

# Create bar chart
fig = px.bar(grouped_data, x='Country', y='Population_size',
             title="Total population in Southeast Asia countries", 
             labels={'Population_size':'Population (Million People)', 'Country':'Country'},
             color='Country')

# Display the figure
st.plotly_chart(fig)
