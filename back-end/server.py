from flask import Flask, request
from final import NLPCheck
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

nlp_check = NLPCheck()

menu_list = [
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Hainanese Chicken Rice", 2.50,
     250],
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Hainanese Chicken Rice", 2.50,
     250],
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Hainanese Chicken Rice", 2.50,
     250],
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Hainanese Chicken Rice", 2.50,
     250]]

@app.route('/menu')
def return_menu():
    menu = json.dumps(menu_list)
    return menu

@app.route('/update_menu',methods=['POST'])
def update_menu():
    name = request.json["name"]
    calorie = request.json["calories"]
    image = request.json["image"]
    price = request.json["price"]
    menu_list.append([image, name, price, calorie])
    return "OK"

@app.route('/calculate',methods=['POST'])
def calculate():
    name = request.json["name"]
    return nlp_check.test(name)