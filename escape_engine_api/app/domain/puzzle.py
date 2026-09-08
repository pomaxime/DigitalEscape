from .game_element import GameElement


class Puzzle(GameElement):
	def check_solution(self, answer: str) -> bool:
		raise NotImplementedError
