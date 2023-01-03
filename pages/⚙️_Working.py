import streamlit as st

st.set_page_config(
    page_title = "Working",
    page_icon = "⚙️",
)

st.title("How this application works")



st.write("""
This project makes use of a Deep Neural Network Architecture called Convolutional Neural Network (CNN).

TensorFlow and Keras have been utilized for the data augmentation, compiling, training and testing of the model.

Attaching the code snippets below!
""")


st.header("Model")
st.code("""
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(80, 80, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(lr=1e-4),
              metrics=['accuracy'])
""")

st.header("Data augmentation")
st.code("""train_datagen = ImageDataGenerator(
    rescale=1.0/255, 
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.5,
    zoom_range=0.5,
    horizontal_flip=True,
    fill_mode='nearest')
""")

import tensorflow as tf
import keras
model = tf.keras.models.load_model('new_model.h5')

print(model.summary)