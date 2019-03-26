from __future__ import print_function
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout
import pickle
import os

class NeuralNetwork:

    def __init__(self, batch_size):
        self.batch_size = batch_size
        self.model = Sequential()
        self.model.add(Dense(self.batch_size, activation='relu', input_shape=(5,)))
        self.model.add(Dense(30, activation='relu'))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam',
                           loss='mse')
        self.fit = None

    def train(self, input, real, number):
        fit = self.model.fit(input, real,validation_split=0.2, epochs=100)
        fit.history['title'] = number
        loss, = plt.plot(fit.history['loss'], label="Loss")
        val_loss, = plt.plot(fit.history['val_loss'], label="Validation Loss")
        plt.legend(handles=[loss, val_loss])
        plt.title('Loss vs Epoch (' + str(number) + ')')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.show()

        if os.path.exists("./history"):
            os.remove("./history")
        if os.path.exists("./model.h5"):
            os.remove("./model.h5")

        with open('./history', 'wb') as hist:
            pickle.dump(fit.history, hist)
        hist.close()

        self.model.save("./model.h5")

    def predict_calorie(self, test):
        test_fix = []
        for l in test:
            for e in l:
                test_fix.append(int(e))
        test_array = np.array(test_fix)
        test_array = np.expand_dims(test_array,axis=0)

        test_output = self.model.predict(test_array, batch_size=1)
        return test_output