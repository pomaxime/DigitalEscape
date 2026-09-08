from .game_element import GameElement


class Room(GameElement):
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        items: list | None = None,
        doors: list | None = None,
        puzzles: list | None = None,
    ):
        super().__init__(id, name, description)
        self.items = items or []
        self.doors = doors or []
        self.puzzles = puzzles or []

    def to_dict(self):
        return {
            **super().to_dict(),
            "items": self.items,
            "doors": self.doors,
            "puzzles": self.puzzles,
        }

    def add_item(self, item):
        self.items.append(item)

    def add_door(self, door):
        self.doors.append(door)

    def add_puzzle(self, puzzle):
        self.puzzles.append(puzzle)
