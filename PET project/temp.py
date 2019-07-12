import os
from keras.models import load_model
import numpy as np
from keras.preprocessing import image
from keras.applications.inception_v3 import preprocess_input

model = load_model("cats_and_dogs_model.h5")

def predict(input_image):
    i = input_image
    img = image.load_img(i,target_size = (299,299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)
    x = preprocess_input(x)
    percentage = model.predict(x, steps = 1)
    pred = np.argmax(model.predict(x,steps = 1), axis = 1)
    return pred
