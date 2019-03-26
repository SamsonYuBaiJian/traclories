from flask import Flask, request
from final import NLPCheck
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

nlp_check = NLPCheck()

menu_list = [
    ["https://steamykitchen.com/wp-content/uploads/2009/08/hainanese-chicken-86.jpg", "Steamed Chicken with Rice", 3.00,
     618],
    ["https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/NC4GztZqgikdztf21/man-creates-dishes-portion-from-chicken-wings-with-rice_sk8vsdlrg_thumbnail-full01.png", "Steamed Chicken Wing with Rice", 3.00,
     620],
    ["https://www.wokandskillet.com/wp-content/uploads/2015/05/chicken-rice.jpg", "Steamed Drumstick Rice", 3.50,
     687],
    ["https://i.ytimg.com/vi/o8PW0xN6uPs/hqdefault.jpg", "Roasted Chicken with Rice", 3.00,
     688],
    ["https://i.pinimg.com/originals/4d/4c/b5/4d4cb59ad4a83a322daeb7d63cbcbf89.jpg", "Roasted Chicken Wing with Rice", 3.00,
     690],
    ["http://www.swankyrecipes.com/wp-content/uploads/2015/03/Honey-Mustard-Chicken-easyrecipe.jpg", "Roasted Drumstick Rice", 3.50,
     757],
    ["https://s3-media1.fl.yelpcdn.com/bphoto/4UtS56S8Hb_otbjlxhi2KA/o.jpg", "Fried Lemon Chicken with Rice", 4.00,
     1277],
    ["http://mmm-yoso.typepad.com/mmmyoso/images/2008/01/18/01062008_013_2.jpg", "Thai Chicken Cutlet with Rice", 4.00,
     1142],
    ["https://i.pinimg.com/originals/76/fd/09/76fd093945198fa83de25de535b43f2d.jpg", "Steamed Chicken Noodles",
     3.00,
     593]]

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
    menu_list.append([image, name, float(price), int(calorie)])
    return "OK"

@app.route('/calculate',methods=['POST'])
def calculate():
    name = request.json["name"]
    return int(nlp_check.test(name))