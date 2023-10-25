from flask import Flask
from random import randint
app = Flask(__name__)

number = randint(0,9)

@app.route('/')
def hello_world():
    return '<h1 style="text-align:center; padding:80px">guess the number</h1>' \
        '<br>' \
        '<img style="display:block; margin-left:auto; margin-right:auto; width:50%;" src="https://media.giphy.com/media/bff7tTkTvW38numiG9/giphy.gif?cid=ecf05e47rd2i5lxy6hcgyyc3dxzysjp9ej9673atzkrre7or&ep=v1_gifs_trending&rid=giphy.gif&ct=g" alt"happy image Kevin Durant Dunking" width=500 height=500>'

@app.route("/<int:guess>")
def guess_the_number(guess):
    # guess = int(guess)
    if guess < number:
        return f'<h1 style="text-align:center; padding:80px">{guess} is too low, guess higher</h1>' \
            '<br>' \
            '<img style="display:block; margin-left:auto; margin-right:auto; width:50%;" src="https://media.giphy.com/media/hWr7cQE2ALhvmLlKm2/giphy.gif?cid=ecf05e47bscspu09bndyb0fnvhcw6p02txo6rc1h6ckih5mh&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt"higher faster stronger" width=500 height=500>'
    if guess > number:
        return f'<h1 style="text-align:center; padding:80px">{guess} is too high, guess lower</h1>' \
            '<br>' \
            '<img style="display:block; margin-left:auto; margin-right:auto; width:50%;" src="https://media.giphy.com/media/vqLZK6Kg4tfQSzh8wv/giphy.gif?cid=ecf05e47ifgjveb30kz96c736z7j42wyb1nuww89zn3g7kcc&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt"lower your expectations" width=500 height=500>'
    else:
        return f'<h1 style="text-align:center; padding:80px">Correct!! {guess} = {number}</h1>' \
            '<br>' \
            '<img style="display:block; margin-left:auto; margin-right:auto; width:50%;" src="https://giphy.com/clips/viralhog-viral-hog-otter-claps-and-taps-for-clams-vfI3uwl4FMuDaLbZah" alt"clapping otters" width=500 height=500>'

if __name__ == "__main__":
    app.run(debug=True)