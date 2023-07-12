import streamlit as st
import pandas as pd
import plotly.express as px



# Set page configuration
st.set_page_config(
    page_title="Unemployment Rates in Southeast Asia",
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



# Create sidebar for user inputs
ascending = st.sidebar.checkbox("Sort ascending")
sorted_data = df.sort_values("Unemployment_rate", ascending=ascending)

# Create scatter plots
fig1 = px.scatter(sorted_data, x="Year", y="Country", color="Unemployment_rate", size="Unemployment_rate", 
                 title="Unemployment Rates in Southeast Asia\nData Source: World Bank",
                 labels={"Year": "Year", "Country": "Country", "Unemployment_rate": "Unemployment Rate (%)"})
st.plotly_chart(fig1)

years = sorted(df["Year"].unique())
selected_year = st.sidebar.selectbox('Select a year:', years)

year_data = df[df['Year'] == selected_year]

fig2 = px.pie(year_data, values='Unemployment_rate', names='Country', 
              title=f"Unemployment Rates in Southeast Asia ({selected_year})")
st.plotly_chart(fig2)
