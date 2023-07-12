import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def load_data(nrows):
    data = pd.read_csv("GOD'sDATA.csv", nrows=nrows)
    data.columns = data.columns.str.strip()
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load data into the dataframe.
df = load_data(10000)

# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

country = st.sidebar.selectbox('Select a Country', df['Country'].unique())
years = st.sidebar.multiselect('Select Years', df['Year'].unique())

filtered_data = df[(df['Country'] == country) & (df['Year'].isin(years))]
filtered_data = filtered_data.sort_values(by='Year')

num_vars = len(years)

angles = [n / float(num_vars) * 2 * 3.14159 for n in range(num_vars)]
angles += angles[:1]  # Close the loop

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

values = filtered_data['Exports_of_GDP'].tolist()
values += values[:1]

plt.xticks(angles[:-1], years, color='black', size=8)

ax.plot(angles, values, linewidth=1, linestyle='solid', label=country)
ax.fill(angles, values, 'b', alpha=0.1)

plt.title('Exports_of_GDP trend for ' + country, size=20, color='blue', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

st.pyplot(fig)
