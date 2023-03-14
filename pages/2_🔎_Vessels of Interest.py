import streamlit as st
from preprocessing_scripts.spherical_distance import calculate_spherical_distance
from preprocessing_scripts.eez_check import eez_check
from preprocessing_scripts.time_of_day import find_time_of_day
from preprocessing_scripts.vessel_of_interest_model import predict_vessel_of_interest
import pandas as pd
import time

st.set_page_config(
    page_title = "Vessels of Interest",
    page_icon = "🔎",
    layout = "wide",
)

gap_hours = st.number_input('Enter gap hours', key = 'start_time')

start_latitude = st.number_input('Enter latitude when AIS was disabled (in decimal degrees):', key = 'start_latitude')

start_longitude = st.number_input('Enter longitude when AIS was disabled (in decimal degrees):', key = 'start_longitude')

end_latitude = st.number_input('Enter latitude when AIS was re-enabled (in decimal degrees):', key = 'end_latitude')

end_longitude = st.number_input('Enter longitude when AIS was re-enabled (in decimal degrees):', key = 'end_longitude')

dist_from_shore = st.number_input('Enter distance from shore (in meters):')

gear_type = st.selectbox('Select gear type from the following:', ['dredge_fishing', 'drifting_longlines', 'fishing', 'fixed_gear', 'other', 'other_purse_seines', 'other_seines', 'pole_and_line', 'pots_and_traps', 'purse_seines', 'seiners', 'set_gillnets', 'set_longlines', 'squid_jigger', 'trawlers', 'trollers', 'tuna_purse_seines'])

start_time = st.time_input('Enter time of AIS disabling event:')

ocean_name = st.selectbox('Enter ocean name: ', ['North Atlantic Ocean', 'South Atlantic Ocean' ,'Celtic Sea',
 'Southern Ocean' ,'Mediterranean Sea - Eastern Basin', 'Norwegian Sea',
 'Barentsz Sea', 'Sea of Okhotsk', 'Japan Sea', 'Bering Sea' ,'Gulf of Alaska',
 'Labrador Sea', 'Davis Strait', 'North Pacific Ocean' ,'South Pacific Ocean',
 'Arafura Sea' ,'Arabian Sea' ,'Indian Ocean' ,'Tasman Sea' ,'Bismarck Sea',
 'Gulf of Guinea', 'Coral Sea' 'Bay of Bengal' 'Great Australian Bight',
 'Mozambique Channel', 'Caribbean Sea', 'Philippine Sea', 'Timor Sea',
 'Greenland Sea' ,'North Sea' ,'Laccadive Sea', 'Bass Strait',
 'Gulf of St. Lawrence' ,'Baffin Bay', 'Gulf of Mexico', 'Solomon Sea'])

predict = st.button('Predict')

if predict:
    if start_latitude and end_latitude and ocean_name and start_time and gap_hours and gear_type and dist_from_shore and start_longitude and end_longitude:
        
        spherical_distance = calculate_spherical_distance(start_latitude, start_longitude, end_latitude, end_longitude)

        eez_check = eez_check(dist_from_shore)

        speed = spherical_distance/ gap_hours

        ais_disable_time_division = find_time_of_day(str(start_time))

        
        df = [{
        "gap_hours":gap_hours,
        "spherical_distances":spherical_distance,
        "eez_check":eez_check,
        "speed":speed,
        "gear type_dredge_fishing": 0,
        "gear type_drifting_longlines": 0,
        "gear type_fishing": 0,
        "gear type_fixed_gear": 0,
        "gear type_other": 0,
        "gear type_other_purse_seines": 0,
        "gear type_other_seines": 0,
        "gear type_pole_and_line": 0, 
        "gear type_pots_and_traps": 0,
        "gear type_purse_seines": 0,
        "gear type_seiners": 0,
        "gear type_set_gillnets": 0,
        "gear type_set_longlines": 0,
        "gear type_squid_jigger": 0,
        "gear type_trawlers": 0,
        "gear type_trollers": 0,
        "gear type_tuna_purse_seines": 0,
        "exact _name new from diff Oceans_Arabian Sea": 0,
        
        "exact _name new from diff Oceans_Arafura Sea": 0,

        "exact _name new from diff Oceans_Baffin Bay": 0,

        "exact _name new from diff Oceans_Barentsz Sea": 0,

        "exact _name new from diff Oceans_Bass Strait": 0,

        "exact _name new from diff Oceans_Bay of Bengal": 0,
        
        "exact _name new from diff Oceans_Bering Sea": 0,

        "exact _name new from diff Oceans_Bismarck Sea": 0,

        "exact _name new from diff Oceans_Caribbean Sea": 0,

        "exact _name new from diff Oceans_Celtic Sea": 0,

        "exact _name new from diff Oceans_Coral Sea": 0,

        "exact _name new from diff Oceans_Davis Strait": 0,

        "exact _name new from diff Oceans_Great Australian Bight": 0,

        "exact _name new from diff Oceans_Greenland Sea": 0,

        "exact _name new from diff Oceans_Gulf of Alaska": 0,

        "exact _name new from diff Oceans_Gulf of Guinea": 0,

        "exact _name new from diff Oceans_Gulf of Mexico": 0,

        "exact _name new from diff Oceans_Gulf of St. Lawrence": 0,

        "exact _name new from diff Oceans_Indian Ocean": 0,

        "exact _name new from diff Oceans_Japan Sea": 0,

        "exact _name new from diff Oceans_Labrador Sea": 0,

        "exact _name new from diff Oceans_Laccadive Sea": 0,

        "exact _name new from diff Oceans_Mediterranean Sea - Eastern Basin": 0,

        "exact _name new from diff Oceans_Mozambique Channel": 0,

        
        "exact _name new from diff Oceans_North Atlantic Ocean": 0,

        "exact _name new from diff Oceans_North Pacific Ocean": 0,

        "exact _name new from diff Oceans_North Sea": 0,

        "exact _name new from diff Oceans_Norwegian Sea": 0,

        "exact _name new from diff Oceans_Philippine Sea": 0,

        "exact _name new from diff Oceans_Sea of Okhotsk": 0,

        "exact _name new from diff Oceans_Solomon Sea": 0,
        
        "exact _name new from diff Oceans_South Atlantic Ocean": 0,
        
        "exact _name new from diff Oceans_South Pacific Ocean": 0,

        "exact _name new from diff Oceans_Southern Ocean": 0,
        
        "exact _name new from diff Oceans_Tasman Sea": 0,
        
        "exact _name new from diff Oceans_Timor Sea": 0,
        
        "ais_disable_time_division_Afternoon": 0,
        
        "ais_disable_time_division_Dawn":0,
        
        "ais_disable_time_division_Evening": 0,
        
        "ais_disable_time_division_Morning": 0,
        
        "ais_disable_time_division_Night": 0,
        
        "ais_disable_time_division_Twilight": 0,        
}]
        
        #add time
        df[0][f'ais_disable_time_division_{ais_disable_time_division}'] = 1

        #add gear type
        df[0][f"gear type_{gear_type}"] = 1

        #add ocean/sea
        df[0][f"exact _name new from diff Oceans_{ocean_name}"] = 1
        
        # st.write(df)

        

        with st.spinner("Checking for possible IUU activity"):
            time.sleep(2)
            if predict_vessel_of_interest(pd.DataFrame.from_dict(df)):
                st.success("The vessel could be a potential vessel of interest!")
            else:
                st.info("The vessel has a low likelihood of being a vessel of interest")

    else:
        st.error('All above fields are mandatory. Please enter values for all and try again.')

    