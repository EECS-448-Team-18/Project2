"""
File name: board.py
Authors: Grant Holmes, Luke Less'Ard-Springett, Fares Elattar, Peyton Doherty, Luke Beesley
Description: This file creates a 9x9 array and functions to allow interactions with the array.
Date: 09/13/2020
"""

from data.settings import *

class GameBoard:

	def __init__(self):
		"""Definition: The purpose of this function is to create a list of lists, or 2D array, that is meat to hold values.
			   When the array is created, each cell is given a 0 to hold.
		   Postcondition: The purpose of creating this 2D array is for it to act as an abstract representaiton of the game board the user plays on.
			   Throughout the game, the boards values can and will be alterted to represent the different states of each square of the board
		"""
		self.grid = []
		self.coords = set()

		for row in range(num_grids[0]):
			for column in range(num_grids[1]):
				self.coords.add((row, column))

        #Creates a 2D array with 0s stored in each index
		for row in range(num_grids[0]):
			self.grid.append([])
			for column in range(num_grids[1]):
				self.grid[row].append(0)

	def get(self, x, y) -> int:
		"""
		Precondition: What must be true at the start of this function is that a value must be in the
		   the cell of the array
		Postcondition: This function will return one of two things. If the value of x and y are anything
		   greater than 9 or anything less than 0 it will return false. The other return will return the
		   value that is in the position of the 2d array. The value will be used to determine if the user
		   got a hit or a miss.
	    Parameters: The parameters this function takes in are the x and y values of the coordinate that
		   the user clicks on.
		"""
		if(not ((x > 9 and x < 0) or (y > 9 and y < 0))):
			for i in range(num_grids[0]):
				for j in range(num_grids[1]):
					if(i == x and j == y):
						return self.grid[i][j]

	def set(self, x, y,value):
		"""
        Precondition: What must be true at the start of the function is that the value being passed in
			   needs to be either a 0, 1, 2, or 3
		Postcondition: This function will change a value in the 2d array. It will change the value
				   either to a 0 for ocean, 1 for ship, 2 for hit, and 3 for miss.
		Parameters: the parameters this funciton takes is the x and y value of the coordinate the
				   user clicks on, as well as the value 0, 1, 2, or 3.
		"""
		if((x > num_grids[0] or x < 0) or (y > num_grids[1] or y < 0)):
            #checks to see if the coordinates are valid
			return(False)
		else:
            #Changes the value of the coordinates given
			for i in range(num_grids[0]):
				for j in range(num_grids[1]):
					if(i == x and j == y):
						self.grid[i][j] = value

	def __contains__(self, pt):
		"""
		Parameters: pt - Takes a location on the grid.
		Returns   : Returns if a ship hit point is on the given grid location
		"""
		return self.coords.__contains__(pt)

	def setBoard(self,test_board):
		"""
		Parameters: test_board - Takes a predefined 2d array which represents a board with
		Description:This method is used for testing the board without having to manually place down
					ships
		"""
		for row in range(num_grids[0]):
			for column in range(num_grids[1]):
				self.grid[row][column] = test_board[row][column]
