class User:
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


user1 = User(name="Breno Viana", nickname="Breno", password="1234")
user2 = User(name="Raymara Almeida", nickname="Ray", password="enzogabriel")

users = {
    user1.nickname: user1,
    user2.nickname: user2,
}
