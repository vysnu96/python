# import the Flask library
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def hello_world():
    if request.method == "POST":
        print("From if")
        if request.args.get("username") == None:
            return render_template('sample.html')
        else:
            username = request.args.get('username')
            password = request.args.get('password')
            credentials = open('credentials.txt', mode='w', encoding='utf-8')
            credentials.write(f"Username: {username}" + '\n')
            credentials.write(f"Password: {password}")
            credentials.close()
            return "Your credentials are stored in a file"


#
# @app.route('/square', methods=['GET'])
# def squarenumber():
#     # If method is GET, check if  number is entered
#     # or user has just requested the page.
#     # Calculate the square of number and pass it to
#     # answermaths method
#     if request.method == 'GET':
#         # If 'num' is None, the user has requested page the first time
#         if (request.args.get('num') == None):
#             return render_template('squarenum.html')
#         # If user clicks on Submit button without
#         # entering number display error
#         elif (request.args.get('num') == ''):
#             return "<html><body> <h1 style= ""color:blue"">Invalid number</h1></body></html>"
#         else:
#             # User has entered a number
#             # Fetch the number from args attribute of
#             # request accessing its 'id' from HTML
#             number = request.args.get('num')
#             sq = int(number) * int(number)
#             # pass the result to the answer HTML
#             # page using Jinja2 template
#             return render_template('answer.html',
#                                    squareofnum=sq, num=number)


# Start with flask web app with debug as
# True only if this is the starting page
if (__name__ == "__main__"):
    app.run(debug=True)
