# Traclories
Calorie estimation with Keras, Gensim, NLTK, BeautifulSoup and pandas (VGG-16 failed).

## Steps:
1. Scrape food information from https://www.allrecipes.com/recipes/. (scraper.py)
2. Apply natural language processing with Gensim and NLTK to find the five nearest word vectors. (nlp_test.py)
3. Use Keras dense layers and ReLU activations to train neural network to apply the appropriate weights to the five vectors for each datapoint. (weight_net.py)
4. Allow users to predict calories in new food items. (final.py)
- Note: The computer vision test with VGG-16 failed because the approximate nearest neighbour algorithm used to build the tree structure for existing datapoints could not be updated incrementally to estimate the calories in new food items. (cv_unused)
