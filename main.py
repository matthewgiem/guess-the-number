from flask import Flask
from random import randint
app = Flask(__name__)

number = randint(0,9)

@app.route('/')
def hello_world():
    return 'guess the number'

@app.route("/<int:guess>")
def guess_the_number(guess):
    # guess = int(guess)
    if guess < number:
        return f"{guess} is too low, guess higher"
    if guess > number:
        return f"{guess} is too high, guess lower"
    else:
        return f"Correct!! {guess} = {number}"

if __name__ == "__main__":
    app.run(debug=True)