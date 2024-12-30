import random

from flask import Flask, render_template, request, redirect, url_for
from random import randint
from countries import africa, asia, europe, oceania, northAmerica, southAmerica, africa_dict, asia_dict, europe_dict, oceania_dict, southAmerica_dict, northAmerica_dict, asia_code, africa_code, europe_code, oceania_code, northAmerica_code, southAmerica_code

app = Flask(__name__)
continents = [
    "africa",
    "asia",
    "europe",
    "northAmerica",
    "southAmerica",
    "oceania"
]


@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/initialize', methods=['POST', 'GET'])
def initialize():
    continent = request.form.get('continent')
    print(continent)
    if continent in globals():
        temp = globals()[continent]
        random.shuffle(temp)
    print(temp)
    number_of_countries = len(temp)
    template_name = f"{continent}.html"
    return temp, number_of_countries, template_name
#    return render_template(template_name, asia_flag=temp[1].lower(), total=number_of_countries)

def process_answer():
    option1 = request.form.get("Option1")
    option2 = request.form.get("Option2")
    option3 = request.form.get("Option3")
    print(option1, option2, option3)
    return render_template('asia.html')

@app.route('/asia', methods=['POST', 'GET'])
def asia_route():
    temp, number_of_countries, template_name = initialize()
    return render_template(template_name, asia_flag=temp[1].lower(), total=number_of_countries)


@app.route('/continent/europe', methods=['POST', 'GET'])
def europe():
    return render_template('europe.html')


@app.route('/continent/africa', methods=['POST', 'GET'])
def africa():
    return render_template('africa.html')


@app.route('/continent/oceania', methods=['POST', 'GET'])
def oceania():
    return render_template('oceania.html')


@app.route('/continent/southAmerica', methods=['POST', 'GET'])
def southAmerica():
    return render_template('southAmerica.html')


@app.route('/continent/northAmerica', methods=['POST', 'GET'])
def northAmerica():
    return render_template('northAmerica.html')


if __name__ == "__main__":
    app.run(debug=True)
