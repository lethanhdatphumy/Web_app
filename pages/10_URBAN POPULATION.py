import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


page_bg_img = '''
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stAppViewContainer"]  {
background-image: url("https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=871&q=80");
background-size:cover;
background-repeat: no-repeat;
}
[data-testid="stHeader"]{
background-color : rgba(0,0,0,0)
    
}
[data-testid="stSidebar"]{
background-image: url("https://images.unsplash.com/photo-1483401757487-2ced3fa77952?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=873&q=80");
background-size:cover;
background-repeat: no-repeat;
}

</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

data = pd.read_csv("GOD'sDATA.csv")
data.columns = data.columns.str.strip()


st.sidebar.header('User Input Parameters')


default_countries = data['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect('Country', default_countries, default=default_countries)


default_years = data['Year'].unique().tolist()
selected_years = st.sidebar.multiselect('Year', default_years, default=[1990, 2000, 2010, 2020])


filtered_data = data[data['Country'].isin(selected_countries) & data['Year'].isin(selected_years)]


grouped_data = filtered_data.groupby(['Country', 'Year'])['Urban_population'].sum().unstack()


colors = ["#ff3030", "#F1C40F", "#2980B9", "#D35400"] * len(selected_countries)


plt.figure(figsize=(12, 8))
grouped_data.plot(kind='bar', grid=True, color=colors, width=0.5)


plt.title("Total urban population in Selected Countries\nData Source: World Bank", fontweight='bold', color='#FF5733', fontsize=22)
plt.xlabel("Year", fontsize=16, color='#00AA00', fontweight='bold')
plt.ylabel("Urban Population (Million People)", fontsize=16, color='#00AA00', fontweight='bold')
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)


plt.legend(loc='upper right')


st.pyplot(plt)
