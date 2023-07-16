import pandas as pd
import plotly.express as px
import streamlit as st
uploaded_file = st.file_uploader("Update your data", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv(r"GOD'sDATA.csv")


st.sidebar.header('User Input Parameters')

default_countries = df['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect('Country', default_countries, default=default_countries)

df['Life_expectancy_diff'] = df.groupby('Country')['Life_expectancy'].diff()
median_order = df.groupby('Country')['Life_expectancy'].median().sort_values()
DFP_sorted = df.set_index('Country').loc[median_order.index].reset_index()

countries = st.sidebar.multiselect("Select countries for the boxplot", DFP_sorted["Country"].unique(), default=DFP_sorted["Country"].unique())
DFP_filtered = DFP_sorted[DFP_sorted["Country"].isin(countries)]

fig = px.line(df[df.Country.isin(selected_countries)], x='Year', y='Life_expectancy', color='Country', 
              labels={'Life_expectancy':'Life Expectancy (Years)', 'Year':'Year'}, 
              title="Average Life Expectancy in Southeast Asia")
st.plotly_chart(fig)

fig = px.box(DFP_filtered, x="Country", y="Life_expectancy", color="Country",
             title="Average Life Expectancy in Selected Countries")
st.plotly_chart(fig)
