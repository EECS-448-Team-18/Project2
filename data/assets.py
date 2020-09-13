"""
File name:
Authors:
Description:
Date:
Description: Visual and other aesthetic/ stylistic components such as colors and images.

Classes:
	ImageCache
"""

import pygame
import os

class ImageCache(dict):
	"""
	ImageCache()
	"""
	def __init__(self):
		dict.__init__(self)
		self["patrol"] = {"file_name": "patrolship.png", "image": None}
		self["cruiser"] = {"file_name": "cruiser.png", "image": None}
		self["battleship"] = {"file_name": "battleship.png", "image": None}
		self["submarine"] = {"file_name": "submarine.png", "image": None}
		self["aircarrier"] = {"file_name": "aircarrier.png", "image": None}
		
		self.resouce_path = os.path.join(os.getcwd(), "resources")

	def init(self) -> None:
		for image in self:
			self[image]["image"] = pygame.image.load(os.path.join(self.resouce_path, self[image]["file_name"]))
			self[image]["image"].convert_alpha()
		self["background"] = {"file_name": "background.png", "image": pygame.image.load(self.resouce_path+"/background.png").convert()}

colors = {
		"white": (255, 255, 255),
		"light_blue": (0, 188, 255),
		"dark_blue": (0, 146, 199),
		"red": (255, 0, 0),
		"green": (0, 255, 0),
		"blue": (0, 0, 255),
		"black": (0, 0, 0),
		"yellow": (255,255,0)
		}

image_cache = ImageCache()
