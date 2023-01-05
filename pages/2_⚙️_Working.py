import streamlit as st
import tensorflow as tf
import keras
from matplotlib import pyplot as plt

st.set_page_config(
    page_title = "Working",
    page_icon = "⚙️",
    layout = "wide",
)

st.title("How this application works")
st.header("Ship Detection")
st.write("""
The ship-detection part of the project makes use of a Deep Neural Network Architecture called **Convolutional Neural Network (CNN)** which included multiple **Convolutional layers (Conv2D with 3x3 filters)** followed by **Max Pooling Layers (2x2)**. This was then Flattened and attached to a **Fully Connected Dense layer** of **512** neurons before being passed to the output layer of 1 neuron that used `Sigmoid` function as the activation.

`ReLU` i.e. Rectified Linear Unit was used as the activation for all the layers except the last because it is known to perform well on Computer Vision tasks such as this one.

**TensorFlow** and **Keras** have been utilized for the **data augmentation, compiling, training and testing of the model**. The dataset used for training can be found [here](https://www.kaggle.com/datasets/apollo2506/satellite-imagery-of-ships)

Attaching the code snippets below!
""")


st.subheader("Model")
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

st.subheader("Data augmentation")
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


st.subheader("Model Summary")


st.markdown("""
Total parameters: `831,681` \n
Trainable parameters: `831,681` \n
Non-trainable parameterss: `0` \n""")

st.subheader("Accuracy")
st.image('accuracy.png')

"""Training accuracy peaks at about `97%`

Validation accuracy peaks at around `98%`"""

st.header("MPA intrustion detection")

st.write("""The main idea behind this to detect unauthorised vessels entering in these protected sites.

**Libraries used:** GeoJSON, Shapely, Folium""")

st.subheader("Map")
st.write("""`Folium` and `streamlit-folium` have been used to render the interactive map and plot coordinates. `Folium` also makes it possible to GeoJSON data to mark Marine Protected Areas.

`GeoJSON` is used to handle geospatial data. More specifically, we are using and parsing GeoJSON data to mark MPA boundaries on our maps. Currently we only have 1 MPA data obtained from the New Zealand government website and more will be added soon.""")

st.code("""
with open('Marine_Protected_Areas_under_the_Marine_Management_Act.geojson') as f:
    geojson_file = geojson.load(f)""")

st.code("""
if latitude and longitude:
        
        map = folium.Map(location = [longitude, latitude], zoom_start = 5)
        
        choropleth = folium.Choropleth(
            geo_data = './Marine_Protected_Areas_under_the_Marine_Management_Act.geojson'
        )
        
        choropleth.geojson.add_to(map)
        folium.Marker([latitude,longitude]).add_to(map)

        st_map = st_folium(map, width = 700, height = 450)""")

st.subheader("is_mpa")

st.write("""Upon entering the necessary details a function `is_mpa` is called that takes these user entered coordinates and converts them to `shapely.Point` object. This is particularly useful as the MPA boundaries are considered to be polygons. It is then only a geometry problem. See the code snippet below:
""")

st.code("""
def is_mpa(longitude, latitude):
      # Creating a Shapely point from the latitude and longitude
  point = Point(longitude, latitude)

  # Iterating through the features in the GeoJSON file
  for feature in geojson_file['features']:
    # Checking if the point is within the polygon defined by the feature
    if Point(point).within(Polygon(feature['geometry']['coordinates'][0])):
        return True

""")

st.write("The entire code of this project can be found here: https://github.com/jaygala223/ship-detection")