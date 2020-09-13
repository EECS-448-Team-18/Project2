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

from core.board import GameBoard
from core.peripherals import *  # checks for mouse and keyboard stuff
from data.assets import colors
from data.elements import *
from core.ships import Fleet, Ship
from data import settings

class State:
	"""
	State()

	Tracks and manages state of game. Handles game logic.

	Methods:
		run_event(dt) -> None
		get_next_event() -> str
		get_objects_to_render() -> tuple
		get_sprites() -> list
		get_time_since_start() -> float

		Events:


	"""

	def __init__(self):
		# main game components
		self.p1_board = GameBoard()
		self.p2_board = GameBoard()

		self.render_queue = RenderQueue()

		self.events = {  # these events are all just examples, replace with actual events as needed
					"menu": Event(self.menu),
					"p1_place_ships": Event(self.p1_place_ships),
					"p2_place_ships": Event(self.p2_place_ships),
					"p1_turn": Event(self.p1_turn),
					"p2_turn": Event(self.p2_turn),
					"next_turn": Event(self.next_turn),
					"game_over": Event(self.end_game),
				}

		# game state attributes
		self.prev_event = None
		self.curr_event = "menu"

		self.left_click_ready = True
		self.right_click_ready = True

		# Event attributes
		self.user_selection = 0

		self.p1_fleet = Fleet()
		self.p2_fleet = Fleet()

		self.all_ships = [self.p1_fleet, self.p2_fleet]

		self.curr_ship = None

		self.p1_ship_counter = 1
		self.p2_ship_counter = 1

		self.p1_ships_placed = False
		self.p2_ships_placed = False

		self.p1_turn_over = False
		self.p2_turn_over = False
		self.turnReady = False

		self.p1_hit_points = 0
		self.p2_hit_points = 0

		self.game_over = False

		self.p1_won = False
		self.p2_won = False


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

		if self.prev_event == "p1_place_ships" and not self.p1_ships_placed:
			return "p1_place_ships"

		if self.prev_event == "p1_place_ships" and self.p1_ships_placed:
			return "p2_place_ships"

		if self.prev_event == "p2_place_ships" and not self.p2_ships_placed:
			return "p2_place_ships"

		if self.prev_event == "p2_place_ships" and self.p2_ships_placed:
			return "next_turn"

		if self.game_over:
			return "game_over"

		if self.prev_event == "p1_turn" and not self.p1_turn_over:
			return "p1_turn"

		if self.prev_event == "p1_turn" and self.p1_turn_over:
			return "next_turn"

		if self.prev_event == "next_turn" and self.p1_turn_over and self.turnReady:
			return "p2_turn"

		if self.prev_event == "next_turn" and self.p1_turn_over and not (self.turnReady):
			return "next_turn"

		if self.prev_event == "p2_turn" and not self.p2_turn_over:
			return "p2_turn"

		if self.prev_event == "p2_turn" and self.p2_turn_over:
			return "next_turn"

		if self.prev_event == "next_turn" and self.p2_turn_over and self.turnReady:
			return "p1_turn"

		if self.prev_event == "next_turn" and self.p2_turn_over and not (self.turnReady):
			return "next_turn"

	def get_objects_to_render(self) -> tuple:
		return tuple(self.render_queue)

	def get_sprites(self) -> list:
		# print(self.p1_fleet + self.p2_fleet)
		return self.p1_fleet + self.p2_fleet

# ----------------------Ship Placement Helper Functions------------------------#
	"""
	Parameters	:player_board - a defined board object
				 x - The x coordinate on the board
				 y - The y coordinate on the board
				 length - How long the ship to be checked is
				 direction which direction the ship is facing
	Description :This function checks the values that are on playerBoard to see
				 if a new ship can be assigned to the coordinates based off the
				 direction and length of the ship.
	Returns	    :This function returns a bool if a ship can be placed.
	"""
	def valid_position(self, player_board, x, y, length, direction) -> bool:
		if(direction == (0,1)):
			for i in range(length):
				if(player_board.get(x+i,y) == 1):
					return False
		elif(direction == (0,-1)):
			for i in range(length):
				if(player_board.get(x-i,y) == 1):
					return False
		elif(direction == (1,0)):
			for i in range(length):
				if(player_board.get(x,y-i) == 1):
					return False
		else:
			for i in range(length):
				if (player_board.get(x,y+i) == 1):
					return False
		return True

	"""
	Parameters	:board - A defined board object
				 curr_ship - A ship object to be placed
	Description :This function changes the values on board to reflect where the
				 current ship will be placed.
	"""
	def map_Ships(self,board, curr_ship):
		if(curr_ship.unit_direction == (0,1)):
			for i in range(curr_ship.length):
				board.set(curr_ship.grid_pos[1]+i,curr_ship.grid_pos[0],1)
		elif(curr_ship.unit_direction == (0,-1)):
			for i in range(curr_ship.length):
				board.set(curr_ship.grid_pos[1]-i,curr_ship.grid_pos[0],1)
		elif(curr_ship.unit_direction == (1,0)):
			for i in range(curr_ship.length):
				board.set(curr_ship.grid_pos[1],curr_ship.grid_pos[0]-i,1)
		else:
			for i in range(curr_ship.length):
				board.set(curr_ship.grid_pos[1],curr_ship.grid_pos[0]+i,1)
#------------------------------------------------------------------------------#
	def get_time_since_start(self) -> float:
		"""
		Returns time passed rounded to 3 decimals since game has started
		"""
		return round(time()-self.timer, 3)

	"""
		Description: This function handles the selection of how many ships the players
					 want to play with.
	"""
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
			if button["rect"].mouse_over(mouse_pos) and not has_clicked:
				button["rect"].fill_color = colors["light_blue"]
			elif button["rect"].mouse_over(mouse_pos):
				button["rect"].fill_color = colors["dark_blue"]
			else:
				button["rect"].fill_color = colors["blue"]
			for element in button.values():
				self.render_queue.add(element)

		if not has_clicked:
			if not self.left_click_ready:
				for button in buttons:
					if buttons[button]["rect"].mouse_over(mouse_pos):
						self.user_selection = button
						break
			self.left_click_ready = True
		else:
			self.left_click_ready = False

		if self.user_selection != 0:
			size_counter = 1
			for i in range(self.user_selection):
				for fleet in self.all_ships:
					fleet.add(Ship(size_counter, Fleet.ship_types[size_counter]))
				self.p1_hit_points += size_counter
				self.p2_hit_points += size_counter
				size_counter += 1
			self.left_click_ready = True

	"""
		Description: This function is responsible for having player 1 place their Ships
					 on their board. If a player tries to place a ship it is checked
					 if it is on the grid and does not collide with other ships.
		Helper Functions: valid_position and map_Ships
	"""
	def p1_place_ships(self):

		mouse_pos = get_mouse_pos()
		grid_pos = ((mouse_pos[0]-p1_board_pos[0])//grid_size[0], (mouse_pos[1]-p1_board_pos[1])//grid_size[1])
		normal_pos = (grid_pos[0]*grid_size[0] + p1_board_pos[0], grid_pos[1]*grid_size[1] + p1_board_pos[1])
		has_clicked = get_left_click()

		curr_ship = self.p1_fleet[self.p1_ship_counter]
		pos_valid = [(grid_pos[0] - (i*curr_ship.unit_direction[0]), grid_pos[1] + (i*curr_ship.unit_direction[1])) in self.p1_board for i in range(curr_ship.length)]
		ship_pos_valid = all(pos_valid)
		ship_pos_off_grid = not any(pos_valid)
		curr_ship.selected = True

		if not get_right_click():
			if not self.right_click_ready:
				curr_ship.rotate()
			self.right_click_ready = True
		else:
			self.right_click_ready = False

		self.render_queue.add(Image("grid",(5,135)))
		self.render_queue.add(Board(self.p1_board, p1_board_pos, colors["light_blue"], colors["dark_blue"]))
		self.render_queue.add(Text("Player 1's turn:", (700, 50), 40, colors["red"], colors["white"]))
		self.render_queue.add(Text("Num ships: " + str(self.user_selection), (1000, 300), 40, colors["red"], colors["white"]))
		curr_ship.move(normal_pos)
		curr_ship.grid_pos = grid_pos

		if ship_pos_off_grid:
			curr_ship.hide()
		else:
			curr_ship.show()

		if not has_clicked:
			if not self.left_click_ready:

				if ship_pos_valid and self.valid_position(self.p1_board, curr_ship.grid_pos[1], curr_ship.grid_pos[0], curr_ship.length, curr_ship.unit_direction):
					curr_ship.placed = True
					curr_ship.selected = False
					self.p1_ship_counter += 1
					self.left_click_ready = False

					self.map_Ships(self.p1_board,curr_ship)

					if self.p1_ship_counter > self.user_selection:
						self.p1_ships_placed = True
						self.p1_fleet.hide()
			self.left_click_ready = True
		else:
			self.left_click_ready = False


	"""
		Description: This function is responsible for having player 2 place their Ships
					 on their board. If a player tries to place a ship it is checked
					 if it is on the grid and does not collide with other ships.
		Helper Functions: valid_position and map_Ships
	"""
	def p2_place_ships(self):

		mouse_pos = get_mouse_pos()
		grid_pos = ((mouse_pos[0]-p2_board_pos[0])//grid_size[0], (mouse_pos[1]-p2_board_pos[1])//grid_size[1])
		normal_pos = (grid_pos[0]*grid_size[0] + p2_board_pos[0], grid_pos[1]*grid_size[1] + p2_board_pos[1])
		has_clicked = get_left_click()

		curr_ship = self.p2_fleet[self.p2_ship_counter]
		pos_valid = [(grid_pos[0] - (i*curr_ship.unit_direction[0]), grid_pos[1] + (i*curr_ship.unit_direction[1])) in self.p1_board for i in range(curr_ship.length)]
		ship_pos_valid = all(pos_valid)
		ship_pos_off_grid = not any(pos_valid)
		curr_ship.selected = True

		if not get_right_click():
			if not self.right_click_ready:
				curr_ship.rotate()
			self.right_click_ready = True
		else:
			self.right_click_ready = False

		self.render_queue.add(Image("grid",(720,135)))
		self.render_queue.add(Board(self.p2_board, p2_board_pos, colors["light_blue"], colors["dark_blue"]))
		self.render_queue.add(Text("Player 2's turn:", (700, 50), 40, colors["red"], colors["white"]))
		self.render_queue.add(Text("Num ships: " + str(self.user_selection), (1000, 300), 40, colors["red"], colors["white"]))
		curr_ship.move(normal_pos)
		curr_ship.grid_pos = grid_pos

		if ship_pos_off_grid:
			curr_ship.hide()
		else:
			curr_ship.show()
		if not has_clicked:
			if not self.left_click_ready:

				if ship_pos_valid and self.valid_position(self.p2_board, curr_ship.grid_pos[1], curr_ship.grid_pos[0], curr_ship.length, curr_ship.unit_direction):
					curr_ship.placed = True
					curr_ship.selected = False
					self.p2_ship_counter += 1
					self.left_click_ready = False

					self.map_Ships(self.p2_board,curr_ship)

					if self.p2_ship_counter > self.user_selection:
						self.p2_ships_placed = True
						self.p2_fleet.hide
						self.p2_turn_over = True
			self.left_click_ready = True
		else:
			self.left_click_ready = False

	"""
		Description: This function handles player 1's turn after both players have placed their ships
					 and allows them to click the other players board to make shots and then transitions
					 into the next event stage until a player wins.
	"""
	def p1_turn(self):
		self.p1_fleet.show()

		self.render_queue.add(Text("Player 1's turn:", (700, 50), 40, colors["red"], colors["white"]))

		self.render_queue.add(Image("grid",(5,135)))
		self.render_queue.add(Image("grid",(720,135)))
		self.render_queue.add(Board(self.p1_board, p1_board_pos, colors["light_blue"], colors["dark_blue"]))
		self.render_queue.add(Board(self.p2_board, p2_board_pos, colors["light_blue"], colors["dark_blue"]))

		mouse_pos = get_mouse_pos()
		has_clicked = get_left_click()

		if has_clicked:
			normal_pos = ((mouse_pos[1]-p2_board_pos[1])//grid_size[1], (mouse_pos[0]-p2_board_pos[0])//grid_size[0])
			if normal_pos in self.p2_board:
				grid_pos = (normal_pos[0]*grid_size[0] + p2_board_pos[0], normal_pos[1]*grid_size[1] + p2_board_pos[1])
				if(self.p2_board.get(normal_pos[0],normal_pos[1]) == 1):
					self.p2_board.set(normal_pos[0],normal_pos[1],3)
					self.p1_turn_over = True
					self.p2_turn_over = False
					self.p2_hit_points -=1
					self.p1_fleet.hide()
				elif(self.p2_board.get(normal_pos[0],normal_pos[1]) == 0):
					self.p2_board.set(normal_pos[0],normal_pos[1],2)
					self.p1_turn_over = True
					self.p2_turn_over = False
					self.p1_fleet.hide()
		if(self.p2_hit_points == 0):
			self.p1_won = True
			self.game_over = True
		self.turnReady = False

	"""
		Description: This function handles player 2's turn after both players have placed their ships
					 and allows them to click the other players board to make shots and then transitions
					 into the next event stage until a player wins.
	"""
	def p2_turn(self):
		self.p2_fleet.show()

		self.render_queue.add(Text("Player 2's turn:", (700, 50), 40, colors["red"], colors["white"]))

		self.render_queue.add(Image("grid",(5,135)))
		self.render_queue.add(Image("grid",(720,135)))
		self.render_queue.add(Board(self.p1_board, p1_board_pos, colors["light_blue"], colors["dark_blue"]))
		self.render_queue.add(Board(self.p2_board, p2_board_pos, colors["light_blue"], colors["dark_blue"]))

		mouse_pos = get_mouse_pos()
		has_clicked = get_left_click()

		if has_clicked:
			normal_pos = ((mouse_pos[1]-p1_board_pos[1])//grid_size[1], (mouse_pos[0]-p1_board_pos[0])//grid_size[0])
			if normal_pos in self.p1_board:
				grid_pos = (normal_pos[0]*grid_size[0] + p1_board_pos[0], normal_pos[1]*grid_size[1] + p1_board_pos[1])
				if(self.p1_board.get(normal_pos[0],normal_pos[1]) == 1):
					self.p1_board.set(normal_pos[0],normal_pos[1],3)
					self.p1_turn_over = False
					self.p2_turn_over = True
					self.p1_hit_points -=1
					self.p2_fleet.hide()
				elif (self.p1_board.get(normal_pos[0],normal_pos[1]) == 0):
					self.p1_board.set(normal_pos[0],normal_pos[1],2)
					self.p1_turn_over = False
					self.p2_turn_over = True
					self.p2_fleet.hide()
		if(self.p1_hit_points == 0):
			self.p2_won = True
			self.game_over = True
		self.turnReady = False

	"""
		Description: This function handles the end of either players turn to allow
					 for a change of player without revealing the other players ship
					 locations.
	"""
	def next_turn(self):
		self.p1_fleet.hide()
		self.p2_fleet.hide()

		mouse_pos = get_mouse_pos()
		has_clicked = get_left_click()

		self.render_queue.add(Image("grid",(5,135)))
		self.render_queue.add(Image("grid",(720,135)))
		self.render_queue.add(Board(self.p1_board, p1_board_pos, colors["light_blue"], colors["dark_blue"]))
		self.render_queue.add(Board(self.p2_board, p2_board_pos, colors["light_blue"], colors["dark_blue"]))

		next_turn_button = Rectangle((615,800), (200, 75), colors["blue"])
		self.render_queue.add(next_turn_button)
		self.render_queue.add(Text("Next Players Turn", (715, 835), 20, colors["red"], colors["white"]))

		if not has_clicked:
			if not self.left_click_ready:
				if next_turn_button.mouse_over(mouse_pos):
					self.turnReady = True
			self.left_click_ready = True
		else:
			self.left_click_ready = False

	"""
		Description: This function Declares a winner for the current game state.
	"""
	def end_game(self):
		if(self.p1_won):
			self.render_queue.add(Text("Player 1 Has Won", (700, 50), 40, colors["red"], colors["white"]))
		else:
			self.render_queue.add(Text("Player 2 Has Won", (700, 50), 40, colors["red"], colors["white"]))

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
