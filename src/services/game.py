from typing import List

from app import db
from models import Game


class GameService:
    def get(
        self,
        *_,
        **kwargs,
    ) -> Game:
        return Game.query.filter_by(**kwargs).first()

    def list(
        self,
        *_,
        order_by=None,
    ) -> List[Game]:
        if not order_by:
            order_by = Game.id
        return Game.query.order_by(order_by)

    def create(
        self,
        *_,
        **kwargs,
    ) -> Game:
        game = Game(**kwargs)
        db.session.add(game)
        db.session.commit()
        return game

    def update(
        self,
        *_,
        **kwargs,
    ) -> Game:
        id = kwargs.pop("id", None)
        game = GameService().get(id=id)
        if game:
            game.name = kwargs.pop("name", None)
            game.category = kwargs.pop("category", None)
            game.platform = kwargs.pop("platform", None)
            db.session.add(game)
            db.session.commit()
        return game

    def delete(
        self,
        *_,
        id=None,
    ) -> Game:
        Game.query.filter_by(id=id).delete()
        db.session.commit()
