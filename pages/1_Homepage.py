import streamlit as st
import pandas as pd
from PIL import Image


st.set_page_config(
    page_title="",
    page_icon=":wave:",
)
page_bg_img = '''
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stAppViewContainer"]  {
background-color: rgb(6,71,17);
}
[data-testid="stHeader"]{
    background-color : rgba(0,0,0,0)
    
}
[data-testid="stSidebar"]{
background-image: url("https://images.unsplash.com/photo-1483401757487-2ced3fa77952?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=873&q=80");
background-size:cover;
background-repeat: no-repeat;
}
[data-testid="stImage"] > img{
border-radius:50%;

}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

data = pd.read_csv("GOD'sDATA.csv")


st.title("Welcome to My" )
st.header("Data Overview")

st.write(data)




