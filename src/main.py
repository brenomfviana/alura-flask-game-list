from flask import Flask, render_template
from game import Game

app = Flask(__name__)


@app.route("/")
def run():
    games = [
        Game(
            name="God of War",
            category="Rack'n Slash",
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
    return render_template(
        "game_list.html",
        title="Jogos",
        games=games,
    )


app.run()
