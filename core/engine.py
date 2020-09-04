"""
Handles GUI and Pygame specific stuff.
"""

import pygame
from data.assets import colors
from data import settings

class Engine:

	def __init__(self):
		pygame.init()
		pygame.font.init()

		self.running = True

		self.clock = pygame.time.Clock()
		
		self.screen = pygame.display.set_mode(settings.screen_size)
		self.background = self.make_background(settings.screen_size, colors["white"])
		
		self.font_cache= {}

		self.dt = None

		pygame.display.set_caption(settings.game_name)

	def make_background(self, size, color):
		surface = pygame.Surface(size)
		surface.fill(color)
		return surface

	def get_dt(self):
		return self.dt

	def keep_running(self):
		self.handle_events()

		# dt is milliseconds passed between frames
		self.dt = self.clock.tick(settings.target_frame_rate) / 1000 * settings.normalized_frame_rate

		return self.running
	
	def clear_screen(self):
		self.screen.blit(self.background, (0, 0))

	def update_text(self, text):
		x_0 = 300
		y_0 = 250
		x = x_0
		y = y_0
		dx = 50
		dy = 100
		
		for t in text:
			self.write_to_screen(t, (x, y), 48, colors["green"])
			x += dx			
			y += dy
	
	def update_screen(self, text):
		self.update_text(text)
		self.display_fps()
		pygame.display.flip()

	def handle_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False
				pygame.quit()

	def write_to_screen(self, output, pos, font_size, text_color, text_background=None):
		if font_size not in self.font_cache:
			self.font_cache[font_size] = pygame.font.SysFont(settings.font_style, font_size)

		font = self.font_cache[font_size]
		spaced_output = " " + output + " "

		if text_background is not None:
			text = font.render(spaced_output, True, text_color, text_background)
		else:
			text = font.render(spaced_output, True, text_color)

		text_rect = text.get_rect()
		text_rect.center = pos
		self.screen.blit(text, text_rect)
		
	def display_fps(self):
		"""displays current frames per second on screen, marker of performance"""
		fps = "FPS: " + str(int(self.clock.get_fps()))
		pos = (int((settings.screen_size[0]/1.25)), int(settings.screen_size[1]/10))
		self.write_to_screen(fps, pos, 36, colors["red"], colors["blue"])
		
