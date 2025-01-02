import random

from flask import Flask, render_template, request, redirect, url_for
from random import randint
from countries import africa, asia, europe, oceania, northAmerica, southAmerica, africa_dict, asia_dict, europe_dict, \
    oceania_dict, southAmerica_dict, northAmerica_dict, asia_code, africa_code, europe_code, oceania_code, \
    northAmerica_code, southAmerica_code

app = Flask(__name__)
continents = [
    "africa",
    "asia",
    "europe",
    "northAmerica",
    "southAmerica",
    "oceania"
]

global selected_continent
global number_of_countries
global question_no
global random_values
global counter
@app.route('/')
def home():
    return render_template('home.html')


def initialize():
    global selected_continent
    global number_of_countries
    global question_no
    global counter
    selected_continent = None
    number_of_countries = 0
    question_no = 1
    counter = 0

    continent = request.form.get('continent')
    if continent in globals():
        selected_continent = globals()[continent]
        random.shuffle(selected_continent)
    number_of_countries = len(selected_continent)

    print("from initialize", selected_continent)

@app.route('/start', methods=['POST', 'GET'])
def start():
    initialize()
    global random_values
    random_values = random.sample(selected_continent, 2)
    return render_template('play.html', flag_image=selected_continent[counter],
                           total=number_of_countries,
                           remaining=question_no, option1=selected_continent[counter],
                           option2=random_values[0],
                           option3=random_values[1], condition=False)


@app.route('/play', methods=['POST', 'GET'])
def play():
    clicked = request.form.get("answer")
    if clicked == selected_continent[0]:
        return render_template('play.html', flag_image=selected_continent[counter],
                               total=number_of_countries,
                               remaining=question_no, option1=selected_continent[counter],
                               option2=random_values[0],
                               option3=random_values[1], condition=True)
    else:
        return render_template('play.html', flag_image=selected_continent[counter],
                               total=number_of_countries,
                               remaining=question_no, option1=selected_continent[counter],
                               option2=random_values[0],
                               option3=random_values[1], condition=True)


@app.route('/nxt', methods=['POST', 'GET'])
def nxt():
    global question_no, selected_continent, counter
    question_no += 1
    counter += 1
    print("from nxt", selected_continent)
    global random_values
    random_values = random.sample(selected_continent, 2)
    return render_template('play.html', flag_image=selected_continent[counter],
                           total=number_of_countries,
                           remaining=question_no, option1=selected_continent[counter],
                           option2=random_values[0],
                           option3=random_values[1], condition=False)


if __name__ == "__main__":
    app.run(debug=True)
