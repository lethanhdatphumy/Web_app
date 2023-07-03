import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="",
    page_icon=":wave:",
)

data = pd.read_csv("GOD'sDATA.csv")

st.title("Welcome to My")
st.header("Data Overview")

st.write(data)

sidebar_image = Image.open(r"C:\Users\Đạt\Pictures\Screenshot 2023-07-01 094636.jpg")
st.sidebar.image(sidebar_image, use_column_width=True)

st.sidebar.markdown("## Sidebar")
st.sidebar.info("Select pages above <3")
