#!/usr/bin/env python3

"""
File name: __main__.py
Authors: Grant Holmes, Luke Less'Ard-Springett, Fares Elattar, Peyton Doherty, Luke Beesley
Description: Entrypoint to the game.
Date: 09/13/20
"""

import sys
from game import Game


def main(argv):
	game = Game()
	game.run()

if __name__ == "__main__":
	main(sys.argv)
	sys.exit()
