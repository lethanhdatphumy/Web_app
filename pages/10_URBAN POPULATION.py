import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("GOD'sDATA.csv")
df.columns = df.columns.str.strip()

st.set_page_config(
    page_title="Life Expectancy and GDP Growth",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
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

st.sidebar.header('User Input Parameters')

default_countries = df['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect('Country', default_countries, default=default_countries)


filtered_df = df[df['Country'].isin(selected_countries)]


plt.figure(figsize=(10, 8))
sns.scatterplot(data=filtered_df, x='GDP_growth', y='Life_expectancy', hue='Country', alpha=0.8, marker='o', edgecolor='none')

plt.title("Relationship between Life Expectancy and GDP Growth\nData Source: World Bank", fontsize=18, color="#FF5733", loc='center', pad=20, fontweight='bold')
plt.xlabel("GDP Growth Rates (%)", fontsize=12, color="#00AA00", fontweight='bold')
plt.ylabel("Life Expectancy (Years)", fontsize=12, color="#00AA00", fontweight='bold')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

legend = plt.legend(title="Country", loc="upper left", bbox_to_anchor=(1.02, 1), fontsize=12, title_fontsize=12, ncol=1)


colors = {
    "Country1": "#e41a1c",
    "Country2": "#377eb8",
    "Country3": "#4daf4a",
    "Country4": "#984ea3",
    "Country5": "#ff7f00",
    "Country6": "#ffff33",
    "Country7": "#a65628",
    "Country8": "#f781bf",
    "Country9": "#999999",
    "Country10": "#66c2a5"
}

for text, label in zip(legend.get_texts(), legend.get_texts()):
    country = label.get_text()
    if country in colors:
        text.set_color(colors[country])

plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.grid(True, which='both', linestyle='--', alpha=0.6)


st.pyplot(plt)



plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x="Exports_of_GDP", y="GDP_growth", hue="Country", s=80, edgecolor='none')

plt.title("Relationship between GDP Growth and Exports\nData Source: World Bank",
          fontweight='bold', loc='center', color='#FF4500', fontsize=18)
plt.xlabel("Exports (% of GDP)", fontweight='bold', loc='center', fontsize=14, color='#00AA00')
plt.ylabel("GDP Growth Rates (%)", fontweight='bold', fontsize=14, color='#00AA00')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

sns.set_style('whitegrid')

legend = plt.legend(title="Country", loc="lower center", bbox_to_anchor=(0.5, -0.35), ncol=5)

for text in legend.get_texts():
    text.set_fontweight('semibold')
    text.set_fontsize(12)

plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.grid(True, which='both', linestyle='--', alpha=0.6)


st.pyplot(plt)