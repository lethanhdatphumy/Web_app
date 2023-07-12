import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Data Visualization")

# File uploader to allow users to update data from the web
uploaded_file = st.file_uploader("Update your data", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv(r"GOD'sDATA.csv")

# Sidebar controls
selected_rating = st.sidebar.selectbox('Select Rating Economy', df['Rating_economy'].unique())

# Filter the data based on the selected rating
subset = df[df['Rating_economy'] == selected_rating]

# Additional interactivity
st.header("Additional Interactivity")

# Plot Histogram
fig = go.Figure(data=[go.Histogram(x=subset['GDP_growth'], nbinsx=20)])

# Update layout for title and axes labels
fig.update_layout(
    title_text='GDP Growth Distribution',
    xaxis_title='GDP Growth',
    yaxis_title='Count',
)

# Display the updated plot using Streamlit's plotting function
st.plotly_chart(fig)
