"""
File name:
Authors:
Description:
Date:
Description:

classes:
	Keys
"""

import pygame

class Keys(dict):
	"""
	Keys()

	Method:
		initialize() -> None
	"""
	def __init__(self):
		dict.__init__(self)

	def init(self) -> None:
		self["w"] = lambda: pygame.key.get_pressed()[pygame.K_w]
		self["s"] = lambda: pygame.key.get_pressed()[pygame.K_s]
		self["a"] = lambda: pygame.key.get_pressed()[pygame.K_a]
		self["d"] = lambda: pygame.key.get_pressed()[pygame.K_d]
		self["space"] = lambda: pygame.key.get_pressed()[pygame.K_SPACE]

def get_left_click() -> bool:
	return pygame.mouse.get_pressed()[0]

def get_right_click() -> bool:
	return pygame.mouse.get_pressed()[2]

def get_mouse_pos() -> tuple:
	return pygame.mouse.get_pos()
	
def get_key(key) -> bool:
	if key in keys:
	  return keys[key]()
	else:
	  raise ValueError("Peripheral key not available...")

def get_mouse() -> dict:
	return {"left_click": get_left_click(), "right_click": get_right_click(), "pos": get_mouse_pos()}

keys = Keys()

