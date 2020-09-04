"""
Tracks game state and contains game events.
"""

from core.board import Board
from core import peripherals  # checks for mouse and keyboard stuff

class State:

	def __init__(self):
		# main game components
		self.p1_board = Board()
		self.p2_board = Board()

		self.events = {  # these events are all just examples, replace with actual events as needed
					"start": {"run_event": self.start, "is_time_dependent": False},
					"end_turn": {"run_event": self.end_turn, "is_time_dependent": False},
					"place_ships": {"run_event": self.place_ships, "is_time_dependent": False},
					"loop": {"run_event": self.loop, "is_time_dependent": False},
				}
		
		# game state attributes
		self.prev_event = None
		self.curr_event = "start"

	def run_event(self, dt):
		if self.events[self.curr_event]["is_time_dependent"]:
			self.events[self.curr_event]["run_event"](dt)
		else:
			self.events[self.curr_event]["run_event"]()
		
		self.prev_event = self.curr_event
		self.curr_event = self.get_next_event()
	
		self.update()

	def get_next_event(self):
		if self.prev_event == "start":
			return "place_ships"

		if self.prev_event == "place_ships":
			return "end_turn"

		if self.prev_event == "end_turn":
			return "loop"

		if self.prev_event == "loop":
			return "loop"

	def get_text_to_display(self):
		# test values to show function, change later
		test_values = ("test_1", "test_2", "test_3")
		return test_values

	def update(self):
		return

	# events... examples right now, implement real events as needed. They shouldnt return anything
	def start(self):
		pass

	def end_turn(self):
		pass
	
	def place_ships(self):
		pass

	def loop(self):
		pass
