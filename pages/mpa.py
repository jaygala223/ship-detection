import streamlit as st
import pandas as pd

st.title("Checking for possible MPA intrusion")

st.write("Enter the coordinates, time and date of the image uploaded")

time = st.time_input("Time of clicking the image")

st.date_input("Enter the date of clicking the image")

latitude = st.number_input("Enter latitude: (in decimal degree format)", key = 'latitude')
longitude = st.number_input("Enter longitude: ", key = 'longitude')

# point_conception = {"LAT":[
# 34° 27.00' N. lat,
# "34° 27.00' N. lat",
# "34° 23.96' N. lat",
# "34° 27.19' N. lat"], 

# "LON":["120° 28.28' W. long", "120° 32.15' W. long", "120° 25.00' W. long", "120° 25.00' W. long"],
# }

# mpa_df = pd.DataFrame(point_conception)

# st.map(mpa_df)
st.map(pd.DataFrame({'latitude': [latitude], 'longitude': [longitude]}))