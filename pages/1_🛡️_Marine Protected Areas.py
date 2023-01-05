import streamlit as st
import pandas as pd
import geojson
import folium
from streamlit_folium import st_folium
from shapely.geometry import Point, Polygon
import re

st.set_page_config(
    page_title = "MPA",
    page_icon = "🛡️",
    layout = "wide",
)

with open('map_experiment.geojson') as f:
    geojson_file = geojson.load(f)

st.write(geojson_file['features'][0])
st.title("Checking for possible MPA intrusion")

col1, col2 = st.columns(2)

with col2:
    st.write("Enter the coordinates, time and date of the image uploaded")

    time = st.time_input("Time of clicking the image")

    date = st.date_input("Enter the date of clicking the image")

    latitude = st.number_input("Enter latitude: (in decimal degree format)", key = 'latitude')
    longitude = st.number_input("Enter longitude: (in decimal degree format)", key = 'longitude')

    # coordinates = st.text_input("Enter Latitude and Longitude in decimal degree format: Example: -6.25, 8.33")


    # st.write(coordinates)

    check_mpa = st.button("Check for MPA intrustion")

def is_mpa(latitude, longitude):
    # Create a Shapely point from the latitude and longitude
  point = Point(latitude, longitude)

  # Iterate through the features in the GeoJSON file
  for feature in geojson_file['features']:
    # Check if the point is within the polygon defined by the feature
    if Point(point).within(Polygon(feature['geometry']['coordinates'][0])):
      return True

  # If the point is not within any of the polygons, return False
  return False

def regex_okay(coordinates):
    return True

def parse_coordinates(coordinates):
    coordinates = coordinates.split(',')
    latitude = float(coordinates[0])
    longitude = float(coordinates[1])

    return latitude, longitude

# latitude, longitude = parse_coordinates(coordinates)

if check_mpa:
    if date and time and latitude and longitude:
    # if date and time and coordinates:
        # if regex_okay(coordinates):
            
            with st.spinner("Checking for possible MPA intrusion"):
                if is_mpa(latitude, longitude):
                    st.sucess("Point is in a Marine Protected Region")
                else:
                    st.info("Point lies outside a Marine Protected Region")
                st.write("woopie")
    else:
        st.error("All above fields are required. Please fill them up and try again!")

with col1:
    if latitude and longitude:
        map = folium.Map(location = [latitude, longitude], zoom_start = 5)
        
        # folium.Marker([latitude,latitude]).add_to(map)
        st.write(f"{latitude}, {longitude}")
        choropleth = folium.Choropleth(
            geo_data = './map.geojson'
        )
        choropleth.geojson.add_to(map)


        st_map = st_folium(map, width = 700, height = 450)


st.info("See how this works [here](Working)")