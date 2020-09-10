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
		# main game components
		# self.p1_board = Board()
		# self.p2_board = Board()

		self.render_queue = RenderQueue()

		self.events = {  # these events are all just examples, replace with actual events as needed
					"example": Event(self.example),
					"menu" : Event(self.menu),
				}
		
		# game state attributes
		self.prev_event = None
		self.curr_event = "menu"

		self.user_selection = 0

		# for rectangles
		self.buttonHeight = 200
		self.buttonWidth = 500
		self.buttonx= 200 #margin in the x direction
		self.buttony = 50 #margin in the y direction

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
		if self.prev_event == "menu" and self.user_selection == 0:
			return "menu"
		if self.prev_event == "menu" and self.user_selection != 0:
			return "example"

		if self.prev_event == "example":
			return "example"
	
	def get_objects_to_render(self) -> tuple:
		return tuple(self.render_queue)

	def get_time_since_start(self) -> float:
		"""
		Returns time passed rounded to 3 decimals since game has started
		"""
		return round(time()-self.timer, 3)

	# events... examples right now, implement real events as needed
	def menu (self):
		mouseX,mouseY = pygame.mouse.get_pos()
                
		self.render_queue.add(Rectangle((self.buttonx,self.buttony ), (self.buttonWidth, self.buttonHeight), colors["blue"], 255))
		self.render_queue.add(Text("One Ship", (self.buttonx + 200, self.buttony +75), 50, (255, 255, 255)))
		option1 = pygame.Rect(self.buttonx,self.buttony,self.buttonWidth, self.buttonHeight)
		
		self.render_queue.add(Rectangle((self.buttonWidth +400,self.buttony ), (self.buttonWidth, self.buttonHeight), colors["blue"], 255))
		self.render_queue.add(Text("Two Ships", (self.buttonWidth + 600, self.buttony +75), 50, (255, 255, 255)))
		option2 = pygame.Rect(self.buttonWidth +400,self.buttony, self.buttonWidth, self.buttonHeight)
		
		self.render_queue.add(Rectangle((self.buttonx,self.buttonHeight+100 ), (self.buttonWidth, self.buttonHeight), colors["blue"], 255))
		self.render_queue.add(Text("Three Ships", (self.buttonx + 200,  self.buttonHeight +180), 50, (255, 255, 255)))
		option3 = pygame.Rect(self.buttonx,self.buttonHeight+100, self.buttonWidth, self.buttonHeight)
		
		self.render_queue.add(Rectangle((self.buttonWidth +400,self.buttonHeight+100 ), (self.buttonWidth, self.buttonHeight), colors["blue"], 255))
		self.render_queue.add(Text("Four Ships", (self.buttonWidth + 600, self.buttonHeight +180), 50, (255, 255, 255)))
		option4 = pygame.Rect(self.buttonWidth +400,self.buttonHeight+100 , self.buttonWidth, self.buttonHeight)
		
		self.render_queue.add(Rectangle((550,2*self.buttonHeight+150 ), (self.buttonWidth, self.buttonHeight), colors["blue"], 255))
		self.render_queue.add(Text("Five Ships", (800, 2*self.buttonHeight +250), 50, (255, 255, 255)))

		option5 = pygame.Rect(550,2*self.buttonHeight+150, self.buttonWidth, self.buttonHeight)

		if option1.collidepoint((mouseX,mouseY)):
			if get_left_click():
				self.user_selection =1
		if option2.collidepoint((mouseX,mouseY)):
			if get_left_click():
				self.user_selection =2
		if option3.collidepoint((mouseX,mouseY)):
			if get_left_click():
				self.user_selection =3
		if option4.collidepoint((mouseX,mouseY)):
			if get_left_click():
				self.user_selection =4
		if option5.collidepoint((mouseX,mouseY)):
			if get_left_click():
				self.user_selection =5

	def example(self):
		# these are random examples, delete and do acutal stuff
		space_pressed = get_key("space")
		if space_pressed:
			print("Space is pressed: "+str(self.get_time_since_start()))
		self.render_queue.add(Image("ship", (300, 300), 95, 45))
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

