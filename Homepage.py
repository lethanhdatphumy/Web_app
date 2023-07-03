import streamlit as st
import pandas as pd

# Set page title and icon
st.set_page_config(
    page_title="My Data Overview",
    page_icon=":wave:"
)

# Set background image using CSS
page_bg_img = '''
<style>
body {
    background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
    background-size: cover;
    background-repeat: no-repeat;
}

.stSidebar {
    background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
    background-size: cover;
    background-repeat: no-repeat;
}

.stImage > img {
    border-radius: 50%;
}

</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Disable the thousands comma
pd.set_option('display.float_format', '{:.0f}'.format)

# Load the data
data = pd.read_csv("GOD'sDATA.csv")
data.columns = data.columns.str.strip()

# Main content
st.title("Welcome to My Data Overview")
st.header("Data Overview")
st.write(data)

# Sidebar
st.sidebar.markdown("## Sidebar")
st.sidebar.info("Select pages above ❤️")
