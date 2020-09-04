"""
Driver of game, this modules keeps game running and calls for events to run.
"""

from core.engine import Engine
from core.state import State

class Game:
	
	engine = Engine()
	state = State()

	def __init__(self):
		pass

	def run(self):
		while self.engine.keep_running():
			self.engine.clear_screen()
			self.state.run_event(self.engine.get_dt())
			self.engine.update_screen(self.state.get_text_to_display())
