"""
File name: game.py
Authors: Grant Holmes, Luke Less'Ard-Springett, Fares Elattar, Peyton Doherty, Luke Beesley
Description: Game driver
Date: 09/13/20
"""

from core.engine import Engine
from core.state import State

class Game:
	"""
		Description: Provides a game entity that represents the entirety of the game. Game is composed of engine
				     to render graphics and to maintain frame rate and a state which handles game logic.

	"""

	engine = Engine()
	state = State()

	def __init__(self):
		pass

	def run(self) -> None:
		"""
		Runs game. Calls run_event from state to signal that next event should be executed.
		keep_running returns false when "X" in top right corner of game window is clicked
		"""
		while self.engine.should_run():
			self.engine.clear_screen()
			self.state.run_event(self.engine.get_dt())
			self.engine.update_screen(self.state.get_objects_to_render(), self.state.get_sprites())
