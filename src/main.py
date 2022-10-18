from flask import Flask, render_template, request, redirect, session, flash
from game import Game

app = Flask(__name__)
app.secret_key = "alura"

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


@app.route("/login")
def login():
    return render_template(
        "login.html",
    )


@app.route(
    "/authenticate",
    methods=[
        "POST",
    ],
)
def authenticate():
    if request.form["password"] == "1234":
        session["user"] = request.form["user"]
        flash(session["user"] + " logado com sucesso!")
        return redirect("/")
    flash("Usuário ou senha inválidos!")
    return redirect("/login")


@app.route("/logout")
def logout():
    session["user"] = None
    flash("Logout efetuado com sucesso!")
    return redirect("/login")


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
