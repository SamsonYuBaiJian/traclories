from weight_net import NeuralNetwork
## from cv_test import CVModel
from nlp_test import NLPModel
## from keras.applications.vgg16 import VGG16
## from annoy import AnnoyIndex
import pandas as pd
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
from gensim.models import Word2Vec
from gensim.similarities import WmdSimilarity
import nltk
import matplotlib.pyplot as plt
import sys
from keras.models import load_model
import os
import pickle
import tensorflow as tf

graph = tf.get_default_graph()

class NLPCheck:
    def __init__(self):
        name_list = []
        calorie_list = []
        ## image_list = []

        # load real data: must be consistent across models
        csv = "./info.csv"
        data = pd.read_csv(csv, error_bad_lines=False)
        data_size = len(data)
        for i in range(data_size):
            for n in data[['Name']].values[i]:
                name_list.append(n)
            for c in data[['Calories']].values[i]:
                calorie_list.append(c)
        ##    for im in data[['Image File Path']].values[i]:
        ##        image_list.append(im)


        # load nlp model
        self.nlp = NLPModel(data = data)
        self.nlp.train()
        print("\nNLP model trained!\n")

        ## load cv mode
        ## cv = CVModel(img_data = image_list, name_list = name_list, calorie_data = calorie_list)
        ## cv.train()
        ## print("\nCV model trained!\n")
        ## cv.save()
        ## cv.load()

        self.nn = NeuralNetwork(batch_size = len(name_list))

        if os.path.isfile('./model.h5') == True and os.path.isfile('./history') == True and len(sys.argv) == 1:
            self.nn.model = load_model('./model.h5')
            print("\nPretrained calorie NN loaded!\n")
        elif os.path.isfile('./model.h5') == True and os.path.isfile('./history') == True and sys.argv[1] != '-train':
            if sys.argv[1] == '-history':
                history = pickle.load(open('./history', "rb"))
                loss, = plt.plot(history['loss'], label ="Loss")
                val_loss, = plt.plot(history['val_loss'], label="Validation Loss")
                plt.legend(handles=[loss, val_loss])
                plt.title('Loss vs Epoch (' + str(history['title']) + ')')
                plt.ylabel('Loss')
                plt.xlabel('Epoch')
                plt.show()
                sys.exit(0)

            else:
                self.nn.model = load_model('./model.h5')
                print("\nPretrained calorie NN loaded!\n")
        elif os.path.isfile('./model.h5') != True or sys.argv[1] == '-train':
            # create dataset for last neural network
            print("\nPreparing calorie NN dataset...\n")
            final_input_x = []
            final_input_y = []
            for i in range(len(name_list)):
                try:
                    print("\nQuery " + str(i) + "/" + str(len(name_list)) + " sent: " + name_list[i] + "\n")
                    nlp_list = self.nlp.predict(name_list[i])
                    ## cv_list = cv.predict_internal(i)
                    final_input_x.append(nlp_list)
                    final_input_y.append([calorie_list[i]])
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    continue

            final_array_x = np.array(final_input_x)
            final_array_y = np.array(final_input_y)

            print("\nTraining calorie NN...\n")

            self.nn.train(final_array_x, final_array_y, len(name_list))
            print("\nCalorie NN trained and saved!\n")


    def test(self, user_input_name):
        if len(user_input_name) < 3:
            return "Please make sure the food name is longer than 2 letters."
        try:
            global graph
            with graph.as_default():
                ## user_input_image = input("Please enter the path of your food item image.")
                nlp_predict_list = self.nlp.predict(user_input_name)
                ## cv_predict_list = cv.predict_external(user_input_image)
                predicted_calories = self.nn.predict_calorie([nlp_predict_list])
                print(str(predicted_calories[0][0]))
                return str(predicted_calories[0][0])
        except IndexError:
            return "No similar food items found. Please try again."