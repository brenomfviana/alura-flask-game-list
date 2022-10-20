from app import app
from flask import flash, render_template, request
from services import AuthService, RedirectService, UserLoginValidatorService

NEXT_PAGE = "next"


@app.route("/login")
def login():
    form = UserLoginValidatorService().get_validator_form()

    kwargs = {"form": form}

    next_page = request.args.get(NEXT_PAGE)
    if next_page:
        kwargs[NEXT_PAGE] = next_page

    return render_template(
        "login.html",
        **kwargs,
    )


@app.route(
    "/authenticate",
    methods=[
        "POST",
    ],
)
def authenticate():
    form = UserLoginValidatorService().get_validator_form()

    if AuthService().authenticate(form=form):
        user = AuthService().get_user()
        flash(user.nickname + " logado com sucesso!")

        next_page = request.form[NEXT_PAGE]
        if next_page:
            return RedirectService().to_page(page=next_page)

        return RedirectService().to_index()

    flash("Usuário ou senha inválidos!")

    return RedirectService().to_login()


@app.route("/logout")
def logout():
    AuthService().logout()
    flash("Logout efetuado com sucesso!")
    return RedirectService().to_login()
