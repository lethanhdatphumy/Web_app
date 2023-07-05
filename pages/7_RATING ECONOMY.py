import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('GOD'sDATA.csv')
df.columns = df.columns.str.strip()

rating_counts = df.groupby('Rating_economy').size().reset_index(name='count')
rating_counts = rating_counts.sort_values('count')

df['Rating_economy'] = pd.Categorical(df['Rating_economy'], categories=rating_counts['Rating_economy'])

Rating_counts = df.groupby(['Rating_economy', 'Country']).size().unstack(fill_value=0)
Rating_counts = Rating_counts.reindex(['low income', 'lower middle income', 'upper middle income', 'high income'])

fig, ax = plt.subplots(figsize=(20, 5))
Rating_counts.plot(kind='bar', stacked=True, ax=ax)

ax.set_title("RATING ECONOMY OF SOUTHEAST ASIAN COUNTRIES \nData source: World Bank", fontweight='bold', loc='center', color='#FF4500', fontsize=18)
ax.set_xlabel("Rating economy", fontweight='bold', loc='center', fontsize=14, color='#00AA00')
ax.set_ylabel("Count", fontweight='bold', fontsize=14, color='#00AA00')
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)
sns.set_style('whitegrid')
ax.set_xticklabels(ax.get_xticklabels(), rotation=15)

legend = ax.legend(title='Country', loc='lower center', bbox_to_anchor=(0.5, -0.4), ncol=5)
for text in legend.get_texts():
    text.set_fontweight('semibold')
    text.set_fontsize(12)

plt.tight_layout()

# Streamlit code
st.title("RATING ECONOMY OF SOUTHEAST ASIAN COUNTRIES")
st.pyplot(fig)

# Interactive elements
selected_countries = st.multiselect('Select Countries', df['Country'].unique())

selected_data = df[df['Country'].isin(selected_countries)]
selected_rating_counts = selected_data.groupby(['Rating_economy', 'Country']).size().unstack(fill_value=0)

st.subheader("Selected Data")
st.dataframe(selected_data)

st.subheader("Rating Economy Counts for Selected Countries")
st.dataframe(selected_rating_counts)
