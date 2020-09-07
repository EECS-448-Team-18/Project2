"""
Game board stuff
"""
import pygame
import engine

class Board:

	def __init__(self):
        self.grid = []
        self.grid2 = []
        self.width = 50
	    self.height = 50
        self.spacing = 5
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
		self.create_grid()
        self.draw_grid()
        self.mouseclick()
    
    #This is building the 2-D array
    def create_grid(self):
        for row in range(9):
            self.grid.append([])
            for column in range(9):
                self.grid[row].append(0)  

        for row in range(9):
            self.grid2.append([])
            for column in range(9):
                self.grid2[row].append(0) 
    
    #This is drawing the grid
    def draw_grid(self):
        for row in range(9):
        for column in range(9):
            color = white
            if grid[row][column] == 1:
                color = green
            pygame.draw.rect(self.engine.screen, color, [ (self.spacing + self.width) * column + self.spacing,
                            (self.spacing + self.height) * row + self.spacing, self.width, self.height])

    def mouseclick(self):
        clock = pygame.time.Clock()
 
        #if the user doesnt quit then the while loop continues
        while self.engine.handle_events == false:
            #handle events function in engine.py
            event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x and y coordinates screen coordinates to grid coordinates
            column = pos[0] // (width + spacing)
            row = pos[1] // (height + spacing)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)


