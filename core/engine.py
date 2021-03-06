"""
File name: Engine.py
Authors: Grant Holmes, Luke Less'Ard-Springett, Fares Elattar, Peyton Doherty, Luke Beesley
Date: 09/13/2020
Description: Handles rendering and pygame specific game backend.
"""

import pygame
from data import assets
from data.assets import colors
from data import settings
from core import peripherals
from core.board import GameBoard
from data.elements import *

class Engine:
	"""
	Engine()

	Handles rendering and pygame specific game backend.
	"""

	def __init__(self):
		pygame.init()
		pygame.font.init()
		peripherals.keys.init()

		self.screen = pygame.display.set_mode(settings.screen_size)
		assets.image_cache.init()

		self.clock = pygame.time.Clock()

		self.background = self.make_background(settings.screen_size, assets.colors["black"])

		self.font_cache = {}
		self.surface_cache = {}

		self.running = True
		self.dt = None

		pygame.display.set_caption(settings.game_name)

	def make_background(self, size, color) -> pygame.Surface:
		"""
		Generates background of game window.
		"""
		#surface = pygame.Surface(size)
		#surface.fill(color)
		#return surface
		return assets.image_cache["background"]["image"]

	def get_dt(self) -> float:
		return self.dt

	def should_run(self) -> bool:
		"""
		Makes call to handle_events. Returns self.running.
		"""
		self.handle_events()

		# dt is milliseconds passed between frames, used to achieve frame rate independence
		self.dt = self.clock.tick(settings.target_frame_rate) / 1000 * settings.normalized_frame_rate

		return self.running

	def handle_events(self) -> None:
		"""
		Handles events from Pygame's event queue. pygame.QUIT occurs when "X" on top right
			corner is clicked.
		"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
				pygame.quit()

	def clear_screen(self) -> None:
		"""
		Removes everything blitted on screen by covering everything with background.
		"""
		self.screen.blit(self.background, (0, 0))

	def update_screen(self, objects_to_render, sprites) -> None:
		"""
		Renders necessary components to screen.
		"""
		self.render_objects(objects_to_render)
		# print(sprites)
		[self.screen.blit(sprite.image, sprite.rect) for sprite in sprites if (sprite.placed or sprite.selected) and not sprite.hidden]
		#self.display_fps()
		pygame.display.flip()

	def render_objects(self, objects_to_render) -> None:
		"""
		Renders objects to screen in appropriate manner.
		"""
		for obj in objects_to_render:
			if obj.render_type == "text":
				self.print_to_screen(obj.text, obj.pos, obj.font_size, obj.text_color, obj.text_background)
			elif obj.render_type == "rect":
				self.render_rect(obj.pos, obj.size, obj.fill_color, obj.alpha)
			elif obj.render_type == "circle":
				self.render_circle(obj.pos, obj.radius, obj.fill_color, obj.alpha)
			elif obj.render_type == "image":
				self.render_image(obj.image_name, obj.pos, obj.scale, obj.angle)
			elif obj.render_type == "board":
				self.render_board(obj.board, obj.pos, obj.color_1, obj.color_2)
			elif obj.render_type == "roundrect":
                                self.render_roundedRect(obj.pos, obj.size, obj.fill_color, obj.alpha)
                                
	def render_rect(self, pos, size, fill_color, alpha) -> None:
		"""
		Blits rect to screen. Alpha is opacity and ranges from 0-255.
		"""
		if size not in self.surface_cache:
			self.surface_cache[size] = pygame.Surface(size)

		surface = self.surface_cache[size]
		surface.set_alpha(alpha)
		surface.fill(fill_color)
		self.screen.blit(surface, pos)

	def render_board(self, board, pos, color_1, color_2) -> None:
		"""
			Description: Renders the board to the screen
			Parameters: board - A board object containing values of the ship locations
						pos - the position on which the board is rendered
						color_1 and color_2 are the default colors for the board where nothing resides in the tile
		"""
		rects = set()
		offset = 1
		for i in range(settings.num_grids[0]):
			for j in range(settings.num_grids[1]):
				if (board.get(i,j) == 2):
					rects.add(Rectangle((settings.grid_size[0]*j + pos[0], settings.grid_size[1]*i + pos[1]), settings.grid_size, colors["yellow"]))
				elif(board.get(i,j) == 3):
					rects.add(Rectangle((settings.grid_size[0]*j + pos[0], settings.grid_size[1]*i + pos[1]), settings.grid_size, colors["red"]))
				elif (offset % 2 == 0 and i%2 == 0) or (offset % 2 == 1 and i%2 == 1):
					rects.add(Rectangle((settings.grid_size[0]*j + pos[0], settings.grid_size[1]*i + pos[1]), settings.grid_size, colors["light_blue"]))
				else:
					rects.add(Rectangle((settings.grid_size[0]*j + pos[0], settings.grid_size[1]*i + pos[1]), settings.grid_size, colors["dark_blue"]))
				offset+=1
			offset-=1
		self.render_objects(rects)

	def render_circle(self, pos, radius, fill_color, alpha) -> None:
		"""
		Blits circle to screen. Alpha is opacity and ranges from 0-255.
		"""
		frame_size = (radius * 2, radius* 2)
		rel_x = radius
		rel_y = radius

		if frame_size not in self.surface_cache:
			self.surface_cache[frame_size] = pygame.Surface(frame_size)

		surface = self.surface_cache[frame_size]
		surface.fill(assets.colors["white"])
		surface.set_colorkey(assets.colors["white"])

		pygame.draw.circle(surface, fill_color, (rel_x, rel_y), radius)
		self.screen.blit(surface, pos)
	def render_roundedRect(self, pos, size, fill_color, alpha) -> None:
		"""
		Blits rounded rectangle to screen. Alpha is opacity and ranges from 0-255.
		"""
		rectangle = (pos, size)
		width, height = size
		x,y = pos
		rel_x =int(x)
		rel_y =int(height/2) +y
		radius = height/2
		pygame.draw.circle(self.screen, fill_color, (rel_x, rel_y), int (radius) )
		pygame.draw.rect(self.screen, fill_color, rectangle)
		rel_x = int(x)+width
		pygame.draw.circle(self.screen, fill_color, (rel_x, rel_y), int (radius) )

	def render_image(self, image_name, pos, scale, angle) -> None:
		"""
		Blits image to screen.
		"""
		image = assets.image_cache[image_name]["image"]
		if scale != 100:
			new_width = int(image.get_width()*scale/100)
			new_height = int(image.get_height()*scale/100)
			image = pygame.transform.scale(image, (new_width, new_height))
		if angle != 0:
			image = pygame.transform.rotate(image, angle)
		self.screen.blit(image, pos)

	def print_to_screen(self, text, pos, font_size, text_color, background_color=None) -> None:
		"""
		Blits text to screen. "background_color" is a colored rect behind text.
		"""
		if font_size not in self.font_cache:
			self.font_cache[font_size] = pygame.font.SysFont(settings.font_style, font_size)

		font = self.font_cache[font_size]
		padded_output = " " + text + " "

		if background_color is not None:
			text = font.render(padded_output, True, text_color, background_color)
		else:
			text = font.render(padded_output, True, text_color)

		text_rect = text.get_rect()
		text_rect.center = pos
		self.screen.blit(text, text_rect)

	def display_fps(self) -> None:
		"""
		displays current frames per second on screen, marker of performance
		"""
		fps = "FPS: " + str(int(self.clock.get_fps()))
		pos = (int((settings.screen_size[0]/1.25)), int(settings.screen_size[1]/10))
		self.print_to_screen(fps, pos, 36, assets.colors["red"], assets.colors["blue"])
