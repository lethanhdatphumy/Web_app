import streamlit as st
from streamlit_folium import folium_static
import folium

# Set page configuration
st.set_page_config(
    page_title="ASEAN Map",
    page_icon=":world_map:",
    
)

# Display title and header
st.title("ASEAN Map")
st.header("Interactive Map of ASEAN Countries")
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

</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
# Create a map centered around ASEAN
map_asean = folium.Map(location=[1.35, 103.8], zoom_start=5, control_scale=True)

# Define ASEAN country coordinates
country_coordinates = {
    "Brunei": (4.5353, 114.7277),
    "Cambodia": (12.5657, 104.9910),
    "Indonesia": (-0.7893, 113.9213),
    "Laos": (19.8563, 102.4955),
    "Malaysia": (4.2105, 101.9758),
    "Myanmar": (21.9162, 95.9560),
    "Philippines": (12.8797, 121.7740),
    "Singapore": (1.3521, 103.8198),
    "Thailand": (15.8700, 100.9925),
    "Vietnam": (14.0583, 108.2772)
}

# Define colors for each country
country_colors = {
    "Brunei": "green",
    "Cambodia": "blue",
    "Indonesia": "red",
    "Laos": "orange",
    "Malaysia": "purple",
    "Myanmar": "yellow",
    "Philippines": "pink",
    "Singapore": "darkblue",
    "Thailand": "lightgreen",
    "Vietnam": "darkred"
}

# Add markers for each ASEAN country with assigned colors
for country, coordinates in country_coordinates.items():
    color = country_colors.get(country, "green")
    folium.Marker(
        location=coordinates,
        tooltip=country,
        icon=folium.Icon(color=color, icon="info-sign")
    ).add_to(map_asean)

# Display the map
folium_static(map_asean)
