import streamlit as st
import pandas as pd
from PIL import Image
import base64
st.set_page_config(
    page_title="",
    page_icon=":wave:",
)



data = pd.read_csv("GOD'sDATA.csv")
data.columns= data.columns.str.strip()
st.title("Welcome to My" )
st.header("Data Overview")
data["Year"] = data["Year"].astype(str)
st.write(data)

st.sidebar.image(sidebar_image,use_column_width=True)
st.sidebar.markdown("## Sidebar")
st.sidebar.info("Select pages above <3")
