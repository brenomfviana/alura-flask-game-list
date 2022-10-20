from flask_bcrypt import check_password_hash

from flask import session
from models import User

from .user import UserService


class AuthService:
    USER_KEY = "user"

    def __init__(self) -> None:
        self.session = session

    def authenticate(
        self,
        *_,
        form=None,
    ) -> bool:
        user = UserService().get(nickname=form.nickname.data)
        if user and check_password_hash(user.password, form.password.data):
            self.session[self.USER_KEY] = user.nickname
            return True
        return False

    def logout(self) -> bool:
        if self.USER_KEY in self.session:
            del self.session[self.USER_KEY]
            return True
        return False

    def is_authenticated(self) -> bool:
        return bool(self.get_user())

    def get_user(self) -> User:
        if self.USER_KEY in self.session:
            user = self.session[self.USER_KEY]
            return UserService().get(nickname=user)
        return None
