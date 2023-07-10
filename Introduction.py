import streamlit as st
import pandas as pd
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Analysis of selected Socio-Economic Issues in ASEAN",
    page_icon=":wave:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define background images and styles
page_bg_img = '''
<style>
body {
    background-image: url("https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=871&q=80");
    background-size: cover;
    background-repeat: no-repeat;
}

.sidebar .sidebar-content {
    background-image: url("https://images.unsplash.com/photo-1486520299386-6d106b22014b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=869&q=80");
    background-size: cover;
    background-repeat: no-repeat;
    border-radius: 10px;
    padding: 20px;
}

.stImage > img {
    border-radius: 50%;
    width: 150px;
}

</style>
'''

# Apply background styles
st.markdown(page_bg_img, unsafe_allow_html=True)

# Display title and header
st.title("Analysis of Selected Socio-Economic Issues in ASEAN")
st.header("Using Python, CSS, and HTML for Plotting")

# Display an image
image = Image.open('ASEAN Welcome page.jpg')
st.image(image, caption='Sunrise by the mountains')

# Add interactive elements to your app
selected_option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])

if selected_option == "Option 1":
    st.write("You selected Option 1.")
elif selected_option == "Option 2":
    st.write("You selected Option 2.")
else:
    st.write("You selected Option 3.")

# Add plots, tables, or any other content you want

# Finally, run your Streamlit app
if __name__ == "__main__":
    main()
