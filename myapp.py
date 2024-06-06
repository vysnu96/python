from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://vishnu:ShYsODCxx7GxaFUj@targeryen.bvinedn.mongodb.net/?retryWrites=true&w=majority&appName=targeryen")
database = client['users']
collection = database['details']


@app.route('/')
def default():
    users = collection.find({})
    # results = []
    # for x in users:
    #     str(x["_id"])
    #     results.append(i)
    # # users = jsonify(users)
    # print(results)
    print(users)
    return render_template('new-home.html', result=users)

@app.route('/add_user',  methods=['GET'])
def add_user():
    return render_template('add-user.html')

@app.route('/write', methods=['POST'])
def write():
    new_dict = {}
    entered_name = request.form.get("name")
    search_entered_name = collection.count_documents({"name": entered_name})
    print(search_entered_name)
    if search_entered_name > 0:
        return f"{entered_name} already exists in database"
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
            return render_template('add-user.html', value="Data inserted successfully")


@app.route('/search', methods=['POST', 'GET'])
def search():
    search_name = request.form.get("query")
    output_name = collection.count_documents({"name": search_name}) > 0
    if output_name:
        result = collection.find_one({"name": search_name}, {"_id": 0})
        print(result)
        return render_template('search.html', result=result)
        # return result
    else:
        return "No matches found"


if __name__ == "__main__":
    app.run(debug=True)