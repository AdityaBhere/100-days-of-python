from flask import Flask
from random import randint

app = Flask(__name__)

answer = randint(0,9)

@app.route("/")
def game_start():
    return (f'<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

@app.route("/<int:choice>")
def game(choice):
    if choice > answer:
        return (f'<h1">Too high try again!</h1>'
                '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3U0cGh3ZWtqbWJ0d29uY2YwZHhwZGducWFveXRmZjdsNm80Zm1jaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/879KMuZIxobrW/giphy.gif">')

    elif choice < answer:
        return (f'<h1>Too low try again!</h1>'
                '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3U0cGh3ZWtqbWJ0d29uY2YwZHhwZGducWFveXRmZjdsNm80Zm1jaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/879KMuZIxobrW/giphy.gif">')

    else:
        return (f'<h1">You found me!</h1>'
                '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjhrcnQxMmliMnprN3E0amt1NWxkcHRpMm5meHZyYXNmYW1vZjIwbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/T70hpBP1L0N7U0jtkq/giphy.gif">')

if __name__ == "__main__":
    app.run(debug=True)