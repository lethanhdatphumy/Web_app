import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st




df = pd.read_csv("GOD'sDATA.csv")
df.columns = df.columns.str.strip()

country = st.sidebar.selectbox('Select a Country', df['Country'].unique())
filtered_data = df[df['Country'] == country]


years = [1990, 1994, 1998, 2002, 2006, 2010, 2014, 2016, 2020]
filtered_data = filtered_data[filtered_data['Year'].isin(years)]
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
