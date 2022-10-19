from flask import session
from models import User

from .user import UserService


class AuthService:
    USER_KEY = "user"
    PASSWORD_KEY = "password"

    def __init__(self) -> None:
        self.session = session

    def authenticate(
        self,
        *_,
        data=None,
    ) -> bool:
        user = UserService().get(nickname=data[self.USER_KEY])
        if user and user.password == data[self.PASSWORD_KEY]:
            self.session[self.USER_KEY] = user.nickname
            return True
        return False

    def logout(self) -> bool:
        if self.USER_KEY in self.session:
            del self.session[self.USER_KEY]
            return True
        return False

    def is_authenticated(self) -> bool:
        exists = self.USER_KEY in self.session
        is_none = exists and not self.session[self.USER_KEY]
        return exists or is_none

    def get_user(self) -> User:
        if self.USER_KEY in self.session:
            user = self.session[self.USER_KEY]
            return UserService().get(nickname=user)
        return None
