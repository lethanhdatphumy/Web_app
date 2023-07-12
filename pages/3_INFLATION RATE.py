import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# File uploader to allow users to update data from the web
uploaded_file = st.file_uploader("Update your data", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv(r"GOD'sDATA.csv")
st.sidebar.header('User Input Features')
selected_years = st.sidebar.slider('Year range', 1990, 2020, (1990, 2020))

df_selected = df[(df['Year'] >= selected_years[0]) & (df['Year'] <= selected_years[1])]

mean_inflation = df_selected.groupby('Country')['Inflation_consumer_prices'].mean()

mean_inflation_sorted = mean_inflation.sort_values(ascending=True)

mean_inflation_sorted = mean_inflation_sorted.reset_index()

fig = px.bar(mean_inflation_sorted, y='Country', x='Inflation_consumer_prices', orientation='h', 
             color='Inflation_consumer_prices', color_continuous_scale=px.colors.sequential.Plasma)

fig.update_layout(
    title_text='Mean Inflation Consumer Prices (Selected Years)',
    xaxis_title="Mean Inflation rates (%)",
    yaxis_title="Country",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"
    ),
)

fig.update_yaxes(automargin=True)
st.plotly_chart(fig)
