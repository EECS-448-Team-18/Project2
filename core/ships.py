"""

"""
from math import sin, cos

class Fleet(dict):

	ship_types = {
				(1, 1): "patrol",
				(1, 2): "submarine",
				(1, 3): "cruiser",
				(1, 4): "battleship",
				(1, 5): "aircarrier",
			}

	def __init__(self):
		dict.__init__(self)

	def add(self, ship_size):
		self[ship_size] = Ship(ship_size[1])

class Ship(dict):
	def __init__(self, length):
		dict.__init__(self)
		for i in range(length):
			self[i] = False

		self.origin = None
		self.normal_origin = None
		self.placed = False

		self.length = length
		self.orientation = (0, 1)

		self.destroyed = False
		self.health = self.length

	
