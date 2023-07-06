import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st



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

# Load data
data = pd.read_csv("GOD'sDATA.csv")
data.columns = data.columns.str.strip()

# Get min and max years in the data
min_year = int(data['Year'].min())
max_year = int(data['Year'].max())

# Add a sidebar selectbox to select a year
year = st.sidebar.selectbox('Select a Year', list(range(min_year, max_year + 1)), index=30)

# Filter the data for the selected year
filtered_data = data[data['Year'] == year]

# Group the filtered data by Year and Country, summing the Population_size
grouped_data = filtered_data.groupby(['Year', 'Country'])['Population_size'].sum().unstack()

# Colors for the bar chart
colors = ["#E60000", "#ff82ab", "#7fffd4", "#ffb90f", "#ff6eb4",
          "#ff3030", "#fa8072", "#FF7F24", "#00ff7f", "#0066cc"]

st.set_option('deprecation.showPyplotGlobalUse', False)

# Set figure size
plt.figure(figsize=(12, 8))

# Create bar chart
grouped_data.plot(kind='bar', grid=True, color=colors, width=0.8)

# Set chart title, labels, ticks, and legend
plt.title("Total population in Southeast Asia countries\nData Source: World Bank", 
          fontweight='bold', color='#FF5733', fontsize=22)
plt.xlabel("Year", fontsize=16, color='#00AA00', fontweight='bold')
plt.ylabel("Population (Million People)", fontsize=16, color='#00AA00', fontweight='bold')
plt.xticks(fontsize=12, rotation=0)
plt.yticks(fontsize=12)
plt.legend(loc='upper right')

# Hide the offset on the y-axis
plt.gca().get_yaxis().get_offset_text().set_visible(False)

# Show the plot in the Streamlit app
st.pyplot(plt.gcf())
