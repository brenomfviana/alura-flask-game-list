from flask_bcrypt import check_password_hash

from flask import session
from models import User
from constants import USER_KEY

from .user import UserService


class AuthService:
    def __init__(self) -> None:
        self.session = session

    def authenticate(
        self,
        *_,
        form=None,
    ) -> bool:
        user = UserService().get(nickname=form.nickname.data)
        if user and check_password_hash(user.password, form.password.data):
            self.session[USER_KEY] = user.nickname
            return True
        return False

    def logout(self) -> bool:
        if USER_KEY in self.session:
            del self.session[USER_KEY]
            return True
        return False

    def is_authenticated(self) -> bool:
        return bool(self.get_user())

    def get_user(self) -> User:
        if USER_KEY in self.session:
            user = self.session[USER_KEY]
            return UserService().get(nickname=user)
        return None
