# Importing necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_csv(r"GOD'sDATA.csv")
df.columns=df.columns.str.strip()
# Create a sidebar for user inputs
st.sidebar.header('User Input Parameters')
rating_selection = st.sidebar.selectbox('Choose Rating Economy Category', ['low income', 'lower middle income', 'upper middle income', 'high income'])

# Filter the data based on the user inputs
df = df[df['Rating_economy'] == rating_selection]

# Preprocess and visualize data
Rating_counts = df.groupby(['Rating_economy', 'Country']).size().unstack(fill_value=0)
rating_counts = df.groupby('Rating_economy').size().reset_index(name='count')
rating_counts = rating_counts.sort_values('count')

df['Rating_economy'] = pd.Categorical(df['Rating_economy'], categories=rating_counts['Rating_economy'])

Rating_counts = Rating_counts.reindex([rating_selection])

# This line will make sure that the app doesn't rerun from the top every time the user interacts with a widget
st.set_option('deprecation.showPyplotGlobalUse', False)

plt.figure(figsize=(20,5))
Rating_counts.plot(kind='bar', stacked=True)

plt.title(f"RATING ECONOMY OF SOUTHEAST ASIAN COUNTRIES - {rating_selection.upper()} \nData source: World Bank", fontweight='bold', loc='center',color='#FF4500',fontsize=18)
plt.xlabel("Rating economy", fontweight='bold',loc='center', fontsize=14, color='#00AA00')
plt.ylabel("Count", fontweight='bold',fontsize=14, color='#00AA00')
plt.tick_params(axis='x', labelsize=12)
plt.tick_params(axis='y', labelsize=12)
sns.set_style('whitegrid')
plt.xticks(rotation=15)
legend = plt.legend(title='Country', loc='best', bbox_to_anchor=(0.5, -0.4), ncol=5)

for text in legend.get_texts():
    text.set_fontweight('semibold')
    text.set_fontsize(12)
plt.tight_layout()
st.pyplot()
