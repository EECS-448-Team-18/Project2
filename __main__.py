#!/usr/bin/env python3

"""
This module is called to start overall program.
"""

import sys
from game import Game


def main(argv):
	game = Game()
	game.run()

if __name__ == "__main__":
	main(sys.argv)
	sys.exit()
