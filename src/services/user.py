from typing import List
from models import User
from app import db


class UserService:
    def get(
        self,
        *_,
        **kwargs,
    ) -> User:
        return User.query.filter_by(**kwargs).first()

    def list(
        self,
        *_,
        order_by=None,
    ) -> List[User]:
        if not order_by:
            order_by = User.id
        return User.query.order_by(order_by)

    def create(
        self,
        *_,
        **kwargs,
    ) -> User:
        user = User(**kwargs)
        db.session.add(user)
        db.session.commit()
        return user

    def update(
        self,
        *_,
        **kwargs,
    ) -> User:
        id = kwargs.pop("id", None)
        user = UserService().get(id=id)

        if user:
            user.name = kwargs.pop("name", None)
            user.category = kwargs.pop("category", None)
            user.platform = kwargs.pop("platform", None)

            db.session.add(user)
            db.session.commit()

        return user
