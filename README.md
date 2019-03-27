# Traclories
- Automating calorie tracking by integrating DBS PayLah! and Healthy 365.
- Calorie estimation with Keras, Gensim, NLTK, BeautifulSoup, pandas, React, Flask, Heroku and VGG-16.
- Deployed to a live server on Heroku for demonstration purposes.
- Created React front-end user interface for vendors to sign up for accounts to upload their food items.
- Created Flask back-end to link the front-end to the machine learning models.
- Used Keras dense layers and ReLU activations to train neural network to apply the appropriate weights to the five vectors for each datapoint.
- Applied natural language processing with Gensim and NLTK to find the five nearest word vectors.
- Scraped nutritional data from Allrecipes with BeautifulSoup.

## Steps
1. Scraped food information from https://www.allrecipes.com/recipes/. (./back-end/scraper.py)
    - Information is saved. (./back-end/info.csv)
2. Applied natural language processing with Gensim and NLTK to find the five nearest word vectors. (./back-end/nlp_test.py)
3. Used Keras dense layers and ReLU activations to train neural network to apply the appropriate weights to the five vectors for each datapoint. (./back-end/weight_net.py)
    - Model and model history are saved. (./back-end/model.h5 and ./back-end/history)
4. Allowed food vendors to predict calories in new food items. (./back-end/final.py)
5. Created React front-end user interface for vendors to sign up for accounts to upload their food items. (./front-end)
6. Created Flask back-end to link the front-end to the machine learning models. (./back-end/server.py)
7. Deployed to a live server on Heroku for demonstration purposes.

Note: The computer vision test with VGG-16 failed because the approximate nearest neighbour algorithm used to build the tree structure for existing datapoints could not be updated incrementally to estimate the calories in new food items. (./back-end/cv_unused)

## Screenshots
### NLP Model Predictions
![Screenshot](https://raw.github.com/SamsonYuBaiJian/traclories/master/screenshots/nlp.png)
### Loss Graph from Keras Neural Network
![Screenshot](https://raw.github.com/SamsonYuBaiJian/traclories/master/screenshots/loss.png)
### Login
![Screenshot](https://raw.github.com/SamsonYuBaiJian/traclories/master/screenshots/login.png)
### Menu
![Screenshot](https://raw.github.com/SamsonYuBaiJian/traclories/master/screenshots/menu.png)
### Add Items
![Screenshot](https://raw.github.com/SamsonYuBaiJian/traclories/master/screenshots/add.png)
### Heroku Logs
![Screenshot](https://raw.github.com/SamsonYuBaiJian/traclories/master/screenshots/heroku.png)