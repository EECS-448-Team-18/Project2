"""
File name: peripherals.py
Authors: Grant Holmes, Luke Less'Ard-Springett, Fares Elattar, Peyton Doherty, Luke Beesley
Description: This file creates classes and functions which allow for the capture of
			 mouse and keyboard inputs.
Date: 09/13/2020

"""

import pygame

class Keys(dict):
	def __init__(self):
		dict.__init__(self)

	def init(self) -> None:
		self["w"] = lambda: pygame.key.get_pressed()[pygame.K_w]
		self["s"] = lambda: pygame.key.get_pressed()[pygame.K_s]
		self["a"] = lambda: pygame.key.get_pressed()[pygame.K_a]
		self["d"] = lambda: pygame.key.get_pressed()[pygame.K_d]
		self["space"] = lambda: pygame.key.get_pressed()[pygame.K_SPACE]

def get_left_click() -> bool:
	"""Postcondition: The function will return if the left click when pressed.
	   Precondition: The user has to click the the left click on the mouse.
	   Description: Meant to return if the left mouse click was pressed."""
	return pygame.mouse.get_pressed()[0]

def get_right_click() -> bool:
	"""Postcondition: The function will return if the right click when pressed.
	   Precondition: The user has to click the the right click on the mouse.
	   Description: Meant to return if the right mouse click was pressed."""
	return pygame.mouse.get_pressed()[2]

def get_mouse_pos() -> tuple:
	"""Postcondition: The function will return the position of the mouse.
	   Description: Meant to return if the right mouse click was pressed."""
	return pygame.mouse.get_pos()

def get_key(key) -> bool:
	"""Postcondition: Returns a key inside dictionary keys. If that fails, it will raise an exception.
	   Precondition: Key needs to exist in the dicitonary."""
	if key in keys:
	  return keys[key]()
	else:
	  raise ValueError("Peripheral key not available...")

def get_mouse() -> dict:
	"""
		Description: returns the where a mouse click has happened on the screen
	"""
	return {"left_click": get_left_click(), "right_click": get_right_click(), "pos": get_mouse_pos()}

keys = Keys()
