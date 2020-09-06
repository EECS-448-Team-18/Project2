"""
File name:
Authors:
Description:
Date:
Description:

Classes:
"""

import pygame

keys = {
    "up": False,
    "right": False,
    "down": False,
    "left": False,
    "space": False,
}


def getLeftClick():
    return pygame.mouse.get_pressed()[0]

def getRightClick():
    return pygame.mouse.get_pressed()[2]

def getMousePos():
    return pygame.mouse.get_pos()

def update_keys():
	keys["up"] = pygame.key.get_pressed()[pygame.K_w]
	keys["right"] = pygame.key.get_pressed()[pygame.K_d]
	keys["down"] = pygame.key.get_pressed()[pygame.K_s]
	keys["left"] = pygame.key.get_pressed()[pygame.K_a]
	keys["space"] = pygame.key.get_pressed()[pygame.K_SPACE]
	# can add more...
	
def getKey(key):
    update_keys()

    if key in keys:
        return keys[key]
    else:
        raise ValueError("Peripheral key not available...")

def get_mouse():
    return {"left_click": getLeftClick(), "right_click": getRightClick(), "pos": getMousePos()}
