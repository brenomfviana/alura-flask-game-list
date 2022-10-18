from flask import Flask, render_template, request, redirect, session, flash, url_for
from models import *


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
    _next = request.args.get("next")
    return render_template(
        "login.html",
        next=_next,
    )


@app.route(
    "/authenticate",
    methods=[
        "POST",
    ],
)
def authenticate():
    if request.form["user"] in users:
        user = users[request.form["user"]]
        if request.form["password"] == user.password:
            session["user"] = user.nickname
            flash(user.nickname + " logado com sucesso!")
            next_page = request.form["next"]
            if not next_page:
                return redirect(next_page)
            return redirect(url_for("index"))
    flash("Usuário ou senha inválidos!")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session["user"] = None
    flash("Logout efetuado com sucesso!")
    return redirect(url_for("login"))


@app.route("/new")
def new():
    if "user" not in session or not session["user"]:
        return redirect(
            url_for(
                "login",
                next=url_for("new"),
            ),
        )

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
    return redirect(url_for("index"))


app.run(debug=True)
