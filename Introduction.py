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
    
[data-testid="stSidebar"]{
background-image: url("https://images.unsplash.com/photo-1486520299386-6d106b22014b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=869&q=80");
background-size:cover;
background-repeat: no-repeat;
}
[data-testid="stImage"] > img{
border-radius:50%;
width:150px;

}
[data-testid="stImage"]{
}
</style>
'''
st.title("Analysis of selected Socio - Economic Issues in ASEAN")
st.header("Using Python, CSS and HTML for ploting")

image = Image.open('ASEAN Welcome page.jpg')

st.image(image, caption='Sunrise by the mountains')
st.markdown(page_bg_img, unsafe_allow_html=True)
