import pandas as pd
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np
from gensim.models import Word2Vec
from gensim.similarities import WmdSimilarity

np.random.seed(2018)

import nltk
nltk.download('wordnet')

csv = "./dataset/info.csv"

data = pd.read_csv(csv, error_bad_lines=False)
data_text = data[['Name']]
data_size = len(data)


def lemmatize_stemming(text):
    stemmer = PorterStemmer()
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

# preprocess: tokenisation, stopwords removed, lemmatised and stemmed
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result

new_list = []
final_list = []
full_list = []

# make word list from both names and categories
for i in range(data_size):
    new_list = []
    final_list = []
    for j in data[['Name']].values[i][0].split(' '):
        k = preprocess(j)
        if k != []:
            new_list.append(k)
    for j in data[['Category']].values[i][0].split(' '):
        k = preprocess(j)
        if k != []:
            new_list.append(k)
    if new_list != []:
        for i in new_list:
            final_list.append(i[0])
    full_list.append(final_list)


sent = 'Delicious Apple Pie'
query = preprocess(sent)

print("\n")
print("Query: " + sent)
print("\n")

model = gensim.models.Word2Vec(full_list, min_count=1,size=300,workers=4)

# normalise vectors
model.init_sims(replace=True)
num_best = 10
instance = WmdSimilarity(full_list, model, num_best=num_best)

sims = instance[query]

for i in range(num_best):
    print(data['Name'][sims[i][0]])
print("\n")