import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/lethanhdatphumy/Data-Analysis-/ed49225f84d63a1424220cb95f01dea4448166d2/GOD'sDATA.csv"

df = pd.read_csv("GOD'sDATA.csv")
df.columns = df.columns.str.strip()

st.set_page_config(
    page_title="Data Visualization",
    page_icon=":bar_chart:",
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

fig1 = px.box(df, 
              x='Country', 
              y='GDP_growth', 
              color='Country',
              template='plotly_white')

plt.title('GDP growth rate by Country \nData Source: World Bank',
          fontweight='bold', color='#FF5733', fontsize=22)
plt.xlabel('Country', fontsize=16, color='#00AA00', fontweight='bold')
plt.ylabel('GDP growth (%)', fontsize=16, color='#00AA00', fontweight='bold')
fig1.update_traces(boxpoints=False)

st.write(fig1)

ratings = df['Rating_economy'].unique()
selected_rating = st.sidebar.selectbox('Select a Rating Economy', ratings)
subset = df[df['Rating_economy'] == selected_rating]

plt.figure(figsize=(10, 6))
# Plotting
sns.kdeplot(subset['GDP_growth'], fill=True, color='red', alpha=0.4, linewidth=1.4,
            label=f'Rating economy: {selected_rating}')

plt.title('Distribution of GDP growth rate according to rating economy\nData Source: World Bank',
          fontweight='bold', color='#FF5733', fontsize=22)
plt.xlabel('GDP Growth (%)', fontsize=16, color='#00AA00', fontweight='bold')
plt.ylabel('Density', fontsize=16, color='#00AA00', fontweight='bold')
plt.legend(title='Rating economy')
plt.minorticks_on()
plt.grid(True, which='both', linestyle='--', alpha=0.8)
plt.tight_layout()

st.pyplot(plt)
