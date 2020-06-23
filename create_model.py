import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

#Load the dataset
mnist = keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#Normalize and round values (from 0 to 0.5 -> 0 and from 0.5 to 1 -> 1)
X_train = keras.utils.normalize(X_train, axis=1)
X_test = keras.utils.normalize(X_test, axis=1)

# Convert binary numbers
for elem in X_train:
    for i in range(28):
        for j in range(28):
            if elem[i][j] != 0:
                elem[i][j] = 1

# Create an ANN
model = keras.Sequential()

# Input layer
model.add(keras.layers.Flatten())

# 1-n layers
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dense(10, activation=tf.nn.softmax))

# Compilation
model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics=["accuracy"])

# Training
model.fit(X_train, y_train, epochs=5)

# Evaluation
test_loss, test_acc = model.evaluate(X_test, y_test)

# Save model
keras.models.save_model(model, "number_guesser.hp5", save_format="h5")

print("Done with acc: ", test_acc)