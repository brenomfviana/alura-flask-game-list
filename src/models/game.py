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
