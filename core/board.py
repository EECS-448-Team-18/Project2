"""
Game board stuff
"""
import pygame

class Board:

	def __init__(self):
        self.grid = []
        self.grid2 = []
		self.create_grid()
    
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
    
    

  


