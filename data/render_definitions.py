"""
File name:
Authors:
Description:
Date:
Description: Contains definitions for objects that contain necessary data to be rendered to screen.

Classes:
	Text
	Rectangle
"""

definition_types = set()

def init():
	definition_types.add(Text)
	definition_types.add(Rectangle)

class Render_Definition:
	
	def __init__(self):
		self.render_type = None

class Text(Render_Definition):
	"""
	Text(string, pos, font_size, text_color, text_background=None)

	Definition for string.
	"""
	def __init__(self, string, pos, font_size, text_color, text_background=None):
		Render_Definition.__init__(self)
		self.render_type = "text"
		self.text = string
		self.pos = pos
		self.font_size = font_size
		self.text_color = text_color
		self.text_background = text_background

class Rectangle(Render_Definition):
	"""
	Rectangle(pos, size, fill_color, alpha=255)
	
	Definition for Pygame Rect.
	"""
	def __init__(self, pos, size, fill_color, alpha=255):
		Render_Definition.__init__(self)
		self.render_type = "rect"
		self.pos = pos
		self.size = size
		self.fill_color = fill_color
		self.alpha = alpha
		
	
