from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import time
import re
import os
import csv

url = "https://www.allrecipes.com/recipes/"
page_url = "?page="
pages = 15
csv_file = './info.csv'
## csv_directory = "./dataset"
## image_directory = "./dataset/images"

# check https://www.allrecipes.com/robots.txt
crawl_delay = 3

# create csv file
if os.path.isfile(csv_file) == False:
    with open(csv_file, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Name', 'Calories', 'Serving Size', 'Fat(g)', 'Carbohydrate(g)', 'Protein(g)', 'Cholesterol(mg)', 'Sodium(mg)', 'Category', 'URL'])

names = []
urls = {}
item = 0

html = urlopen(url)

soup = BeautifulSoup(html, features="lxml")
for tag in soup.find_all('a', {'href': re.compile('allrecipes.com/recipes')}):
    text = tag.get_text().lstrip()
    text = text.rstrip()
    if text not in urls.keys():
        # urls = {category: url}
        urls[text] = tag.get('href')


for category, link in urls.items():

    for page in range(pages):
        page += 1

        if page == 1:
            target_url = link
        else:
            target_url = link + page_url + str(page)

        print("PAGE: " + str(page))
        print("URL: " + target_url)
        print("\n")

        try:
            target_html = urlopen(target_url)
            soup = BeautifulSoup(target_html, features="lxml")
        except:
            continue

        try:

            for tag in soup.find_all('article', {'class':['fixed-recipe-card', 'ng-isolate-scope']}):
                try:
                    ## recipe_image = tag.find_all('img', {'class': 'fixed-recipe-card__img'})[0].get('data-original-src')

                    recipe_url = tag.find_all('a', {'href': re.compile('allrecipes.com/recipe/')}, {'data-click-id': re.compile('card slot')})[0].get('href')
                    recipe_html = urlopen(recipe_url)

                    recipe_soup = BeautifulSoup(recipe_html, features="lxml")

                    name = recipe_soup.find_all('h1', {'class': 'recipe-summary__h1'})[0].get_text()
                    name = name.replace('/', ' ')

                    if name not in names:
                        item += 1
                        names.append(name)
                        calories = recipe_soup.find_all('span', {'class': 'calorie-count'})[0].find_all('span')[0].get_text()
                        calories = int(calories)
                        serving_size = recipe_soup.find_all('meta', {'id': 'metaRecipeServings'})[0].get('content')

                        nutrition = recipe_soup.find_all('div', {'class': "nutrition-summary-facts"})[0]
                        fat = nutrition.find_all('span', {'itemprop': 'fatContent'})[0].get_text()
                        carbohydrate = nutrition.find_all('span', {'itemprop': 'carbohydrateContent'})[0].get_text()
                        protein = nutrition.find_all('span', {'itemprop': 'proteinContent'})[0].get_text()
                        cholesterol = nutrition.find_all('span', {'itemprop': 'cholesterolContent'})[0].get_text()
                        sodium = nutrition.find_all('span', {'itemprop': 'sodiumContent'})[0].get_text()
                        nutrition = [fat, carbohydrate, protein, cholesterol, sodium]

                        print("Item: " + str(item))
                        print("Name: " + name)
                        print("Calories: " + str(calories))
                        ## print("Image URL: " + recipe_image)
                        print("Serving Size: " + serving_size)
                        print("Fat: " + fat + "g")
                        print("Carbohydrate: " + carbohydrate + "g")
                        print("Protein: " + protein + "g")
                        print("Cholesterol: " + cholesterol + "mg")
                        print("Sodium: " + sodium + "mg")
                        print("Category: " + category)
                        print("URL: " + recipe_url + "\n")

                        # save data
                        with open(csv_file, 'a') as csvfile:
                            filewriter = csv.writer(csvfile)
                            filewriter.writerow(
                                [name, str(calories), serving_size, fat, carbohydrate, protein, cholesterol, sodium, category, recipe_url])
                        ## urlretrieve(recipe_image, image_directory + "/" + name)

                        print("\n")
                except:
                    continue

                time.sleep(crawl_delay)

        except:
            continue