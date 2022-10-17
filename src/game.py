class Game:
    def __init__(
        self,
        *,
        name: str,
        category: str,
        platform: str,
    ) -> None:
        self.name = name
        self.category = category
        self.platform = platform
