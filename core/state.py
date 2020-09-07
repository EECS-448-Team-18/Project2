"""
File name:
Authors:
Description:
Date:
Description: Tracks game state and implements game events. Handles game logic.

Classes:
	State
	RenderQueue
	Event
"""

from core.board import Board
from core import peripherals  # checks for mouse and keyboard stuff
from data.assets import colors
from data import render_definitions
from data.render_definitions import *
from time import time

class State:
	"""
	State()

	Tracks and manages state of game. Handles game logic.

	Methods:
		run_event(dt) -> None
		get_next_event() -> str
		get_objects_to_render(self) -> tuple
		get_time_since_start(self) -> float

		Events:
			
		
	"""

	def __init__(self):
		peripherals.init()
		render_definitions.init()

		# main game components
		self.p1_board = Board()
		self.p2_board = Board()

		self.render_queue = RenderQueue()

		self.events = {  # these events are all just examples, replace with actual events as needed
					"start": Event(self.start),
					"end_turn": Event(self.end_turn),
					"place_ships": Event(self.place_ships),
					"loop": Event(self.loop),
				}
		
		# game state attributes
		self.prev_event = None
		self.curr_event = "start"

		self.timer = time()

	def run_event(self, dt) -> None:
		"""
		Runs event from event dictionary. Updates event sequence.
		"""	
		self.render_queue.clear()
		self.events[self.curr_event](dt)
		self.prev_event = self.curr_event
		self.curr_event = self.get_next_event()

	def get_next_event(self) -> str:
		"""
		Conditionals determining game event logic. Decides next event based on previous event
			that has just been completed and any other necessary logic.
		"""
		if self.prev_event == "start":
			return "place_ships"

		if self.prev_event == "place_ships":
			return "end_turn"

		if self.prev_event == "end_turn":
			return "loop"

		if self.prev_event == "loop":
			return "loop"
	
	def get_objects_to_render(self) -> tuple:
		return tuple(self.render_queue)

	def get_time_since_start(self) -> float:
		"""
		Returns time passed rounded to 3 decimals since game has started
		"""
		return round(time()-self.timer, 3)

	# events... examples right now, implement real events as needed
	def start(self):
		pass

	def end_turn(self):
		pass
	
	def place_ships(self):
		pass

	def loop(self):
		# these are random examples, delete and do acutal stuff
		if self.curr_event == "loop" and int(self.get_time_since_start())%2==0:
			self.render_queue.add(Text("test_1", (100, 100), 36, colors["green"]))
			self.render_queue.add(Text("test_2", (200, 175), 30, (255, 0, 255)))
			self.render_queue.add(Rectangle((200, 200), (175, 25), colors["blue"], 200))
			self.render_queue.add(Circle((400, 50), 50, colors["red"]))

class RenderQueue(list):
	"""
	RenderQueue()
	
	Queue wrapper to store objects ready to be rendered to screen.

	Methods:
		add() -> None
	"""
	def __init__(self):
		list.__init__(self)

	def add(self, render_object) -> None:
		"""
		Makes sure render_object is correctly defined and can be rendered then adds to queue.
		"""
		if type(render_object) in render_definitions.definition_types:
			self.append(render_object)
		else:
			raise TypeError("Incorrectly wrapped...")

class Event:
	"""
	Event(func, is_time_dependent)

	Wrapper for function to be used as event.

	Methods:
		__call__(dt) -> None
	"""
	def __init__(self, func, is_time_dependent=False):
		self.func = func
		self.is_time_dependent = is_time_dependent
		self.output = None
		
	def __call__(self, dt) -> None:
		if self.is_time_dependent:
			self.output = self.func(dt)
		else:
			self.output = self.func()
		return self.output

