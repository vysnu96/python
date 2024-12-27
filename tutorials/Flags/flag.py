import random

from flask import Flask, render_template, request, redirect, url_for
from random import randint
from countries import africa, asia, europe, oceania, northAmerica, southAmerica, africa_dict, asia_dict, europe_dict, oceania_dict, southAmerica_dict, northAmerica_dict, asia_code, africa_code, europe_code, oceania_code, northAmerica_code, southAmerica_code

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/start')
# def start(continent_name):
#     x = random.sample(continent_name, len(continent_name))
#     return x

@app.route('/continent/asia', methods=['POST', 'GET'])
def asia_route():
    asia_temp = random.sample(asia_code, len(asia_code))
    numberOfCountries = len(asia_temp)
    print(numberOfCountries)
    for x in asia_temp:

        return render_template('asia.html', asia_flag=asia_temp[1].lower())


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
