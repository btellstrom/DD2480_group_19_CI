from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
mongo_object = MongoClient(HOST, PORT)
db = mongo_object['mydb']
collection = db['mycollection']

@app.route("/", methods = ['GET','POST'])
def hello():

    content = request.json # Load JSON data sent with POST request
    print (content)
    return "CI server!"

def pymongo_data_display():
    my_data = collection.find_one()
    # Here we need to add some defensive programming in case my_data is None
    return my_data

if __name__ == '__main__':
    app.run(debug = True, port=8080)