import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# Read the dataset from the CSV file
df = pd.read_csv("GOD'sDATA.csv")
df.columns = df.columns.str.strip()

sns.set_style("whitegrid")

# Create checkboxes for sorting options
ascending = st.checkbox("Sort ascending")



# Sort the data based on the selected column and toggle value
sorted_data = df.sort_values("Unemployment_rate", ascending=ascending)

# Extract necessary columns
countries = sorted_data["Country"]
years = sorted_data["Year"]
unemployment_rate = sorted_data["Unemployment_rate"]

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(years, countries, s=unemployment_rate * 50, alpha=0.7, c=unemployment_rate, cmap='cool')

# Add labels and title
ax.set_title("Unemployment Rates in Southeast Asia\nData Source: World Bank", fontweight='bold', color='#FF5733', fontsize=22)
ax.set_xlabel("Unemployment Rate (%)", fontsize=16, color='#00AA00', fontweight='bold')
ax.set_ylabel("Country", fontsize=16, color='#00AA00', fontweight='bold')
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# Add a colorbar
cbar = fig.colorbar(scatter)
cbar.set_label('Unemployment Rate', fontsize=12)

# Remove the spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Customize the tick labels
ax.xaxis.set_tick_params(labelsize=12, rotation=45, color='#555555')
ax.yaxis.set_tick_params(labelsize=12, color='#555555')

# Customize the plot colors
scatter.set_cmap('cool')
cbar.ax.tick_params(labelsize=10, color='#555555')

# Display the plot in Streamlit
st.pyplot(fig)

# Interactive selectbox for selecting a year
years = [1990, 2000, 2005, 2010, 2015, 2020]
selected_year = st.selectbox('Select a year:', years)

# Filter data for the selected year
year_data = df[df['Year'] == selected_year]
unemployment_rates = year_data['Unemployment_rate']
countries = year_data['Country']

# Set up the plot with larger chart size
fig2, ax2 = plt.subplots(figsize=(10, 8))

# Create the donut chart with a dynamic color palette
palette = sns.color_palette("hsv", len(countries))
wedges, texts, autotexts = ax2.pie(unemployment_rates, colors=palette, autopct='%1.1f%%',
                                  startangle=90, pctdistance=0.85, wedgeprops={'edgecolor': 'white', 'linewidth': 2},
                                  textprops={'fontsize': 12})

# Draw a white circle at the center to create a donut chart
center_circle = plt.Circle((0, 0), 0.70, fc='white')
fig2.gca().add_artist(center_circle)

# Move the labels outside the donut chart and set properties for better readability
plt.setp(autotexts, size=10, weight="bold", color='black')

# Set equal aspect ratio to ensure circular shape
ax2.axis('equal')

# Set the title with larger font size and color
ax2.set_title(f"Unemployment Rates in Southeast Asia ({selected_year})", fontsize=16, color="navy", fontweight="bold")

# Add legend outside the pie chart
plt.legend(wedges, countries,
           title="Countries",
           loc="center left",
           bbox_to_anchor=(1, 0, 0.5, 1))

# Display the plot in Streamlit
st.pyplot(fig2)
