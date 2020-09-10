"""
File name:
Authors:
Description:
Date:
Description: Contains definitions for objects that contain necessary data to be rendered to screen.

Classes:
	Text
	Rectangle
	Circle
	Image
	Board
"""

from data.settings import *

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
	
	Definition for rectangle.
	"""
	def __init__(self, pos, size, fill_color, alpha=255):
		Render_Definition.__init__(self)
		self.render_type = "rect"
		self.pos = pos
		self.size = size
		self.fill_color = fill_color
		self.alpha = alpha

	def is_clicked(self, pos):
		return (self.pos[0] <= pos[0] <= (self.pos[0] + self.size[0])) and (self.pos[1] <= pos[1] <= (self.pos[1] + self.size[1]))

class Circle(Render_Definition):
	"""
	Circle(pos, radius, fill_color, alpha=255)

	Definition for circle.
	"""
	def __init__(self, pos, radius, fill_color, alpha=255):
		Render_Definition.__init__(self)
		self.render_type = "circle"
		self.pos = pos
		self.radius = radius
		self.fill_color = fill_color
		self.alpha = alpha

class Image(Render_Definition):
	"""
	Image()

	Definition for image graphics.
	"""
	def __init__(self, image_name, pos, scale=100, angle=0):
		Render_Definition.__init__(self)
		self.render_type = "image"
		self.image_name = image_name
		self.pos = pos
		self.scale = scale
		self.angle = angle

class Board(Render_Definition):
	def __init__(self, board, pos, color_1, color_2):
		Render_Definition.__init__(self)
		self.render_type = "board"
		self.board = board
		self.pos = pos
		self.color_1 = color_1
		self.color_2 = color_2

render_types = [Text, Rectangle, Circle, Image, Board]
	
