"""
File name: settings.py
Authors: Grant Holmes, Luke Less'Ard-Springett, Fares Elattar, Peyton Doherty, Luke Beesley
Description: Standard settings for the game.
Date: 09/13/20
"""

game_name = "Battleship"

screen_size = (1440, 900)
grid_size = (65, 65)
num_grids = (9, 9)

target_frame_rate = 60
normalized_frame_rate = 60
font_style = "impact"

button_size = (500, 200)
buttonHeight = 200
buttonWidth = 500
buttonx= 0.03*screen_size[0] #margin in the x direction
buttony = 50 #margin in the y direction

#A board is 585 pixels wide
#p1_board ends  at x: 665
p1_board_pos = (70, 200)
p2_board_pos = (785, 200)
