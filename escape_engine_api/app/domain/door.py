from .game_element import GameElement


class Door(GameElement):
	def __init__(
		self,
		id: str,
		name: str,
		description: str,
		is_locked: bool = False,
		required_item_id: str | None = None,
	):
		super().__init__(id, name, description)
		self.is_locked = is_locked
		self.required_item_id = required_item_id
