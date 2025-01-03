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
# Declaring global variables to use in any function
global selected_continent, continentName
global number_of_countries
global question_no
global random_values
global counter
global score


@app.route('/')
def home():
    return render_template('home.html')


# This function will be called whenever a new game is started
def initialize():
    """ Since using global variables in python, it has be called again or mentioned again.Directly modifying the
    variable throws an error """

    global selected_continent, continentName
    global number_of_countries
    global question_no
    global counter
    global score
    selected_continent = None
    number_of_countries = 0
    question_no = 1
    counter = 0
    score = 0

    continent = request.form.get('continent')
    continentName = continent
    if continent in globals():
        selected_continent = globals()[continent]
        random.shuffle(selected_continent)
    number_of_countries = len(selected_continent)

    print("from initialize", selected_continent)
    print(continentName)


@app.route('/start', methods=['POST', 'GET'])
def start():
    initialize()
    global random_values, score
    random_values = random.sample(selected_continent, 2)
    return render_template('play.html', flag_image=selected_continent[counter],
                           total=number_of_countries,
                           remaining=question_no, option1=selected_continent[counter],
                           option2=random_values[0],
                           option3=random_values[1], condition=False, score=score, continent=continentName.upper())


@app.route('/play', methods=['POST', 'GET'])
def play():
    clicked = request.form.get("answer")
    global score
    if clicked.strip().lower() == selected_continent[counter].strip().lower():
        score += 1
        print("Score:", score)
        print("If from play called")
        return render_template('play.html', flag_image=selected_continent[counter],
                               total=number_of_countries,
                               remaining=question_no, option1=selected_continent[counter],
                               option2=random_values[0],
                               option3=random_values[1], condition=True, score=score, continent=continentName.upper())
    else:
        print("Else from play called")
        return render_template('play.html', flag_image=selected_continent[counter],
                               total=number_of_countries,
                               remaining=question_no, option1=selected_continent[counter],
                               option2=random_values[0],
                               option3=random_values[1], condition=True, score=score, continent=continentName.upper())


@app.route('/nxt', methods=['POST', 'GET'])
def nxt():
    global question_no, selected_continent, counter, score
    question_no += 1
    counter += 1
    print("counter", counter)
    global random_values
    random_values = random.sample(selected_continent, 2)
    return render_template('play.html', flag_image=selected_continent[counter],
                           total=number_of_countries,
                           remaining=question_no, option1=selected_continent[counter],
                           option2=random_values[0],
                           option3=random_values[1], condition=False, score=score, continent=continentName.upper())


@app.route('/finish', methods=['POST', 'GET'])
def finish():
    return render_template('score_card.html', continent=continentName, score=score, total=number_of_countries, continent_image=continentName)


if __name__ == "__main__":
    app.run(debug=True)
