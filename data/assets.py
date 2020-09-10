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
		self["ship"] = {"file_name": "battleship.png", "image": None}
		self.resouce_path = os.path.join(os.getcwd(), "resources")

	def init(self) -> None:
		for image in self:
			self[image]["image"] = pygame.image.load(os.path.join(self.resouce_path, self[image]["file_name"]))
			self[image]["image"].convert_alpha()

colors = {
		"white": (255, 255, 255),
		"light": (0, 188, 255),
		"dark": (0, 146, 199),
		"red": (255, 0, 0),
		"green": (0, 255, 0),
		"blue": (0, 0, 255),
		"black": (0, 0, 0),
		}

image_cache = ImageCache()
