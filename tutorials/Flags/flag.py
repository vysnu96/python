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

@app.route('/initialize', methods=['POST', 'GET'])
def initialize():
    country = request.form.get('continent')
    country_temp = random.sample(f"{country}_code", len(f"{country}_code"))
    print(country_temp)
    return render_template(f"{country}.html", asia_flag=country_temp[1].lower())

def process_answer():
    option1 = request.form.get("Option1")
    option2 = request.form.get("Option2")
    option3 = request.form.get("Option3")
    print(option1, option2, option3)
    return render_template('asia.html')

@app.route('/continent/asia', methods=['POST', 'GET'])
def asia_route():
    asia_temp = random.sample(asia_code, len(asia_code))
    numberOfCountries = len(asia_temp)
    choosen_country = asia_temp[1]
    return render_template('asia.html', asia_flag=choosen_country.lower(), total=numberOfCountries, Option1=asia_dict["choosen_country"], Option2=asia_dict["asia_temp[2]"], Option3=asia_dict["asia_temp[3]"])


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
