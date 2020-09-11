"""

"""

from data.elements import Board
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

    #Wants to return if there is a ship in that position
	def get(self, x, y) -> int:
        #checks to see if the coordinates are valid
		if((x > 9 and x < 0) or (y > 9 and y < 0)):
			return False
		else:
            #Will return the value at that given coordinate
			for i in range(num_grids[0]):
				for j in range(num_grids[1]):
					if(i == x and j == y):
						return self.grid[i][j]

    #Changes the number in the grid to value in order represent a specific
	#action or object within the grid position.
	#I.E
	#	A 0 represents Ocean
	#	A 1 represents A Ship tile
	#	A 2 represents A Missed Shot
	#	A 3 represents a Hit Shot
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
