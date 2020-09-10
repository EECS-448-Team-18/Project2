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
	def __init__(self, pos, color_1, color_2):
		Render_Definition.__init__(self)
		self.render_type = "board"
		self.pos = pos
		self.color_1 = color_1
		self.color_2 = color_2
	
		self.grid = []
    
        #Creates a 2D array with 0s stored in each index
		for row in range(num_grids[0]):
			self.grid.append([])
			for column in range(num_grids[1]):
				self.grid[row].append(0)  

    #Wants to return if there is a ship in that position
	def get(self, x, y) -> int:
        #checks to see if the coordinates are valid
		if((x > num_grids[0] or x < 0) or (y > num_grids[1] or y < 0)):
			return False
		else:
            #Will return the value at that given coordinate
			for i in range(num_grids[0]):
				for j in range(num_grids[1]):
					if(i == x and j == y):
						return self.grid[i][j]
    
    #Changes the number in the grid to 1 in order represent that there is a ship on that positon of the board
	def set(self, x, y):
		if((x > num_grids[0] or x < 0) or (y > num_grids[1] or y < 0)):
            #checks to see if the coordinates are valid
			return(False)
		else:
            #Changes the value of the coordinates given
			for i in range(num_grids[0]):
				for j in range(num_grids[1]):
					if(i == x and j == y):
						self.grid[i][j] = 1

render_types = [Text, Rectangle, Circle, Image, Board]
	
