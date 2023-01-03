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

st.write("""Illegal Fishing is a serious problem plaguing our oceans and marine life for years. We now have a solution thanks to the breakthroughs in Deep Learning techniques. With this project I hope to come one step closer to stopping **illegal fishing** for good!""")


st.write("""The dataset used for training can be found here https://www.kaggle.com/datasets/rhammell/ships-in-satellite-imagery""")


st.write("""
A clear plan for this project:
1. Allow users to upload images
2. run a CNN
3. Display prediction

3.1. additional pts
4. show eda via graphs, plots, df, etc.
5. read about marine protected areas (MPA)
6. implement a is_mpa() function that can take coordinates and 
if ship == detected and is_mpa:
    report to authorities 
7. add a page to explain what is the architecture and how is the app working.
""")

uploaded_image = st.file_uploader("Upload satellite images here", type = ['jpg', 'jpeg', 'png'])

def prediction(uploaded_image):
    model = keras.models.load_model('./new_model.h5')
    
    uploaded_image = tf.keras.preprocessing.image.load_img(uploaded_image, target_size=(80,80), color_mode = 'rgb')
    uploaded_image = tf.keras.utils.img_to_array(uploaded_image)
    uploaded_image = uploaded_image/255.0
    uploaded_image = np.reshape(uploaded_image, [1,80,80,3])

    predictions = model.predict(uploaded_image)
    print(type(predictions))
    st.write(predictions)


def load_image(image_file):
    img = Image.open(image_file)
    return img

if uploaded_image is not None:
    #file details
	file_details = {
        "filename": uploaded_image.name, 
        "filetype": uploaded_image.type,
        "filesize": uploaded_image.size}

	st.caption(file_details)

    # To View Uploaded Image
	st.image(load_image(uploaded_image), caption = f"Filename: {uploaded_image.name}", width=250)

button = st.button('Predict')

    
if button:
    if uploaded_image:
        prediction(uploaded_image)
    else:
        st.error('Please upload an image first!')