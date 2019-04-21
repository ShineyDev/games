"""
/games/towers.py
"""

__authors__      = [("shineydev", "contact@shiney.dev")]
__maintainers__  = [("shineydev", "contact@shiney.dev")]

__version_info__ = (1, 0, 0, "stable", 0)
__version__      = ".".join([str(n) for n in __version_info__[:4:]])


import os

import colorama
import pyfiglet


HEIGHTS = {
    "easy": 3,
    "intermediate": 4,
    "hard": 5
}


class Towers():
    def __init__(self, difficulty : {"easy", "intermediate", "hard"}):
        """
        initializes a `Towers` object
        """

        self.tower_height = HEIGHTS[difficulty]

    def game(self):
        """
        starts the game
        """

        pass

    def start(self):
        """
        calls `self.game` in a 'would you like to play again?' loop
        """

        choice = "y"
        while (choice.startswith("y")):
            os.system("cls")
            print(pyfiglet.figlet_format("Towers"))
            print()
            input("enter to play\nctrl + c to quit to main menu\n\n")

            self.game()
            choice = input("\nwould you like to play again?\n> ").strip()
        

if (__name__ == "__main__"):
    difficulty = None
    while (difficulty not in {"easy", "intermediate", "hard"}):
        os.system("cls")
        print()
        difficulty = input("difficulty;\n> ").strip()

    game = Towers(difficulty)
    game.start()