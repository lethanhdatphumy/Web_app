import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="",
    page_icon=":wave:",
)
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]  {
background-image:url("https://i.pinimg.com/originals/8c/56/a9/8c56a962d578e97c357ddb761052d5ea.gif");
background-repeat: no-repeat;
background-position: center;
background-size:cover;

}
[data-testid="stHeader"]{
background-color : rgba(0,0,0,0)
    
}
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

st.markdown(page_bg_img, unsafe_allow_html=True)

data = pd.read_csv("GOD'sDATA.csv")


st.title("Welcome to My" )
st.header("Dataset ")
data["Year"] = data["Year"].astype(str)
st.write(data)

st.sidebar.markdown("## Sidebar")
st.sidebar.info("Select pages above <3")

