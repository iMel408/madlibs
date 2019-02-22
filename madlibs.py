"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """Ask user if they want to play"""

    play = request.args.get('play')


    if play == 'yes':
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Ask user if they want to play"""

    color = request.args.get('color')
    noun = request.args.get('noun')
    author = request.args.get('author')
    adjective = request.args.get('adjective')

    # print(request.args.get('food'))

    if request.args.get('food') == 'pizza':
        food = 'pizza'
    elif request.args.get('food') == 'sushi':
        food = 'sushi'
    else:
        food = 'burrito'

    return render_template("madlib.html",
        color=color, noun=noun, author=author, adjective=adjective, food=food)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also

    app.run(debug=True)
