from app import app
from flask import flash, render_template, request, send_from_directory
from services import (
    AuthService,
    GameService,
    GameValidatorService,
    ImageService,
    RedirectService,
)


@app.route("/new")
def new():
    if not AuthService().is_authenticated():
        return RedirectService().to_login(next_page="new")

    form = GameValidatorService().get_validator_form()

    return render_template(
        "new_game.html",
        title="New Game",
        form=form,
    )


@app.route("/edit/<int:id>")
def edit(id):
    if not AuthService().is_authenticated():
        return RedirectService().to_login(next_page="edit")

    game = GameService().get(id=id)

    form = GameValidatorService().get_validator_form()
    form.name.data = game.name
    form.category.data = game.category
    form.platform.data = game.platform

    cover = ImageService().get_image(id=id)

    return render_template(
        "edit_game.html",
        title="Edit Game",
        id=game.id,
        form=form,
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
    form = GameValidatorService().get_validator_form()

    if not form.validate_on_submit():
        return RedirectService().to_page("new")

    name = form.name.data
    category = form.category.data
    platform = form.platform.data

    if GameService().get(name=name):
        flash("O jogo já está registrado!")
    else:
        game = GameService().create(
            name=name,
            category=category,
            platform=platform,
        )

        picture = request.files["file"]
        ImageService().add(
            picture=picture,
            game=game,
        )

    return RedirectService().to_index()


@app.route(
    "/update",
    methods=[
        "POST",
    ],
)
def update():
    form = GameValidatorService().get_validator_form()

    if form.validate_on_submit():
        id = request.form["id"]

        game = GameService().update(
            id=id,
            name=form.name.data,
            category=form.category.data,
            platform=form.platform.data,
        )

        picture = request.files["file"]
        ImageService().add(
            picture=picture,
            game=game,
        )

    return RedirectService().to_index()


@app.route("/uploads/<filename>")
def image(filename):
    return send_from_directory(app.config["UPLOAD_PATH"], filename)
