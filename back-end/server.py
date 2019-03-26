from flask import Flask, request
from final import NLPCheck
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

nlp_check = NLPCheck()

menu_list = [
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Steamed Chicken with Rice", 3.00,
     618],
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Steamed Chicken Wing with Rice", 3.00,
     620],
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Steamed Drumstick Rice", 3.50,
     687],
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Roasted Chicken with Rice", 3.00,
     688],
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Roasted Chicken Wing with Rice", 3.00,
     690],
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Roasted Drumstick Rice", 3.50,
     757],
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Fried Lemon Chicken with Rice", 4.00,
     1277],
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Thai Chicken Cutlet with Rice", 4.00,
     1142],
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Steamed Chicken Noodles",
     3.00,
     593],
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-lg-691.jpg", "Roasted Chicken Noodles",
     3.00,
     663]]

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