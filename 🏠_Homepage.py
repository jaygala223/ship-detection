import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import tensorflow as tf
import keras
# from model import model

st.set_page_config(
    page_title = "Ship detection",
    page_icon = "🛳️",
)

st.title("""
Ship Detection
""")

st.write("""Oceans support the livelihoods of an estimated 520 million people who rely on fishing and fishing related activities, and 2.6 billion people who depend on fish as an important part of their diet. But Illegal fishing is threatening the food supply of coastal communities as fish populations decline due to overfishing in areas fishers are not permitted to access. Addressing illegal fishing will positively contribute to the equitable growth and empowerment of the people who rely on oceans for food and income. """)


# st.metric("Illegal", value = 5)


st.write("""We now have a solution thanks to the breakthroughs in Deep Learning techniques. With this project we hope to come one step closer to stopping **illegal fishing** for good!""")


st.write("""The dataset used for training can be found here: https://www.kaggle.com/datasets/apollo2506/satellite-imagery-of-ships""")


st.write("""
Steps to use this project:
1. Upload satellite images
2. Click the predict button and wait for the Deep Learning algorithm to produce a result
3. Display prediction
4. Additionally, if the images is detected to be a ship you can check whether it was in a Marine Protected Region
""")

# TODO for me:
# 3.1. additional pts
# 4. show eda via graphs, plots, df, etc.
# 5. read about marine protected areas (MPA)
# 6. implement a is_mpa() function that can take coordinates and 
# if ship == detected and is_mpa:
#     report to authorities 
# 7. add a page to explain what is the architecture and how is the app working.

uploaded_image = st.file_uploader("Upload satellite images here", type = ['jpg', 'jpeg', 'png'])

def prediction(uploaded_image):
    model = keras.models.load_model('./new_model.h5')
    
    uploaded_image = tf.keras.preprocessing.image.load_img(uploaded_image, target_size=(80,80), color_mode = 'rgb')
    uploaded_image = tf.keras.utils.img_to_array(uploaded_image)
    uploaded_image = uploaded_image/255.0
    uploaded_image = np.reshape(uploaded_image, [1,80,80,3])

    predictions = model.predict(uploaded_image)
    # print(type(predictions))

    st.write("Output probability: ", predictions[0][0])

    if predictions[0][0] >= 0.4:
        st.success("The uploaded image appears to contain a ship")
    else:
        
        st.error("The uploaded image appears to contain no ship")


def load_image(image_file):
    img = Image.open(image_file)
    return img

if uploaded_image is not None:
    #file details
	# file_details = {
        # "filename": uploaded_image.name, 
        # "filetype": uploaded_image.type,
        # "filesize": uploaded_image.size}

	# st.caption(file_details)

    # To View Uploaded Image
	st.image(load_image(uploaded_image), caption = f"Filename: {uploaded_image.name}", width=250)

button = st.button('Predict')

    
if button:
    if uploaded_image:
        prediction(uploaded_image)
    else:
        st.error('Please upload an image first!')