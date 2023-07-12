import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(
    page_title="Life Expectancy and GDP Growth",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)


uploaded_file = st.file_uploader("Update your data", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.columns=df.columns.str.strip()

else:
    df = pd.read_csv(r"GOD'sDATA.csv")
    df.columns=df.columns.str.strip()


# Set page configuration

# Create sidebar for user inputs
st.sidebar.header('User Input Parameters')
default_countries = df['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect('Country', default_countries, default=default_countries)

# Filter dataframe based on selected countries
filtered_df = df[df['Country'].isin(selected_countries)]

# Create scatter plots
fig1 = px.scatter(filtered_df, x='GDP_growth', y='Life_expectancy', color='Country', 
                 title="Relationship between Life Expectancy and GDP Growth\nData Source: World Bank",
                 labels={"GDP_growth": "GDP Growth Rates (%)", "Life_expectancy": "Life Expectancy (Years)"})
st.plotly_chart(fig1)

fig2 = px.scatter(filtered_df, x='Exports_of_GDP', y='GDP_growth', color='Country', 
                 title="Relationship between GDP Growth and Exports\nData Source: World Bank",
                 labels={"Exports_of_GDP": "Exports (% of GDP)", "GDP_growth": "GDP Growth Rates (%)"})
st.plotly_chart(fig2)
