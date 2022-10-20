from app import app
from flask import render_template
from services import AuthService, GameService


@app.route("/")
def index():
    games = GameService().list()
    user = AuthService().get_user()

    return render_template(
        "index.html",
        title="Jogos",
        games=games,
        user=user,
    )
