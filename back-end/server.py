from flask import Flask, request, session
from final import NLPCheck
from flask_cors import CORS
import json
import pandas as pd
import csv

app = Flask(__name__)
CORS(app)

nlp_check = NLPCheck()

@app.route('/menu')
def return_menu():
    menu_list = []
    with open('./demo.csv','r') as file:
        data = pd.read_csv(file, error_bad_lines=False)
    data_size = len(data)
    for i in range(data_size):
        menu_list.append([data[['Image']].values[i][0],str(data[['Name']].values[i][0]),data[['Price']].values[i][0],str(data[['Calories']].values[i][0])])
    print(menu_list)
    menu = json.dumps(menu_list)
    return menu

@app.route('/update_menu',methods=['POST'])
def update_menu():
    name = request.json["name"]
    calorie = request.json["calories"]
    image = request.json["image"]
    price = request.json["price"]
    with open('./demo.csv', 'a') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(
            [name, calorie, image, price])
    return "OK"

@app.route('/calculate',methods=['POST'])
def calculate():
    name = request.json["name"]
    try:
        return int(nlp_check.test(name))
    except:
        return nlp_check.test(name)