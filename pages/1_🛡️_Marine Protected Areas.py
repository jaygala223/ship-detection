import streamlit as st
import pandas as pd
import geojson
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title = "MPA",
    page_icon = "🛡️",
    layout = "wide"
)

st.title("Checking for possible MPA intrusion")

col1, col2 = st.columns(2)

with col2:
    st.write("Enter the coordinates, time and date of the image uploaded")

    time = st.time_input("Time of clicking the image")

    date = st.date_input("Enter the date of clicking the image")

    latitude = st.number_input("Enter latitude: (in decimal degree format)", key = 'latitude')
    longitude = st.number_input("Enter longitude: (in decimal degree format)", key = 'longitude')

    check_mpa = st.button("Check for MPA intrustion")

def is_mpa(latitude, longitude):
    import time
    time.sleep(5)

with col1:
    

    map = folium.Map(location = [latitude,longitude], zoom_start = 5)
    folium.Marker([latitude,latitude]).add_to(map)

    choropleth = folium.Choropleth(
        geo_data = './map.geojson'
    )
    choropleth.geojson.add_to(map)

    st_map = st_folium(map, width = 700, height = 450)



if check_mpa:
    if date and time and latitude and longitude:
        with st.spinner("Checking for possible MPA intrusion"):
            is_mpa(latitude, longitude)
            st.write("woopie")
    else:
        st.error("All above fields are required. Please fill them up and try again!")

st.info("See how this works [here](Working)")