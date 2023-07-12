import streamlit as st
import pandas as pd
import plotly.figure_factory as ff

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

# Add a slider to adjust the bandwidth parameter of the KDE plot
bandwidth = st.slider("Bandwidth", min_value=0.1, max_value=5.0, step=0.1, value=1.0)

# Update the plot with the new bandwidth and color
colors = ['#FA8072'] # Salmon color
fig = ff.create_distplot([subset['GDP_growth']], ['GDP Growth'], bin_size=bandwidth, 
                         show_curve=True, colors=colors)

# Update layout for title and axes labels
fig.update_layout(
    title_text='GDP Growth Distribution',
    xaxis_title='GDP Growth',
    yaxis_title='Density',
)

# Display the updated plot using Streamlit's plotting function
st.plotly_chart(fig)
