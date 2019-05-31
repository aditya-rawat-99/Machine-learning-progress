import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import keras
from keras import backend as k
from keras.models import Sequential
from keras.layers import Activation
from keras.layers.core import Dense
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


X = np.random.randn(1000,2)
y = np.logical_xor(X[:,0]<0, X[:,1]<0)
y = np.where(y,1,0)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.1, random_state = 1)

model = Sequential()
model.add(Dense(20, input_shape = (2,),activation = "relu"))
model.add(Dense(10, activation = "relu"))
model.add(Dense(2, activation = "softmax"))

model.compile(optimizer = Adam(lr = 0.001),
               loss = keras.losses.sparse_categorical_crossentropy,
               metrics = ["accuracy"])

model.fit(X_train,y_train, batch_size = 110, epochs = 50, 
          shuffle = True,
          verbose = True)

# Only be used one time
import pickle
file = open("/home/aditya/Desktop/File.pickle","wb")
pickle.dump(model, file)

model = pickle.load(open("/home/aditya/Desktop/File.pickle","rb"))

y_pred = np.argmax(model.predict(X_test),axis = 1)
print(accuracy_score(y_test, y_pred))