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
    layout = "wide",
)

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

st.title("""Ship Detection 
[![](https://img.shields.io/github/stars/jaygala223/ship-detection?style=social)](https://github.com/jaygala223/ship-detection)""")

st.write(
    '<style>button[title="View fullscreen"], h4 a {display: none !important} [data-testid="stImage"] img {border: 1px solid #D6D6D9; border-radius: 3px; height: 200px; object-fit: cover; width: 100%} .block-container img:hover {}</style>',
    unsafe_allow_html=True,
)

st.write("""Oceans support the livelihoods of an estimated 520 million people who rely on fishing and fishing related activities, and 2.6 billion people who depend on fish as an important part of their diet. But Illegal fishing is threatening the food supply of coastal communities as fish populations decline due to overfishing in areas fishers are not permitted to access. Addressing illegal fishing will positively contribute to the equitable growth and empowerment of the people who rely on oceans for food and income. """)


st.write("""We now have a solution thanks to the breakthroughs in Deep Learning techniques. With this project we hope to come one step closer to stopping **illegal fishing** for good!""")


col1, col2 = st.columns(2)

with col1:
    st.subheader("Steps to use this project:")
    st.write("""
    1. Upload satellite images
    2. Click the predict button and wait for the Deep Learning algorithm to produce a result""")

    # st.warning("Coming soon!")
    st.info("""Coming soon!""")

    st.write("""3. Additionally, if the image is detected to be a ship you can check whether it was in a Marine Protected Region by clicking [here](Marine_Protected_Areas).
    """)

st.sidebar.info("""Code: [jaygal223/ship-detection](https://github.com/jaygala223/ship-detection)\n
Linkedin:  [@jaykishorgala](https://www.linkedin.com/in/jaykishorgala)\n
Leetcode: [@jaygala223](https://www.leetcode.com/jaygala223) \n

""")


# TODO for me:
# 3.1. additional pts
# 4. show eda via graphs, plots, df, etc.
# 5. read about marine protected areas (MPA)
# 6. implement a is_mpa() function that can take coordinates and 
# if ship == detected and is_mpa:
#     report to authorities 
# 7. add a page to explain what is the architecture and how is the app working.

with col2:

    uploaded_image = st.file_uploader("**Upload satellite images here**", type = ['jpg', 'jpeg', 'png'])

    if uploaded_image is not None:
        #file details
	# file_details = {
        # "filename": uploaded_image.name, 
        # "filetype": uploaded_image.type,
        # "filesize": uploaded_image.size}

	# st.caption(file_details)

    # To View Uploaded Image
        st.image(load_image(uploaded_image), caption = f"Filename: {uploaded_image.name}", width=250)

    button = st.button('Predict', key = 'predict')

    
    if button:
        if uploaded_image:
            with col1:
                with st.spinner("Predicting..."):
                    prediction(uploaded_image)
        else:
            st.error('Please upload an image first!')






st.components.v1.html("""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>""")