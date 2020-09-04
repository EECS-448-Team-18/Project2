"""
Tracks game state and contains game events.
"""

from core.board import Board
from core import peripherals  # checks for mouse and keyboard stuff
from data.assets import colors
from time import time

class State:

	def __init__(self):
		# main game components
		self.p1_board = Board()
		self.p2_board = Board()

		self.events = {  # these events are all just examples, replace with actual events as needed
					"start": Event(self.start, False),
					"end_turn": Event(self.end_turn, False),
					"place_ships": Event(self.place_ships, False),
					"loop": Event(self.loop, False),
				}
		
		# game state attributes
		self.prev_event = None
		self.curr_event = "start"

		self.timer = time()

	def run_event(self, dt):
		self.events[self.curr_event](dt)
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
		output = []
		if self.curr_event == "loop" and int(self.get_game_time())%2==0:
			output.append(Text("test_1", (100, 100), 36, colors["green"]))
			output.append(Text("test_2", (200, 175), 30, (255, 0, 255)))

		return tuple(output)

	def update(self):
		return

	def get_game_time(self):
		return round(time()-self.timer, 3)

	# events... examples right now, implement real events as needed
	def start(self):
		pass

	def end_turn(self):
		pass
	
	def place_ships(self):
		pass

	def loop(self):
		pass

class Event:
	
	def __init__(self, func, is_time_dependent):
		self.func = func
		self.is_time_dependent = is_time_dependent
		self.output = None
		
	def __call__(self, dt):
		if self.is_time_dependent:
			self.output = self.func(dt)
		else:
			self.output = self.func()
		return self.output

class Text:
		
	def __init__(self, string, pos, font_size, text_color, text_background=None):
		self.string = string
		self.pos = pos
		self.font_size = font_size
		self.text_color = text_color
		self.text_background = text_background

