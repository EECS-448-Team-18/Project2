"""

"""
import pygame.sprite
import pygame.transform
from pygame import Surface, Rect
from math import sin, cos
from data import assets

class Fleet(dict):

	ship_types = {
				1: "patrol",
				2: "submarine",
				3: "cruiser",
				4: "battleship",
				5: "aircarrier",
			}

	def __init__(self):
		dict.__init__(self)
		self.hidden = False

	
	def add(self, ship):
		self[ship.length] = ship

	"""Description: The purpose of this function is to hide the ships during the game so that the oppsing 
	   player cannot see the other players ships while playing the game.
	   Postcondition: This function will call a helper function called show that makes the ship visible"""
	def hide(self):
		self.hidden = True
		for ship in self.values():
			ship.hide()

	"""Description: The puropse of this function is for the player to see their ships during the placing 
	   phase before the game starts.
	   Postcondition: This function will call a helper function called hide that makes the ship hidden"""
	def show(self):
		self.hidden = False
		for ship in self.values():
			ship.show()

	def __add__(self, other):
		return list(self.values()) + list(other.values())

class Ship(pygame.sprite.Sprite):
	scale = 17

	"""Description: This function deals with the ship sprite itself.
	   Postcondition: The user will have a ship sprite to interact with. 
	   Preconditon: This function takes in a length and ship type. The length is the size of the ship(1x1, 1x2, 1x3,
	   1x4, 1x5) and and the ship_type deals with what kind of ship sprite correlates with the length.  """
	def __init__(self, length, ship_type):
		pygame.sprite.Sprite.__init__(self)

		self.image = assets.image_cache[ship_type]["image"]

		new_width = int(self.image.get_width()*Ship.scale/100)
		new_height = int(self.image.get_height()*Ship.scale/100)

		self.image = pygame.transform.scale(self.image, (new_width, new_height))
		self.image = pygame.transform.rotate(self.image, -90)
		self.rect = self.image.get_rect()

		self.length = length

		self.pos = None
		self.grid_pos = None

		self.unit_direction = (0, 1)

		self.placed = False
		self.selected = False
		self.hidden = False

		self.destroyed = False
		self.health = self.length

	"""Description: This funciton is what makes the ship visible.
	   Postcodition: Will only return false. Returning false will make the ship visible on screen."""
	def show(self):
		self.hidden = False

	"""Description: This funciton is what makes the ship hidden.
	   Postcodition: Will only return true. Returning true will make the ship disappear on screen."""
	def hide(self):
		self.hidden = True

	"""Description: This function deals with moving the ship around with your mouse.
	   Precondition: This function will take in a positon. 
	   Postconditon: While this function doesn't return anything, it will allow user to move their
	   ship to the location that they want so they can later click and cement the location."""
	def move(self, pos):
		if self.unit_direction == (0, -1):
			self.pos = (pos[0], pos[1]-int((self.length-1)*self.image.get_height()/(self.length)))
		elif self.unit_direction == (1, 0):
			self.pos = (pos[0]-int((self.length-1)*self.image.get_width()/self.length), pos[1])
		else:
			self.pos = pos
		self.rect.x = self.pos[0]
		self.rect.y = self.pos[1]

	"""Descritption: This function allows the user to rotate their ship. 
	   Postcondition: The user will be able to rotate their ship by 90 degrees to their desired direction 
	   and later, will be able to set the ship in that position """
	def rotate(self):
		self.image = pygame.transform.rotate(self.image, -90)
		self.rect = self.image.get_rect(center=self.rect.center)

		self.unit_direction = (self.unit_direction[1], -self.unit_direction[0])
