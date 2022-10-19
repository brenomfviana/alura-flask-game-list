from flask import (
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for,
)
from app import app, db
from models import Game, User
from services import AuthService, RouteService, GameService


@app.route("/")
def index():
    games = GameService().list()
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
    user = User.query.filter_by(nickname=request.form["user"]).first()
    if user:
        if request.form["password"] == user.password:
            session["user"] = user.nickname
            flash(user.nickname + " logado com sucesso!")
            next_page = request.form["next"]
            if next_page:
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
    if AuthService().is_authenticated(session=session):
        return RouteService().redirect(
            redirect_page="login",
            next_page="new",
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

    if GameService().get(name=name):
        flash("O jogo já está registrado!")
    else:
        GameService().create(
            name=name,
            category=category,
            platform=platform,
        )

    return redirect(url_for("index"))


@app.route("/edit/<int:id>")
def edit(id):
    if AuthService().is_authenticated(session=session):
        return RouteService().redirect(
            redirect_page="login",
            next_page="edit",
        )

    game = GameService().get(id=id)

    return render_template(
        "edit_game.html",
        title="Edit Game",
        game=game,
    )


@app.route(
    "/update",
    methods=[
        "POST",
    ],
)
def update():
    id = request.form["id"]

    GameService().update(
        id=id,
        name=request.form["name"],
        category=request.form["category"],
        platform=request.form["platform"],
    )

    return redirect(url_for("index"))
