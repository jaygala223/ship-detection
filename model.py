import json
import pickle
import pandas as pd
import numpy as np
import tensorflow as tf
import keras
# from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
from tensorflow.keras.optimizers import RMSprop,Adam

with open('F:/JAY/13. SHIP CLASSIFICATION PERSONAL PROJECT/data/shipsnet/shipsnet.json') as data_file:
    dataset = json.load(data_file)
shipsnet = pd.DataFrame(dataset)
print(shipsnet.head())

# st.write("Showing the head of the dataset:",shipsnet.head())

size_of_image = len(shipsnet['data'].iloc[0])


ship_images = shipsnet["labels"].value_counts()[0]
no_ship_images = shipsnet["labels"].value_counts()[1]

# Turning the json information into numpy array and then assign it as x and y variables
x = np.array(dataset['data']).astype('uint8')
y = np.array(dataset['labels']).astype('uint8')

x_reshaped = x.reshape([-1, 3, 80, 80])

x_reshaped = x.reshape([-1, 3, 80, 80]).transpose([0,2,3,1])
# x_reshaped.shape

y_reshaped = tf.keras.utils.to_categorical(y, num_classes=2)

y_reshaped.shape

image_no_ship = x_reshaped[y==0]
image_ship = x_reshaped[y==1]


#MODEL

x_reshaped = x_reshaped / 255
x_reshaped[0][0][0] # Normalized RGB values of the firs pixel of the first image in the dataset.

print(x_reshaped[0].shape)

# tf.reshape(x_reshaped, [-1, 80,80,3])

x_train_1, x_test, y_train_1, y_test = train_test_split(x_reshaped, y_reshaped, test_size = 0.20, random_state = 42)


x_train, x_val, y_train, y_val = train_test_split(x_train_1, y_train_1, test_size = 0.25, random_state = 42)


print("x_train shape",x_train.shape)
print("x_test shape",x_test.shape)
print("y_train shape",y_train.shape)
print("y_test shape",y_test.shape)
print("y_train shape",x_val.shape)
print("y_test shape",y_val.shape)


from keras import callbacks
model = keras.models.Sequential()
#
model.add(keras.layers.Conv2D(filters = 64, kernel_size = (4,4),padding = 'Same', 
                 activation ='relu', input_shape = (80,80,3)))
model.add(keras.layers.MaxPool2D(pool_size=(5,5)))
# model.add(keras.layers.Dropout(0.25))
#
model.add(keras.layers.Conv2D(filters = 32, kernel_size = (3,3),padding = 'Same', 
                 activation ='relu'))
model.add(keras.layers.MaxPool2D(pool_size=(3,3), strides=(1,1)))
# model.add(keras.layers.Dropout(0.25))
#
model.add(keras.layers.Conv2D(filters = 16, kernel_size = (2,2),padding = 'Same', 
                 activation ='relu'))
model.add(keras.layers.MaxPool2D(pool_size=(3,3), strides=(1,1)))
# model.add(keras.layers.Dropout(0.25))

# Fully connected
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(200, activation = "relu"))
# model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(150, activation = "relu"))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(150, activation = "relu"))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(50, activation = "relu"))
model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(2, activation = "sigmoid"))

# optimizer = Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999)
optimizer = Adam(learning_rate=0.001)

model.compile(optimizer = optimizer , loss = "categorical_crossentropy", metrics=["accuracy"])

earlystopping = callbacks.EarlyStopping(monitor ="val_loss", mode ="min", patience = 10, restore_best_weights = True)


datagen = tf.keras.preprocessing.image.ImageDataGenerator(
        featurewise_center=False,
        samplewise_center=False, 
        featurewise_std_normalization=False, 
        samplewise_std_normalization=False,  
        zca_whitening=False,
        rotation_range=5,  
        zoom_range = 0.1,
        width_shift_range=0.1,  
        height_shift_range=0.1,  
        horizontal_flip=False, 
        vertical_flip=False)  

datagen.fit(x_train)

history = model.fit(datagen.flow(x_train, y_train), epochs = 30, 
                    validation_data=(x_val, y_val), callbacks = [earlystopping])

# history = model.fit(x_train, y_train, epochs = 25, validation_data=(x_val, y_val), callbacks = [earlystopping])

# pickle.dump(model, open('my_model.h5', 'wb'))

# # loading dependency
# from sklearn import *

# sklearn.joblib.dump(model , 'model_jlib')

model.save('./saved_model1.h5')