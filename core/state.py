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

# from core.board import Board
from core.peripherals import *  # checks for mouse and keyboard stuff
from data.assets import colors
from data.elements import *
from time import time
from data.settings import *

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
		# main game components
		# self.p1_board = Board()
		# self.p2_board = Board()

		self.render_queue = RenderQueue()

		self.events = {  # these events are all just examples, replace with actual events as needed
					"menu": Event(self.menu),
					"p1_place_ships": Event(self.p1_place_ships),
					"p2_place_ships": Event(self.p2_place_ships),
				}
		
		# game state attributes
		self.prev_event = None
		self.curr_event = "menu"

		self.timer = time()

		self.user_selection = 0

		# for rectangles
		

		

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
		if self.prev_event == "menu" and self.user_selection == 0:
			return "menu"
		if self.prev_event == "menu" and self.user_selection != 0:
			return "p1_place_ships"

		if self.prev_event == "p1_place_ships":
			return "p1_place_ships"
	
	def get_objects_to_render(self) -> tuple:
		return tuple(self.render_queue)

	def get_time_since_start(self) -> float:
		"""
		Returns time passed rounded to 3 decimals since game has started
		"""
		return round(time()-self.timer, 3)
	
	# helper functions...
	
	
		#pos = get_mouse()["pos"]
		#print((pos[0]//grid_size[0], pos[1]//grid_size[1]))
	
	# events... examples right now, implement real events as needed
	def menu(self):

		buttons = {
				1: {"rect": Rectangle((buttonx, buttony), (buttonWidth, buttonHeight), colors["blue"]),
						"text": Text("One Ship", (buttonx + 200, buttony +75), 50, colors["white"]) },
				2: {"rect": Rectangle((buttonWidth +400, buttony), (buttonWidth, buttonHeight), colors["blue"]),
						"text": Text("Two Ships", (buttonWidth + 600, buttony +75), 50, colors["white"]) },
				3:  {"rect": Rectangle((buttonx, buttonHeight+100), (buttonWidth, buttonHeight), colors["blue"]),
						"text": Text("Three Ships", (buttonx + 200,  buttonHeight +180), 50, colors["white"]) },
				4:  {"rect": Rectangle((buttonWidth +400,buttonHeight+100 ), (buttonWidth, buttonHeight), colors["blue"]),
						"text": Text("Four Ships", (buttonWidth + 600, buttonHeight +180), 50, colors["white"]) },
				5:  {"rect": Rectangle((550,2*buttonHeight+150 ), (buttonWidth, buttonHeight), colors["blue"], 255),
						"text": Text("Five Ships", (800, 2*buttonHeight +250), 50, colors["white"]) },
			}

		mouse_pos = get_mouse_pos()
		has_clicked = get_left_click()
		
		for button in buttons.values():
			for element in button.values():
				self.render_queue.add(element)      
		
		if has_clicked:
			for button in buttons:
				if buttons[button]["rect"].is_clicked(mouse_pos):
					self.user_selection = button
					break
	
	def p1_place_ships(self):
		self.render_queue.add(Board((300, 150), colors["light_blue"], colors["dark_blue"]))
	
	def p2_place_ships(self):
		self.render_queue.add(Board((300, 150), colors["light_blue"], colors["dark_blue"]))

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
		if type(render_object) in render_types:
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

