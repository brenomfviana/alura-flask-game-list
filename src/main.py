from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "alura"
uri = "{dbms}://{user}:{password}@{server}/{database}".format(
    dbms="mysql+mysqlconnector",
    user="root",
    password="#Admin123",
    server="localhost",
    database="jogoteca",
)
app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(40), nullable=False)
    platform = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}"


class User(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}"


class User(db.Model):
    def __init__(
        self,
        *,
        name: str = None,
        nickname: str = None,
        password: str = None,
    ) -> None:
        self.name = name
        self.nickname = nickname
        self.password = password


@app.route("/")
def index():
    games = Game.query.order_by(Game.id)
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

    game = Game.query.filter_by(
        name=name,
    ).first()

    if game:
        flash("O jogo já está registrado!")
    else:
        new_game = Game(
            name=name,
            category=category,
            platform=platform,
        )
        db.session.add(new_game)
        db.session.commit()

    return redirect(url_for("index"))


app.run(debug=True)
