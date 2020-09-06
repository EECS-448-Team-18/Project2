"""
File name: game.py
Authors:
Description:
Date:
Description: Game driver

Classes:
	Game
"""

from core.engine import Engine
from core.state import State

class Game:
	"""
	Game()
	
	Provides a game entity that represents the entirety of the game. Game is composed of engine
		to render graphics and to maintain frame rate and a state which handles game logic.

	Methods:
		run() -> None
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
			self.engine.update_screen(self.state.get_text_to_display())
