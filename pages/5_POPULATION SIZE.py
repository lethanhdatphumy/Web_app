import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

try:
    df = pd.read_csv("GOD'sDATA.csv")
except FileNotFoundError:
    st.error("File not found, please check the path and file name.")

df.columns = df.columns.str.strip()

df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

df = df[df['Year'].notna()]

year = st.sidebar.slider('Select a Year Range', int(df['Year'].min()), int(df['Year'].max()), (1990, 2020))

filtered_data = df[(df['Year'] >= year[0]) & (df['Year'] <= year[1])]

grouped_data = filtered_data.groupby(['Year', 'Country'])['Population_size'].sum().reset_index()

sns.set_style("whitegrid")

fig, ax = plt.subplots(figsize=(12, 8))


for country in grouped_data['Country'].unique():
    country_data = grouped_data[grouped_data['Country'] == country]
    sns.histplot(data=country_data, x='Year', y='Population_size', label=country, kde=True)

ax.set_title("Population distribution in Southeast Asian countries from 1990 to 2020", fontweight='bold', color='#333333', fontsize=22)
ax.set_xlabel("Year", fontsize=16, color='#333333', fontweight='bold')
ax.set_ylabel("Population (Million People)", fontsize=16, color='#333333', fontweight='bold')

plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
ax.get_yaxis().get_major_formatter().set_scientific(False)

ax.legend(title='Country', title_fontsize='13', fontsize='11')

st.pyplot(fig)
