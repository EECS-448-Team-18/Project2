#!/usr/bin/env python3

"""
File name: __main__.py
Authors: Grant Holmes, Luke Less'Ard-Springett, Fares Elattar, Peyton Doherty, Luke Beesley
Maintainer: Abhigyan Saxena
Description: Entrypoint to the game and update the background effect.
Date: 10/4/20
"""

import sys
from pygame import mixer
from game import Game


#background sound
mixer.music.load('background.mp3')
mixer.music.play(-1)

def main(argv):
	game = Game()
	game.run()

if __name__ == "__main__":
	main(sys.argv)
	sys.exit()
