"""
Game board stuff
"""
import pygame

class Board:

	def __init__(self):
        self.grid = []
        self.get_coordinates()
        self.place_and_set()
    
        #Creates a 2D array with 0s stored in each index
        for row in range(10):
            self.grid.append([])
            for column in range(10):
                self.grid[row].append(0)  

    #Wants to return if there is a ship in that position
    def get_coordinates(self, x, y)->grid position:
        #checks to see if the coordinates are valid
        if((x > 9 or x < 0) or (y > 9 or y < 0)):
            return (False)
        else:
            #Will return the value at that given coordinate
            for i in range(10):
                for j in range(10):
                    if(i == x and j == y):
                        return self.grid[i][j]
    
    #Changes the number in the grid to 1 in order represent that there is a ship on that positon of the board
    def place_and_set(self, x, y):
        if((x > 9 or x < 0) or (y > 9 or y < 0)):
            #checks to see if the coordinates are valid
            return(False)
        else:
            #Changes the value of the coordinates given
            for i in range(10):
                for j in range(10):
                    if(i == x and j == y):
                        self.grid[i][j] = 1
        
    
    

  


