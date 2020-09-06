"""
File name: Engine.py
Authors:
Description:
Date:
Description: Handles rendering and pygame specific game backend.

Classes:
	Engine
"""

import pygame
from data.assets import colors
from data import settings

class Engine:
	"""
	Engine()

	Handles rendering and pygame specific game backend.
	
	Methods:
		make_background(size, color) -> pygame.Surface
		get_dt() -> float
		should_run() -> bool
		handle_events() -> None
		clear_screen() -> None
		update_screen(objects) -> None
		render_objects(objects_to_render) -> None
		print_to_screen(text, pos, font_size, text_color, background_color=None)
		display_fps() -> None
		"""

	def __init__(self):
		pygame.init()
		pygame.font.init()

		self.running = True

		self.clock = pygame.time.Clock()
		
		self.screen = pygame.display.set_mode(settings.screen_size)
		self.background = self.make_background(settings.screen_size, colors["white"])
		
		self.font_cache = {}
		self.surface_cache = {}

		self.dt = None

		pygame.display.set_caption(settings.game_name)

	def make_background(self, size, color) -> pygame.Surface:
		"""
		Generates background of game window.
		"""
		surface = pygame.Surface(size)
		surface.fill(color)
		return surface

	def get_dt(self) -> float:
		return self.dt

	def should_run(self) -> bool:
		"""
		Makes call to handle_events. Returns self.running.
		"""
		self.handle_events()

		# dt is milliseconds passed between frames, used to achieve 
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

	def update_screen(self, objects_to_render) -> None:
		"""
		Renders necessary components to screen. 
		"""
		self.render_objects(objects_to_render)
		self.display_fps()
		pygame.display.flip()

	def render_objects(self, objects_to_render) -> None:
		"""
		Renders objects to screen in appropriate manner.
		"""
		for obj in objects_to_render:
			if obj.render_type == "text":
				self.print_to_screen(obj.text, obj.pos, obj.font_size, obj.text_color, obj.text_background)

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
		self.print_to_screen(fps, pos, 36, colors["red"], colors["blue"])
		
