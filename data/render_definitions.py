"""
File name:
Authors:
Description:
Date:
Description:

Classes:
"""

class Text:
		
	def __init__(self, string, pos, font_size, text_color, text_background=None):
		self.render_type = "text"
		self.text = string
		self.pos = pos
		self.font_size = font_size
		self.text_color = text_color
		self.text_background = text_background
