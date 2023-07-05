import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("GOD'sDATA.csv")
df.columns = df.columns.str.strip()

st.set_page_config(
    page_title="Data Visualization",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)

fig1 = px.box(df, 
              x='Country', 
              y='GDP_growth', 
              color='Country',
              labels={"Country": "Country", "GDP_growth": "GDP Growth (%)"},
              title="GDP Growth by Country",
              template='plotly_white'
)

fig1.update_layout(
    font_family="Courier New",
    font_color="darkblue",
    title_font_family="Times New Roman",
    title_font_color="red"
)

# Create density plot for GDP growth rate by rating economy
fig2 = go.Figure()
colors = ['blue', 'orange', 'green', 'red']

for rating, color in zip(df['Rating_economy'].unique(), colors):
    subset = df[df['Rating_economy'] == rating]
    fig2.add_trace(go.Histogram(x=subset['GDP_growth'], 
                                nbinsx=30, 
                                histnorm='probability density',  # set to create a density plot
                                opacity=0.7, 
                                marker_color=color, 
                                name=f'Rating economy: {rating}'))

fig2.update_layout(
    barmode='overlay',
    title_text='Density Plot of GDP growth rate by rating economy',
    xaxis_title_text='GDP Growth (%)', 
    yaxis_title_text='Density',  # update axis label to reflect the change to a density plot
    template='plotly_white', 
    font=dict(
        family="Courier New",  
        size=14,
        color="darkblue"
    ),
    title_font=dict(
        family="Times New Roman", 
        size=18, 
        color="red"
    )
)
fig2.update_traces(marker_line_color='black', marker_line_width=1.2, showlegend=False)


st.title("Welcome to Data Visualization")
st.header("Data Visualization")

# Display the box plot
st.plotly_chart(fig1)

st.markdown("---")


st.plotly_chart(fig2)
