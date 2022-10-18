from app import db


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(40), nullable=False)
    platform = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"{self.name}"
