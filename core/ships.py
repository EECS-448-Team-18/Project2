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

	def hide(self):
		self.hidden = True
		for ship in self.values():
			ship.hide()

	def show(self):
		self.hidden = False
		for ship in self.values():
			ship.show()

	def __add__(self, other):
		return list(self.values()) + list(other.values())

class Ship(pygame.sprite.Sprite):
	scale = 17

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

	def show(self):
		self.hidden = False

	def hide(self):
		self.hidden = True

	def move(self, pos):
		if self.unit_direction == (0, -1):
			self.pos = (pos[0], pos[1]-int((self.length-1)*self.image.get_height()/(self.length)))
		elif self.unit_direction == (1, 0):
			self.pos = (pos[0]-int((self.length-1)*self.image.get_width()/self.length), pos[1])
		else:
			self.pos = pos		
		self.rect.x = self.pos[0]
		self.rect.y = self.pos[1]

	def rotate(self):
		self.image = pygame.transform.rotate(self.image, -90)
		self.rect = self.image.get_rect(center=self.rect.center)
		
		self.unit_direction = (self.unit_direction[1], -self.unit_direction[0])
	
