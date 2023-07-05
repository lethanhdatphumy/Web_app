import streamlit as st
import pandas as pd
from PIL import Image
from pandas import options

st.set_page_config(
    page_title="",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("Analysis of selected Socio - Economic Issues in ASEAN")
st.header("Using Python, CSS and HTML for ploting")

image = Image.open('ASEAN Welcome page.jpg')

st.image(image, caption='Sunrise by the mountains')
