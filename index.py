from flask import Flask, render_template, request, jsonify, make_response
import random

app = Flask(__name__)

choices = ("Paper", "Rock", "Scissors")

@app.route("/")
def index():
    ''' 
        Render the page to select the option
        (paper, rock or scissors)
    '''
    return render_template("index.html")


@app.route("/process", methods = ['POST'])
def process():
    ''' 
        Process the user option and compare
        to the computer option
    '''
    user_option = request.get_json().get('user_option')
    computer_option = get_computer_option()

    if (user_option == "Paper" and computer_option == "Rock") or (user_option == "Rock" and computer_option == "Scissors") or (user_option == "Scissors" and computer_option == "Paper"):
        winner = "User"
    elif user_option == computer_option:
        winner = "Draw"
    else:
        winner = "Computer"

    response = make_response(
        jsonify(
            {
                'winner': winner,
                'user_option': user_option,
                'computer_option': computer_option
            }
        ),
        200,
    )
    response.headers["Content-Type"] = "application/json"
    return response


def get_computer_option():
    ''' 
        Provides a string representing 
        the random computer option
    '''
    return choices[random.randint(0,2)]


if __name__ == "__main__":
    app.run(debug=True)
