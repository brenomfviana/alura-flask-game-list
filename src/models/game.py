class Game:
    def __init__(
        self,
        *,
        name: str = None,
        category: str = None,
        platform: str = None,
    ) -> None:
        self.name = name
        self.category = category
        self.platform = platform


games = [
    Game(
        name="God of War",
        category="Hack'n Slash",
        platform="PS2",
    ),
    Game(
        name="Mortal Combat",
        category="Fighting",
        platform="PS3",
    ),
    Game(
        name="Crash Bandicoot",
        category="Adventure",
        platform="PS1",
    ),
    Game(
        name="Valorant",
        category="FPS",
        platform="PC",
    ),
    Game(
        name="Tetris",
        category="Puzzle",
        platform="Atari",
    ),
]
