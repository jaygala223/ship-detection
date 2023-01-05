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

with open('Marine_Protected_Areas_under_the_Marine_Management_Act.geojson') as f:
    geojson_file = geojson.load(f)

# st.write(geojson_file['features'][0])
st.title("MPA intrusion detection")

st.write("""

**Marine protected areas (MPA)** are protected areas of seas, oceans, estuaries or in the US, the Great Lakes. These marine areas can come in many forms ranging from wildlife refuges to research facilities. MPAs **restrict human activity for a conservation purpose**, typically to protect natural or cultural resources. Such marine resources are protected by local, state, territorial, native, regional, national, or international authorities and differ substantially among and between nations. This variation includes different limitations on **development, fishing practices, fishing seasons and catch limits, moorings and bans on removing or disrupting marine life**. (**Source**: [Wikipedia](https://en.wikipedia.org/wiki/Marine_protected_area))

""")


col1, col2 = st.columns(2)

with col1:
    st.write("**Enter the coordinates, time and date of the image uploaded**")

    time = st.time_input("**Time of clicking the image**")

    date = st.date_input("**Enter the date of clicking the image**")

    longitude = st.number_input("**Enter longitude: (in decimal degree format)**", key = 'latitude')
    latitude = st.number_input("**Enter latitude: (in decimal degree format)**", key = 'longitude')

    # coordinates = st.text_input("Enter Latitude and Longitude in decimal degree format: Example: -6.25, 8.33")


    # st.write(coordinates)

    check_mpa = st.button("**Check for MPA intrustion**", )

def is_mpa(longitude, latitude):
  # Creating a Shapely point from the latitude and longitude
  point = Point(longitude, latitude)

  # Iterating through the features in the GeoJSON file
  for feature in geojson_file['features']:
    # Checking if the point is within the polygon defined by the feature
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
                if is_mpa(longitude, latitude):
                    st.success("Point is in a Marine Protected Region. See how this works [here](Working)")
                else:
                    st.info("Point lies outside a Marine Protected Region. See how this works [here](Working)")
    else:
        st.error("All above fields are required. Please fill them up and try again!")

with col2:
    if latitude and longitude:
        
        map = folium.Map(location = [longitude, latitude], zoom_start = 5)
        
        choropleth = folium.Choropleth(
            geo_data = './Marine_Protected_Areas_under_the_Marine_Management_Act.geojson'
        )
        
        choropleth.geojson.add_to(map)
        folium.Marker([latitude,longitude]).add_to(map)

        st_map = st_folium(map, width = 700, height = 450)