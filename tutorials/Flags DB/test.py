import hashlib
import os, random
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user, UserMixin
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(
    "mongodb+srv://vishnu:C1kW0dlbf0UTsSb4@targeryen.bvinedn.mongodb.net/?retryWrites=true&w=majority&appName=targeryen")
app.config['SECRET_KEY'] = "secret"
database = client['flagQuiz']

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"  # Redirects unauthorized users to the login page
login_manager.login_message = "Please log in to access this page."  # Custom message

users_cache = {}

continents = [
    "africa",
    "asia",
    "europe",
    "northAmerica",
    "southAmerica",
    "oceania"
]
# Declaring global variables to use in any function
global selected_continent, continentName
global number_of_countries
global question_no
global random_values
global counter
global score
global user_choices
global shuffle
global updated_list
global correct_option


# Modify User class to not use user_id (if you had one)
class User:
    def __init__(self, username):
        self.username = username

    # Define is_authenticated, is_active, and get_id for Flask-Login compatibility
    @property
    def is_authenticated(self):
        # Since the user is logged in after validation, return True
        return True

    @property
    def is_active(self):
        # Active status (you can change this based on your logic)
        return True

    def get_id(self):
        # We return the username instead of user_id
        return self.username

    # No need for user_id anymore, just use username
    @staticmethod
    def get(username):
        # This is now just a simple cache lookup
        return users_cache.get(username)


# Callback to load the user from the cache
@login_manager.user_loader
def load_user(username):
    # Fetch the user from the cache by username
    user_data = users_cache.get(username)
    if user_data:
        return User(username=user_data['username'])  # Return the User object
    return None


@login_manager.unauthorized_handler
def unauthorized():
    return "Login required"


@app.route('/', methods=['GET', 'POST'])
def start():
    return render_template('login.html')


def initialize():
    """ Since using global variables in python, it has be called again or mentioned again.Directly modifying the
    variable throws an error """

    global selected_continent, continentName
    global number_of_countries
    global question_no
    global counter
    global score
    global user_choices
    question_no = 1
    counter = 0
    score = 0
    user_choices = []

    continent = request.form.get('continent')
    continentName = continent
    if continent in globals():
        selected_continent = globals()[continent]
        random.shuffle(selected_continent)
    number_of_countries = len(selected_continent)

    print("from initialize", selected_continent)
    print(continentName)


def reset():
    global selected_continent, continentName
    global number_of_countries
    global question_no
    global random_values
    global counter
    global score
    selected_continent, continentName = None, None
    number_of_countries, question_no, counter, score = 0, 0, 0, 0


def select_choices(input):
    global shuffle
    choices = random.sample(input, 2)
    shuffle = [selected_continent[counter], choices[0], choices[1]]
    random.shuffle(shuffle)


@app.route('/start_game', methods=['GET', 'POST'])
@login_required
def start_game():
    initialize()
    global updated_list, correct_option
    correct_option = selected_continent[counter]
    updated_list = selected_continent[1:]
    select_choices(updated_list)
    return render_template('play.html', flag_image=selected_continent[counter],
                           total=number_of_countries,
                           remaining=question_no, option1=shuffle[0],
                           option2=shuffle[1],
                           option3=shuffle[2], condition=False, score=score, continent=continentName.upper(),
                           isItCorrect=None)


@app.route('/play', methods=['POST', 'GET'])
def play():
    clicked = request.form.get("answer")
    global score
    user_choices.append(clicked)
    position = shuffle.index(clicked) + 1
    if position == 1:
        opt1 = "green"
        opt2 = "red"
        opt3 = "red"
    elif position == 2:
        opt1 = "red"
        opt2 = "green"
        opt3 = "red"
    else:
        opt1 = "red"
        opt2 = "red"
        opt3 = "green"

    if clicked == selected_continent[counter]:
        score += 1
        return render_template('play.html', flag_image=selected_continent[counter],
                               total=number_of_countries,
                               remaining=question_no, option1=shuffle[0],
                               option2=shuffle[1],
                               option3=shuffle[2], condition=True, score=score, continent=continentName.upper(),
                               isItCorrect=True, opt1=opt1, opt2=opt2, opt3=opt3)
    else:
        return render_template('play.html', flag_image=selected_continent[counter],
                               total=number_of_countries,
                               remaining=question_no, option1=shuffle[0],
                               option2=shuffle[1],
                               option3=shuffle[2], condition=True, score=score, continent=continentName.upper(),
                               isItCorrect=False, opt1=opt1, opt2=opt2, opt3=opt3)


@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    collection = database['users']
    username = request.form.get('username')
    password = request.form.get('password')
    # print("Form data",username, password)
    user = collection.find_one({"username": username})
    # print("DB result", user)

    if user is not None:
        computed_password = hashlib.sha256(password.encode() + bytes.fromhex(user['salt'])).hexdigest()
        if (user['username'] == username) and (user['password'] == computed_password):
            user_obj = User(username=username)
            users_cache[username] = {"username": username}
            login_user(user_obj)
            print(current_user)
            return redirect(url_for("home"))
        else:
            flash("Invalid credentials")
    else:
        return "User not found"
    return "Invalid login"


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    username = request.form.get("username")
    password = request.form.get("password")
    salt = os.urandom(16)
    hashed_password = hashlib.sha256(password.encode() + salt).hexdigest()
    new_user = {"username": username, "password": hashed_password, "salt": salt.hex()}
    collection = database['users']
    collection.insert_one(new_user)
    return render_template('signUp.html')


@app.route('/login_redirect', methods=['POST', 'GET'])
def login_redirect():
    return render_template('login.html')


@app.route('/signup_redirect', methods=['POST', 'GET'])
def signup_redirect():
    return render_template('signUp.html')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    # Log out the user
    logout_user()
    flash("Logged out successfully")
    return render_template('login.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, use_reloader=True, debug=True)
