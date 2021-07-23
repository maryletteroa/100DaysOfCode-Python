from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1> \
    <p>This is a paragraph</p> \
    <img width=200px src='https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif'>"


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper
def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper
def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old"

if __name__ == "__main__":
    app.run(debug=True)