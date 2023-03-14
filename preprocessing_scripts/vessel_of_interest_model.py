import tensorflow as tf
import keras
import pickle as pkl
# import sklearn
import pandas as pd

df = [{
        "gap_hours":0.03,
        "spherical_distances":2.4863940766127923,
        "eez_check":1,
        "speed":82.87980255375975,
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

def predict_vessel_of_interest(dataframe):

    model = pkl.load(open('preprocessing_scripts\logistic_regression_model.h5', 'rb'))

    preds = model.predict(dataframe)
    return preds[0]
    

# predict_vessel_of_interest(pd.DataFrame(tp_df))

# print(pd.DataFrame.from_dict(tp_df))

# predict_vessel_of_interest(pd.DataFrame.from_dict(df))