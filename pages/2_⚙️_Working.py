import streamlit as st
import tensorflow as tf
import keras
from matplotlib import pyplot as plt

st.set_page_config(
    page_title = "Working",
    page_icon = "⚙️",
)

st.title("How this application works")



st.write("""
This project makes use of a Deep Neural Network Architecture called Convolutional Neural Network (CNN) which included multiple Convolutional layers (Conv2D with 3x3 filters) followed by Max Pooling Layers (2x2). This was then Flattened and attached to a Fully Connected layer of 512 neurons before being passed to the output layer of 1 neuron that used `Sigmoid` function as the activation. 

`ReLU` i.e. Rectified Linear Unit was used as the activation for all the layers except the last because it is known to perform well on Computer Vision tasks such as this one.

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


st.header("Model Summary")


st.markdown("""
Total parameters: `831,681` \n
Trainable parameters: `831,681` \n
Non-trainable parameterss: `0` \n""")

st.header("Accuracy")
st.image('accuracy.png')

st.write("The entire code of this project can be found here: https://github.com/jaygala223/ship-detection")