import json
import os

import logging
from logging.handlers import RotatingFileHandler
from bson import ObjectId
from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
url = os.environ.get("URL")
# client = MongoClient(f"mongodb://{username}:{password}@{url}:27017/?authSource=admin")
client = MongoClient("mongodb+srv://vishnu:ShYsODCxx7GxaFUj@targeryen.bvinedn.mongodb.net/?retryWrites=true&w=majority&appName=targeryen")
database = client['users']
collection = database['details']


@app.route('/')
def default():
    if collection.count_documents({}) > 0:
        users = collection.find({})
        return render_template('home.html', result=users, params=None)
    else:
        return render_template('home.html', message="Collection is empty")

@app.route('/add_user',  methods=['GET'])
def add_user():
    return render_template('add_user.html')

@app.route('/write', methods=['POST'])
def write():
    new_dict = {}
    entered_name = request.form.get("name")
    search_entered_name = collection.count_documents({"name": entered_name})
    print(search_entered_name)
    if search_entered_name > 0:
        return render_template('add_user.html', value="Name already exists")
    else:
        new_dict["name"] = request.form.get("name")
        new_dict["age"] = request.form.get("age")
        new_dict["gender"] = request.form.get("gender")
        new_dict["city"] = request.form.get("city")
        new_dict["state"] = request.form.get("state")
        new_dict["country"] = request.form.get("country")
        print(new_dict)
        collection.insert_one(new_dict)
        is_entered = collection.count_documents({"name": entered_name})
        if is_entered > 0:
            return render_template('add_user.html', value="Data inserted successfully")

@app.route('/get_user', methods=['POST','GET'])
def get_user():
    id = request.form.get('Id')
    user = collection.find_one({"_id":ObjectId(id)})
    user["_id"] = str(user["_id"])
    return user

@app.route('/update', methods=['POST','GET'])
def update():
    new_dict = {}
    obj_id = request.form.get("id")
    new_dict["name"] = request.form.get("name")
    new_dict["age"] = request.form.get("age")
    new_dict["gender"] = request.form.get("gender")
    new_dict["city"] = request.form.get("city")
    new_dict["state"] = request.form.get("state")
    new_dict["country"] = request.form.get("country")
    update_doc = {"$set": new_dict}
    collection.update_one({"_id":ObjectId(obj_id)}, update_doc)
    return redirect('/')

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    obj_id = request.form.get("passing-id")
    print(obj_id)
    collection.delete_one({"_id":ObjectId(obj_id)})
    return redirect('/')

@app.route('/search', methods=['POST', 'GET'])
def search():
    search_name = request.form.get("query")
    all_names = collection.find({}, {"name":1,"_id":0})
    for i in all_names:
        if search_name in i["name"]:
            result = collection.find_one({"name": i["name"]}, {"_id": 0})
            print(result)
            return render_template('search.html', result=result)

    return "No matches found"

    # search_name = request.form.get("query")
    # output_name = collection.count_documents({"name": search_name}) > 0
    # if output_name:
    #     result = collection.find_one({"name": search_name}, {"_id": 0})
    #     print(result)
    #     return render_template('search.html', result=result)
    # else:
    #     return "No matches found"

@app.route('/new_search', methods=['POST'])
def new_search():
    search_params = {}
    name = request.form.get("s-name")
    age = request.form.get("s-age")
    gender = request.form.get("s-gender")
    country = request.form.get("s-country")
    if name:
        search_params["name"] = name
    if age:
        search_params["age"] = age
    if gender:
        search_params["gender"] = gender
    if country:
        search_params["country"] = country

    search_result = collection.find(search_params)
    return render_template('home.html', result=search_result, params=search_params)

if __name__ == "__main__":
    app.run(debug=True)