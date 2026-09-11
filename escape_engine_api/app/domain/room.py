from .game_element import GameElement


class Room(GameElement):
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        Items: list | None = None,
        doors: list | None = None,
        puzzles: list | None = None,
        time_limit: int | None = None,
    ):
        super().__init__(id, name, description)
        self.Items = Items or []
        self.doors = doors or []
        self.puzzles = puzzles or []
        self.time_limit = time_limit

    def to_dict(self):
        return {
            **super().to_dict(),
            "Items": self.Items,
            "doors": self.doors,
            "puzzles": self.puzzles,
            "time_limit": self.time_limit,
        }

    def add_item(self, item):
        self.Items.append(item)

    def add_door(self, door):
        self.doors.append(door)

    def add_puzzle(self, puzzle):
        self.puzzles.append(puzzle)

