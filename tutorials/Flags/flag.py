import random
from flask import Flask, render_template, request, redirect, url_for
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
global user_choices
global shuffle


@app.route('/')
def home():
    reset()
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

def random_func(remaining_values):
    global shuffle
    random_values = random.sample(remaining_values, 2)
    shuffle = [selected_continent[counter], random_values[0], random_values[1]]
    random.shuffle(shuffle)

@app.route('/start', methods=['POST', 'GET'])
def start():
    initialize()
    global random_values, score
    remaining_values = [country for country in selected_continent if country != selected_continent[counter]]
    random_func(remaining_values)
    return render_template('play.html', flag_image=selected_continent[counter],
                           total=number_of_countries,
                           remaining=question_no, option1=shuffle[0],
                           option2=shuffle[1],
                           option3=shuffle[2], condition=False, score=score, continent=continentName.upper(), isItCorrect=None)


@app.route('/play', methods=['POST', 'GET'])
def play():
    opt1, opt2, opt3 = None, None, None
    clicked = request.form.get("answer")
    global score
    user_choices.append(clicked)
    print(clicked)
    print(shuffle)
    position = shuffle.index(selected_continent[counter]) + 1
    print(position)
    if clicked != selected_continent[counter]:
        pos = shuffle.index(clicked) + 1
        if pos == 1:
            opt1 = "red"
        elif pos == 2:
            opt2 = "red"
        else:
            opt3 = "red"
    else:
        pass

    if position == 1:
        opt1 = "green"
    elif position == 2:
        opt2 = "green"
    else:
        opt3 = "green"
    print(opt1, opt2, opt3)
    if clicked.strip().lower() == selected_continent[counter].strip().lower():
        score += 1
        # print("Score:", score)
        # print("If from play called")
        return render_template('play.html', flag_image=selected_continent[counter],
                               total=number_of_countries,
                               remaining=question_no, option1=shuffle[0],
                               option2=shuffle[1],
                               option3=shuffle[2], condition=True, score=score, continent=continentName.upper(), isItCorrect=True, opt1=opt1, opt2=opt2, opt3=opt3)
    else:
        # print("Else from play called")
        return render_template('play.html', flag_image=selected_continent[counter],
                               total=number_of_countries,
                               remaining=question_no, option1=shuffle[0],
                               option2=shuffle[1],
                               option3=shuffle[2], condition=True, score=score, continent=continentName.upper(), isItCorrect=False, opt1=opt1, opt2=opt2, opt3=opt3)


@app.route('/nxt', methods=['POST', 'GET'])
def nxt():
    global question_no, selected_continent, counter, score
    question_no += 1
    counter += 1
    # print("counter", counter)
    global random_values
    remaining_values = [country for country in selected_continent if country != selected_continent[counter]]
    random_func(remaining_values)
    return render_template('play.html', flag_image=selected_continent[counter],
                           total=number_of_countries,
                           remaining=question_no, option1=shuffle[0],
                           option2=shuffle[1],
                           option3=shuffle[2], condition=False, score=score, continent=continentName.upper(), isItCorrect=None)


@app.route('/finish', methods=['POST', 'GET'])
def finish():
    print("your choice",user_choices)
    print("Answer",selected_continent)
    return render_template('result.html', continent=continentName.upper(), score=score, total=number_of_countries,
                           continent_image=continentName, user_choices=user_choices, selected_continent=selected_continent)


if __name__ == "__main__":
    app.run(debug=True)
