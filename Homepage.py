import streamlit as st
import pandas as pd
from PIL import Image
from pandas import options

st.set_page_config(
    page_title="",
    page_icon=":wave:",
)

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]  {
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size:cover;
background-repeat: no-repeat;
}
[data-testid="stHeader"]{
    background-color : rgba(0,0,0,0)
    
}
[data-testid="stSidebar"]{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size:cover;
background-repeat: no-repeat;
}
[data-testid="stImage"] > img{
border-radius:50%;

}
[data-testid="stImage"]{
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)




data = pd.read_csv("GOD'sDATA.csv")
data.columns = data.columns.str.strip()
data["Year"] = pd.to_numeric(data["Year"])
data["Year"] = data["Year"].astype(int)
options.display.float_format = '{:.0f}'.format

st.title("Welcome to My")
st.header("Data Overview")





st.sidebar.markdown("## Sidebar")
st.sidebar.info("Select pages above <3")
