import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="",
    page_icon=":wave:",
)


data = pd.read_csv("GOD'sDATA.csv")


st.title("Welcome to My Dataset" )
data["Year"] = data["Year"].astype(str)
st.write(data)

st.sidebar.markdown("## Sidebar")
st.sidebar.info("Select pages above <3")

