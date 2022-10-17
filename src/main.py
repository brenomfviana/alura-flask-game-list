from flask import Flask, render_template, request, redirect
from game import Game

app = Flask(__name__)

games = [
    Game(
        name="God of War",
        category="Hack'n Slash",
        platform="PS2",
    ),
    Game(
        name="Mortal Combat",
        category="Fighting",
        platform="PS3",
    ),
    Game(
        name="Crash Bandicoot",
        category="Adventure",
        platform="PS1",
    ),
    Game(
        name="Valorant",
        category="FPS",
        platform="PC",
    ),
    Game(
        name="Tetris",
        category="Puzzle",
        platform="Atari",
    ),
]


@app.route("/")
def index():
    return render_template(
        "game_list.html",
        title="Jogos",
        games=games,
    )


@app.route("/new")
def new():
    return render_template(
        "new_game.html",
        title="New Game",
    )


@app.route(
    "/create",
    methods=[
        "POST",
    ],
)
def create():
    name = request.form["name"]
    category = request.form["category"]
    platform = request.form["platform"]
    game = Game(
        name=name,
        category=category,
        platform=platform,
    )
    games.append(game)
    return redirect("/")


app.run(debug=True)
