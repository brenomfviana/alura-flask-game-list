from app import app
from flask import flash, render_template, request, send_from_directory
from services import AuthService, GameService, ImageService, RedirectService

NEXT_PAGE = "next"


@app.route("/")
def index():
    games = GameService().list()
    user = AuthService().get_user()

    return render_template(
        "game_list.html",
        title="Jogos",
        games=games,
        user=user,
    )


@app.route("/login")
def login():
    next_page = request.args.get(NEXT_PAGE)

    if next_page:
        return render_template(
            "login.html",
            next=next_page,
        )
    else:
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
    if AuthService().authenticate(data=request.form):
        user = AuthService().get_user()
        flash(user.nickname + " logado com sucesso!")

        next_page = request.form[NEXT_PAGE]
        if next_page and next_page != "None":
            return RedirectService().to_page(page=next_page)

        return RedirectService().to_index()

    flash("Usuário ou senha inválidos!")

    return RedirectService().to_login()


@app.route("/logout")
def logout():
    AuthService().logout()
    flash("Logout efetuado com sucesso!")
    return RedirectService().to_login()


@app.route("/new")
def new():
    if not AuthService().is_authenticated():
        return RedirectService().to_login(next_page="new")

    return render_template(
        "new_game.html",
        title="New Game",
    )


@app.route("/edit/<int:id>")
def edit(id):
    if not AuthService().is_authenticated():
        return RedirectService().to_login(next_page="edit")

    game = GameService().get(id=id)
    cover = ImageService().get_image(id=id)

    return render_template(
        "edit_game.html",
        title="Edit Game",
        game=game,
        cover=cover,
    )


@app.route("/delete/<int:id>")
def delete(id):
    if not AuthService().is_authenticated():
        return RedirectService().to_login()

    GameService().delete(id=id)

    flash("Jogo deletado com sucesso!")

    return RedirectService().to_index()


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
        game = GameService().create(
            name=name,
            category=category,
            platform=platform,
        )

        picture = request.files["file"]
        picture_name = ImageService().new_name(id=game.id)
        picture.save(picture_name)

    return RedirectService().to_index()


@app.route(
    "/update",
    methods=[
        "POST",
    ],
)
def update():
    id = request.form["id"]

    game = GameService().update(
        id=id,
        name=request.form["name"],
        category=request.form["category"],
        platform=request.form["platform"],
    )

    ImageService().delete_image(id=game.id)

    picture = request.files["file"]
    picture_name = ImageService().new_name(id=game.id)
    picture.save(picture_name)

    return RedirectService().to_index()


@app.route("/uploads/<filename>")
def image(filename):
    return send_from_directory(app.config["UPLOAD_PATH"], filename)
