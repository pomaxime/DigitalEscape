from .game_element import GameElement


class Item(GameElement):
    def __init__(self, id: str, name: str, description: str, item_type: str):
        super().__init__(id, name, description)
        self.item_type = item_type

    def to_dict(self):
        return {
            **super().to_dict(),
            "item_type": self.item_type,
        }


class Key(Item):
    def __init__(self, id: str, name: str, description: str):
        super().__init__(id, name, description, "key")


class Ribs(Item):
    def __init__(self, id: str, name: str, description: str):
        super().__init__(id, name, description, "ribs")
