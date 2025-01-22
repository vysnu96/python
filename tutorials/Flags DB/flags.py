import random, os, hashlib
from functools import wraps

from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from user.models import User

from countries import asia, africa, europe, northAmerica, southAmerica, oceania

app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://vishnu:C1kW0dlbf0UTsSb4@targeryen.bvinedn.mongodb.net/?retryWrites=true&w=majority&appName=targeryen")
app.config['SECRET_KEY'] = "secret"
database = client['flagQuiz']


# collection = database['continents']
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/login')

    return wrap


@app.route('/')
def start():
    return render_template('signUp.html')


@app.route('/user/signup', methods=['POST'])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")
    salt = os.urandom(16)
    hashed_password = hashlib.sha256(password.encode() + salt).hexdigest()
    new_user = {"username": username, "password": hashed_password, "salt": salt.hex()}
    collection = database['users']
    collection.insert_one(new_user)
    return render_template('signUp.html')


@app.route('/user/login', methods=['POST', 'GET'])
def login():
    loggedInUser = User().login()
    return render_template('home.html', user=loggedInUser)


# For redirection from the signup page
@app.route('/login', methods=['POST', 'GET'])
def login_redirect():
    return render_template('login.html')


# For redirection from the login page
@app.route('/signup', methods=['POST', 'GET'])
def signup_redirect():
    return render_template('signUp.html')


@app.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html')


#
# @app.route('/signup', methods=['POST', 'GET'])
# def signup():
#     username = request.form.get("username")
#     password = request.form.get("password")
#     salt = os.urandom(16)
#     hashed_password = hashlib.sha256(password.encode() + salt).hexdigest()
#     new_user = {"username": username, "password": hashed_password, "salt": salt.hex()}
#     collection = database['users']
#     collection.insert_one(new_user)
#     return render_template('home.html')

#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     username = request.form.get("username")
#     password = request.form.get("password")
#     collection = database['users']
#     find = collection.find_one({"username": username}, {"_id": 0})
#     print("Entered user, " + username)
#     print("found user, " + find['username'])
#     # if username == find['username']:
#     #     return "User Found"
#     return render_template('home.html')
#
#
# @app.route('/start', methods=['POST', 'GET'])
# def play():
#     continent = request.form.get('continent')
#     print(continent)
#     return render_template('play.html')
#

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, use_reloader=True, debug=True)
