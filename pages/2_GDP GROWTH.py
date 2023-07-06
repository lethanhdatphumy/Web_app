import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

url = "https://raw.githubusercontent.com/lethanhdatphumy/Data-Analysis-/ed49225f84d63a1424220cb95f01dea4448166d2/GOD'sDATA.csv"

df = pd.read_csv(url)
df.columns = df.columns.str.strip()


st.set_page_config(
    page_title="Data Visualization",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)


fig1 = px.box(df, 
              x='Country', 
              y='GDP_growth', 
              color='Country',
              labels={"Country": "Country", "GDP_growth": "GDP Growth (%)"},
              title="GDP Growth by Country",
              template='plotly_white'
)

fig1.update_traces(boxpoints=False)  
fig1.update_layout(
    font_family="Courier New",
    font_color="darkblue",
    title_font_family="Times New Roman",
    title_font_color="red"
)
colors = ['#EE2C2C', '#00F5FF', '#CD853F', '#00CD00']

st.write(fig1)
ratings = df['Rating_economy'].unique()


selected_rating = st.sidebar.selectbox('Select a Rating Economy', ratings)


subset = df[df['Rating_economy'] == selected_rating]

plt.figure(figsize=(10, 6))

# Plotting
sns.kdeplot(subset['GDP_growth'], fill=True, color=colors[ratings.tolist().index(selected_rating)], alpha=0.4, linewidth=1.4,
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
