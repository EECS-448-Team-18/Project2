"""
File name:
Authors:
Description:
Date:
Description:
"""

import pygame

keys = {}

def init() -> None:
	global keys
	keys = {
		"w": lambda: pygame.key.get_pressed()[pygame.K_w],
		"s": lambda: pygame.key.get_pressed()[pygame.K_s],
		"a": lambda: pygame.key.get_pressed()[pygame.K_a],
		"d": lambda: pygame.key.get_pressed()[pygame.K_d],
		"space": lambda: pygame.key.get_pressed()[pygame.K_SPACE],
}

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
	return {"left_click": getLeftClick(), "right_click": getRightClick(), "pos": getMousePos()}
