import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="",
    page_icon=":wave:",
)


data = pd.read_csv("E:\\code\\GOD\\GOD'sDATA.csv")


st.title("Welcome to My" )
st.header("Data Overview")

st.write(data)


st.sidebar.markdown("## Sidebar")
st.sidebar.info("Select pages above <3")


