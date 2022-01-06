

from flask import Flask
from mock_data import catalog
import json


app = Flask(__name__)

me = {
        "name": "Mike",
        "last": "Mckitrick",
        "age": "37",
        "hobbies": [],
        "address": {
            "street": "Evergreen",
            "number": 42,
            "city":"Springfield"
        }
    }

@app.route("/")
def home():
    return "Hello from Python"

@app.route("/test")
def any_name():
    return "I'm a test function"

@app.route("/about")
def about():
    return me["name"]+" "+ me["last"]


#*********************************************
#***************API ENDPOINTS****************
#*********************************************



@app.route("/api/catalog")
def get_catalog():
    return json.dumps(catalog)

@app.route("/api/cheapest")
def get_cheapest():
    cheap = catalog[0]
    for product in catalog:

        if product["price"] < cheap["price"]:
            cheap = product
    #find the cheapest products in catalog list
    return json.dumps(cheap)

@app.route("/api/product/<id>")
def get_product(id):
    #find the product whose _id is equal to id
    for product in catalog:
        if product["_id"] == id:
            return json.dumps(product)

    return "NOT FOUND"


    # return it as json
    


#start the server
app.run(debug=True)