import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "MPA",
    page_icon = "🛡️",
)

st.title("Checking for possible MPA intrusion")

st.write("Enter the coordinates, time and date of the image uploaded")

time = st.time_input("Time of clicking the image")

date = st.date_input("Enter the date of clicking the image")

latitude = st.number_input("Enter latitude: (in decimal degree format)", key = 'latitude')
longitude = st.number_input("Enter longitude: (in decimal degree format)", key = 'longitude')

def is_mpa(latitude, longitude):
    import time
    time.sleep(5)

# st.map(mpa_df)
st.map(pd.DataFrame({'latitude': [latitude], 'longitude': [longitude]}))

mpa = st.button("Check for MPA")

if mpa:
    if date and time and latitude and longitude:
        with st.spinner("Checking for possible MPA intrusion"):
            
            is_mpa(latitude, longitude)
    else:
        st.error("All above fields are required. Please fill them up and try again!")