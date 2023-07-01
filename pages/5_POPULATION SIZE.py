import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns


data = pd.read_csv("https://github.com/lethanhdatphumy/Data-Analysis-/blob/ed49225f84d63a1424220cb95f01dea4448166d2/GOD'sDATA.csv")
data.columns= data.columns.str.strip()


year = st.sidebar.slider('Select a Year Range', 1990, 2020, (1990, 2020))


filtered_data = data[(data['Year'] >= year[0]) & (data['Year'] <= year[1])]


grouped_data = filtered_data.groupby(['Year', 'Country'])['Population_size_million_people'].sum().unstack()


sns.set_style("whitegrid")
palette = sns.color_palette("husl", len(grouped_data.columns))


fig, ax = plt.subplots(figsize=(12, 8))

grouped_data.plot(kind='bar', stacked=True, ax=ax, color=palette, grid=False, edgecolor='black')


ax.set_title("Total population in Southeast Asia countries from 1990 to 2020", fontweight='bold', color='#333333', fontsize=22)
ax.set_xlabel("Year", fontsize=16, color='#333333', fontweight='bold')
ax.set_ylabel("Population (Million People)", fontsize=16, color='#333333', fontweight='bold')


plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)
ax.get_yaxis().get_major_formatter().set_scientific(False)


ax.legend(title='Country', title_fontsize='13', fontsize='11')


st.pyplot(fig)
