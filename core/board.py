"""

"""

from data.settings import *

class GameBoard:

	def __init__(self):
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
				
	"""Precondition: What must be true at the start of this function is that a value must be in the
	   the cell of the array
	   Postcondition: This function will return one of two things. If the value of x and y are anything
	   greater than 9 or anything less than 0 it will return false. The other return will return the
	   value that is in the position of the 2d array. The value will be used to determine if the user
	   got a hit or a miss.
	   Parameters: The parameters this function takes in are the x and y values of the coordinate that
	   the user clicks on."""
	def get(self, x, y) -> int:
		if((x > 9 and x < 0) or (y > 9 and y < 0)):
			return False
		else:
			for i in range(num_grids[0]):
				for j in range(num_grids[1]):
					if(i == x and j == y):
						return self.grid[i][j]

	"""Precondition: What must be true at the start of the function is that the value being passed in
	   needs to be either a 0, 1, 2, or 3
	   Postcondition: This function will change a value in the 2d array. It will change the value
	   either to a 0 for ocean, 1 for ship, 2 for hit, and 3 for miss.
	   Parameters: the parameters this funciton takes is the x and y value of the coordinate the 
	   user clicks on, as well as the value 0, 1, 2, or 3."""
	def set(self, x, y,value):
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
		return self.coords.__contains__(pt)

	def setBoard(self,testBoard):
			for row in range(num_grids[0]):
				for column in range(num_grids[1]):
					self.grid[row][column] = testBoard[row][column]
