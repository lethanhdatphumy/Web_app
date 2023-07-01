import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("GOD'sDATA.csv")
df.columns = df.columns.str.strip()

st.sidebar.header('User Input Parameters')


default_countries = df['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect('Country', default_countries, default=default_countries)


linetype = st.sidebar.selectbox('Line Style', ['solid', 'dashed', 'dashdot', 'dotted'])
linewidth = st.sidebar.slider('Line Width', 0.1, 5.0, 2.2)

plt.figure(figsize=(10, 6))
plt.title("Average Life Expectancy in Southeast Asia\nData Source: World Bank", fontsize=18, fontweight="bold", color="#FF5733")
plt.xlabel("Year", fontsize=12, color="#00AA00", fontweight="bold")
plt.ylabel("Life Expectancy (Years)", fontsize=12, color="#00AA00", fontweight="bold")
plt.xticks(fontsize=12, color="black")
plt.yticks(fontsize=12, color="black")
plt.xlim(df['Year'].min(), df['Year'].max())
plt.ylim(df['Life_expectancy'].min(), df['Life_expectancy'].max())


colors = ["#FF6600", "#d95f02", "#7570b3", "#e7298a", "#66a61e", "#e6ab02", "#a6761d", "#666666", "#FF0000", "#00CC00", "#fdb863"]
for i, country in enumerate(selected_countries):
    country_data = df.loc[df['Country'] == country]
    plt.plot(country_data['Year'], country_data['Life_expectancy'], label=country, color=colors[i % len(colors)], linestyle=linetype, linewidth=linewidth)


plt.legend(title="Country", fontsize=12, title_fontsize=12, loc="lower center", bbox_to_anchor=(0.5,-0.25), ncol=3)
plt.grid()
plt.tight_layout()


st.pyplot(plt)

df['Life_expectancy_diff'] = df.groupby('Country')['Life_expectancy'].diff()

median_order = df.groupby('Country')['Life_expectancy'].median().sort_values()


DFP_sorted = df.set_index('Country').loc[median_order.index].reset_index()


countries = st.sidebar.multiselect("Select countries for the boxplot", DFP_sorted["Country"].unique(), default=DFP_sorted["Country"].unique())


DFP_filtered = DFP_sorted[DFP_sorted["Country"].isin(countries)]


plt.figure(figsize=(10, 4))
sns.violinplot(data=DFP_sorted, x="Country", y="Life_expectancy", palette="tab10")


plt.title("Average Life Expectancy in Selected Countries\nData Source: World Bank", fontweight='bold', color='#FF5733', fontsize=22)
plt.xlabel("Country", fontsize=16, color='#00AA00', fontweight='bold')
plt.ylabel("Life Expectancy (years)", fontsize=16, color='#00AA00', fontweight='bold')
plt.xticks(rotation=45, ha="right", fontsize=12)
plt.yticks(fontsize=12)
plt.minorticks_on()
plt.grid(alpha=0.4)


st.pyplot(plt)



