import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("GOD'sDATA.csv")
df.columns = df.columns.str.strip()

st.set_page_config(
    page_title="Inflation and Unemployment Analysis",
    page_icon="💹",
    layout="wide",
    initial_sidebar_state="expanded"
)


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


mean_inflation = df.groupby('Country')['Inflation_consumer_prices'].mean()
mean_inflation_sorted = mean_inflation.sort_values(ascending=True)

selected_countries = st.multiselect("Select Countries", mean_inflation_sorted.index)
filtered_data = mean_inflation_sorted[selected_countries]

fig1, ax = plt.subplots(figsize=(10, len(filtered_data) * 0.5))
colors = plt.cm.viridis(np.linspace(0, 1, len(filtered_data)))
ax.barh(filtered_data.index, filtered_data.values, color=colors)

plt.xlabel('Mean Inflation rates (%)', fontweight='bold', fontsize=14, color='#222831')
plt.ylabel('Country', fontweight='bold', fontsize=14, color='#222831')
plt.title('Mean Inflation Consumer Prices (1990-2020)', fontweight='bold', loc='center', color='#FF4500', fontsize=18)
plt.tick_params(axis='both', labelsize=12, colors='#393e46')
plt.grid(True, axis='x', linestyle='--', color='#e3e3e3')
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

st.pyplot(fig1)
st.markdown("---")
