#"""
#Game board stuff
#"""

#class Board:

	#def __init__(self):
		#pass

import pygame
 
#Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
 
#Height and Width of each square
width = 50
height = 50
 
#Spacing between each square
spacing = 5

# Creates a 2 dimensial array
grid = []
for row in range(9):
    grid.append([])
    for column in range(9):
        grid[row].append(0)  

grid2 = []
for row in range(9):
    grid2.append([])
    for column in range(9):
        grid2[row].append(0)
 
pygame.init()
 
# Setting the size of the screen
display = [1200, 600]
screen = pygame.display.set_mode(display)
 
# Setting the title
pygame.display.set_caption("Battleship Grid")
 
done = False
 
# Manages how fast the screen updates
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  # This will allow the user to exit
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (width + spacing)
            row = pos[1] // (height + spacing)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Makes the background black
    screen.fill(black)
 
    # Draws both grids
    for row in range(9):
        for column in range(9):
            color = white
            if grid[row][column] == 1:
                color = green
            pygame.draw.rect(screen,color,[ (spacing + width) * column + spacing,
                            (spacing + height) * row + spacing, width, height])
 
    # Limits to 60 FPS
    clock.tick(60)
 
    # Updates the screen
    pygame.display.flip()
 
pygame.quit()
