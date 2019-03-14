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

class NLPModel:
    def __init__(self, data):
        self.csv = "./info.csv"
        self.data = data
        self.data_text = self.data[['Name']]
        self.data_calorie = self.data[['Calories']]
        self.data_size = len(self.data)
        self.full_list = []
        self.model = None
        self.num_best = 5
        self.instance = None

    def lemmatize_stemming(self, text):
        stemmer = PorterStemmer()
        return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

    # preprocess: tokenisation, stopwords removed, lemmatised and stemmed
    def preprocess(self, text):
        result = []
        for token in gensim.utils.simple_preprocess(text):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 2:
                result.append(self.lemmatize_stemming(token))
        return result

    def make_word_list(self):
        nltk.download('wordnet')

        # make word list from both names and categories
        for i in range(self.data_size):
            new_list = []
            final_list = []
            for j in self.data[['Name']].values[i][0].split(' '):
                k = self.preprocess(j)
                if k != []:
                    new_list.append(k)
            for j in self.data[['Category']].values[i][0].split(' '):
                k = self.preprocess(j)
                if k != []:
                    new_list.append(k)
            if new_list != []:
                for i in new_list:
                    final_list.append(i[0])
            self.full_list.append(final_list)

    def train(self):
        np.random.seed(2018)

        self.make_word_list()

        self.model = gensim.models.Word2Vec(self.full_list, min_count=1, size=300, workers=4)

        # normalise vectors
        self.model.init_sims(replace=True)
        self.instance = WmdSimilarity(self.full_list, self.model, num_best=self.num_best)

    def predict(self, sent):
        query = self.preprocess(sent)
        sims = self.instance[query]
        calorie_list = []

        print("\nNLP predictions:\n")

        for i in range(self.num_best):
            print(self.data['Name'][sims[i][0]])
            calorie_list.append(self.data['Calories'][sims[i][0]])
        print("\n")

        return calorie_list