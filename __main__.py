#!/usr/bin/env python3

"""
File name: __main__.py
Authors:
Description:
Date:
Description: Entrypoint to game
"""

import sys
from game import Game


def main(argv):
	game = Game()
	game.run()

if __name__ == "__main__":
	main(sys.argv)
	sys.exit()
