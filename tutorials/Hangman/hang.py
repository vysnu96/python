from flask import Flask, render_template, request, redirect, url_for
from random import randint


app = Flask(__name__)

tamil_movies = [
    {"Name": "ROJA", "Year": 1992, "Hero": "Arvind Swamy"},
    {"Name": "GENTLEMAN", "Year": 1993, "Hero": "Arjun"},
    {"Name": "BAASHA", "Year": 1995, "Hero": "Rajinikanth"},
    {"Name": "INDIAN", "Year": 1996, "Hero": "Kamal Haasan"},
    {"Name": "MINSARA KANAVU", "Year": 1997, "Hero": "Arvind Swamy"},
    {"Name": "JEANS", "Year": 1998, "Hero": "Prashanth"},
    {"Name": "PADAYAPPA", "Year": 1999, "Hero": "Rajinikanth"},
    {"Name": "ALAI PAYUTHEY", "Year": 2000, "Hero": "Madhavan"},
    {"Name": "DHEENA", "Year": 2001, "Hero": "Ajith Kumar"},
    {"Name": "KANNATHIL MUTHAMITTAL", "Year": 2002, "Hero": "Madhavan"},
    {"Name": "SAAMY", "Year": 2003, "Hero": "Vikram"},
    {"Name": "GILLI", "Year": 2004, "Hero": "Vijay"},
    {"Name": "ANNIYAN", "Year": 2005, "Hero": "Vikram"},
    {"Name": "VARALARU", "Year": 2006, "Hero": "Ajith Kumar"},
    {"Name": "SIVAJI", "Year": 2007, "Hero": "Rajinikanth"},
    {"Name": "VARSHAAM", "Year": 2008, "Hero": "Prabhas"},
    {"Name": "VETTAIYAADU VILAIYAADU", "Year": 2006, "Hero": "Kamal Haasan"},
    {"Name": "AYAN", "Year": 2009, "Hero": "Suriya"},
    {"Name": "ENNAI ARINDHAAL", "Year": 2015, "Hero": "Ajith Kumar"},
    {"Name": "GURU", "Year": 2017, "Hero": "Venkatesh"},
    {"Name": "KAALA", "Year": 2018, "Hero": "Rajinikanth"},
    {"Name": "KAAPPAAN", "Year": 2019, "Hero": "Suriya"},
    {"Name": "MAARI", "Year": 2015, "Hero": "Dhanush"},
    {"Name": "BIRYANI", "Year": 2013, "Hero": "Karthi"},
    {"Name": "RAAVANAN", "Year": 2010, "Hero": "Vikram"},
    {"Name": "SINGAM", "Year": 2010, "Hero": "Suriya"},
    {"Name": "RAJAPATTAI", "Year": 2011, "Hero": "Vikram"},
    {"Name": "7AUM ARIVU", "Year": 2011, "Hero": "Suriya"},
    {"Name": "THUPPAKKI", "Year": 2012, "Hero": "Vijay"},
    {"Name": "VISHWAROOPAM", "Year": 2013, "Hero": "Kamal Haasan"},
    {"Name": "VELAIYILLA PATTATHARI", "Year": 2014, "Hero": "Dhanush"},
    {"Name": "KATHI", "Year": 2014, "Hero": "Vijay"},
    {"Name": "I", "Year": 2015, "Hero": "Vikram"},
    {"Name": "THERI", "Year": 2016, "Hero": "Vijay"},
    {"Name": "KABALI", "Year": 2016, "Hero": "Rajinikanth"},
    {"Name": "MERSAL", "Year": 2017, "Hero": "Vijay"},
    {"Name": "VIKRAM VEDHA", "Year": 2017, "Hero": "Madhavan"},
    {"Name": "96", "Year": 2018, "Hero": "Vijay Sethupathi"},
    {"Name": "PETTA", "Year": 2019, "Hero": "Rajinikanth"},
    {"Name": "ASURAN", "Year": 2019, "Hero": "Dhanush"},
    {"Name": "KAITHI", "Year": 2019, "Hero": "Karthi"},
    {"Name": "SOORARAI POTTRU", "Year": 2020, "Hero": "Suriya"},
    {"Name": "MASTER", "Year": 2020, "Hero": "Vijay"},
    {"Name": "DARBAR", "Year": 2020, "Hero": "Rajinikanth"},
    {"Name": "KAAKI SATTAI", "Year": 2015, "Hero": "Sivakarthikeyan"},
    {"Name": "KODI", "Year": 2016, "Hero": "Dhanush"},
    {"Name": "ANEGAN", "Year": 2015, "Hero": "Dhanush"},
    {"Name": "VADA CHENNAI", "Year": 2018, "Hero": "Dhanush"},
    {"Name": "KURANGU BOMMAI", "Year": 2017, "Hero": "Vidharth"},
    {"Name": "TIK TIK TIK", "Year": 2018, "Hero": "Jayam Ravi"},
    {"Name": "THANI ORUVAN", "Year": 2015, "Hero": "Jayam Ravi"},
    {"Name": "KO", "Year": 2011, "Hero": "Jeeva"},
    {"Name": "KUTTI", "Year": 2010, "Hero": "Dhanush"},
    {"Name": "VETTAIKARAN", "Year": 2009, "Hero": "Vijay"},
    {"Name": "AADUKALAM", "Year": 2011, "Hero": "Dhanush"},
    {"Name": "ARRAMBAM", "Year": 2013, "Hero": "Ajith Kumar"},
    {"Name": "MANKATHA", "Year": 2011, "Hero": "Ajith Kumar"},
    {"Name": "ENNAI ARINDHAAL", "Year": 2015, "Hero": "Ajith Kumar"},
    {"Name": "VEERAM", "Year": 2014, "Hero": "Ajith Kumar"},
    {"Name": "KOMARAM PULI", "Year": 2010, "Hero": "Pawan Kalyan"},
    {"Name": "JILLA", "Year": 2014, "Hero": "Vijay"},
    {"Name": "VELAYUDHAM", "Year": 2011, "Hero": "Vijay"},
    {"Name": "KAVALAN", "Year": 2011, "Hero": "Vijay"},
    {"Name": "BILLA 2", "Year": 2012, "Hero": "Ajith Kumar"},
    {"Name": "BAIRAVAA", "Year": 2017, "Hero": "Vijay"},
    {"Name": "KABALI", "Year": 2016, "Hero": "Rajinikanth"},
    {"Name": "ANBUDAN KATHALAN", "Year": 2016, "Hero": "Vijay Sethupathi"},
    {"Name": "NADUVULA KONJAM PAKKATHA KAANOM", "Year": 2012, "Hero": "Vijay Sethupathi"},
    {"Name": "SOODHU KAVVUM", "Year": 2013, "Hero": "Vijay Sethupathi"},
    {"Name": "KADHALUM KADANTHU POGUM", "Year": 2016, "Hero": "Vijay Sethupathi"},
    {"Name": "ORU NALLA NAAL PAATHU SOLREN", "Year": 2018, "Hero": "Vijay Sethupathi"},
    {"Name": "SEETHAKATHI", "Year": 2018, "Hero": "Vijay Sethupathi"},
    {"Name": "PETTA", "Year": 2019, "Hero": "Rajinikanth"},
    {"Name": "SARKAR", "Year": 2018, "Hero": "Vijay"},
    {"Name": "JIGARTHANDA", "Year": 2014, "Hero": "Siddharth"},
    {"Name": "IRAIVI", "Year": 2016, "Hero": "S. J. Surya"},
    {"Name": "PRIYAMANAVALE", "Year": 2000, "Hero": "Vijay"},
    {"Name": "KASADA TABARA", "Year": 2020, "Hero": "Shantanu Bhagyaraj"},
    {"Name": "MAYA", "Year": 2015, "Hero": "Nayanthara"},
    {"Name": "ARAM", "Year": 2017, "Hero": "Nayanthara"},
    {"Name": "COLLECTOR", "Year": 2019, "Hero": "Jeeva"},
    {"Name": "YENNAI ARINDHAAL", "Year": 2015, "Hero": "Ajith Kumar"},
    {"Name": "VISWASAM", "Year": 2019, "Hero": "Ajith Kumar"},
    {"Name": "VIVEGAM", "Year": 2017, "Hero": "Ajith Kumar"},
    {"Name": "MAANKARATE", "Year": 2014, "Hero": "Sivakarthikeyan"},
    {"Name": "REMOS", "Year": 2016, "Hero": "Sivakarthikeyan"},
    {"Name": "SEEMA RAJA", "Year": 2018, "Hero": "Sivakarthikeyan"},
    {"Name": "MR LOCAL", "Year": 2019, "Hero": "Sivakarthikeyan"},
    {"Name": "HERO", "Year": 2019, "Hero": "Sivakarthikeyan"},
    {"Name": "VIKRAM", "Year": 2020, "Hero": "Kamal Haasan"},
    {"Name": "KAITHI", "Year": 2019, "Hero": "Karthi"},
    {"Name": "RAJA RANI", "Year": 2013, "Hero": "Arya"},
    {"Name": "MADRAS", "Year": 2014, "Hero": "Karthi"},
    {"Name": "THALAIVAR", "Year": 2013, "Hero": "Rajinikanth"},
    {"Name": "PULI", "Year": 2015, "Hero": "Vijay"},
    {"Name": "VIKRAM VEDHA", "Year": 2017, "Hero": "Madhavan"},
    {"Name": "MERSAL", "Year": 2017, "Hero": "Vijay"},
    {"Name": "JOKER", "Year": 2016, "Hero": "Guru Somasundaram"},
    {"Name": "NGK", "Year": 2019, "Hero": "Suriya"},
    {"Name": "BIGIL", "Year": 2019, "Hero": "Vijay"}
    ]

@app.route('/')
def default():
    return render_template('home.html', warn='')

@app.route('/start', methods=['POST','GET'])
def start():
    number = randint(1,100)
    global dashes
    dashes = []
    global single_movie
    single_movie = tamil_movies[number]["Name"]
    print(single_movie)
    global actor
    actor = tamil_movies[number]["Hero"]
    global guessed_letters
    guessed_letters = []
    global lives
    lives = 5
    for i in single_movie:
        if i == " ":
            dashes.append(" ")
        else:
            dashes.append("_ ")
    print(dashes)
    return render_template('gameplay.html', l = ''.join(dashes), lives=lives, warn='', game_image_url=lives)

@app.route('/play', methods=['POST','GET'])
def play():
    global lives
    global guessed_letters
    guess = request.form.get("movie_letter").upper()
    if guess not in guessed_letters:
        guessed_letters.append(guess)
        print(' '.join(guessed_letters))
    else:
        msg = guess + " already entered"
        return render_template('gameplay.html', msg=msg, l=''.join(dashes), lives=lives, guessed=sorted(''.join(guessed_letters)), game_image_url=lives)

    for index, i in enumerate(single_movie):
        if guess == single_movie[index]:
            dashes[index] = guess
        else:
            if guess.upper() not in single_movie:
                # warn = guess + " not present &#128531;. You lost a life &#128148;"
                lives = lives - 1
                if lives > 0:
                    return render_template('gameplay.html', warn=guess, l = ''.join(dashes), lives = lives, guessed=sorted(''.join(guessed_letters)), game_image_url=lives)
                else:
                    return render_template('gameplay.html', won="You lost:)", l=single_movie, lives=lives, guessed='', game_image_url="lost")


    if ''.join(dashes) == single_movie:
        return render_template('gameplay.html', won="Yeah, You guessed it!", l = ''.join(dashes), warn='', lives = 0, guessed='', game_image_url="win")
    if lives > 0:
        return render_template('gameplay.html', l = ''.join(dashes), lives=lives, guessed=sorted(''.join(guessed_letters)), game_image_url=lives)
    else:
        return render_template('gameplay.html', won="You lost:)", l=single_movie, lives = 0, guessed='', game_image_url="lost")

@app.route('/clue', methods=['POST','GET'])
def clue():
    global actor
    return render_template('gameplay.html', l=''.join(dashes), lives=lives, guessed=sorted(''.join(guessed_letters)),
                           game_image_url=lives, clue=actor)

@app.route('/reset', methods=['POST','GET'])
def reset():
    return redirect(url_for('start'))

if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=5000)
