"""
/games/simon.py
"""

__authors__      = [("shineydev", "contact@shiney.dev")]
__maintainers__  = [("shineydev", "contact@shiney.dev")]

__version_info__ = (1, 0, 0, "stable", 0)
__version__      = ".".join([str(n) for n in __version_info__[:4:]])


import os
import random
import time

import colorama
import pyfiglet


COLORS = {
    "easy": [
        (colorama.Back.RED, "red"),
        (colorama.Back.GREEN, "green"),
        (colorama.Back.BLUE, "blue"),
        (colorama.Back.YELLOW, "yellow")
    ],
    "intermediate": [
        (colorama.Back.RED, "red"),
        (colorama.Back.GREEN, "green"),
        (colorama.Back.BLUE, "blue"),
        (colorama.Back.YELLOW, "yellow"),
        (colorama.Back.CYAN, "cyan")
    ],
    "hard": [
        (colorama.Back.GREEN, "green"),
        (colorama.Back.BLUE, "blue"),
        (colorama.Back.YELLOW, "yellow"),
        (colorama.Back.CYAN, "cyan"),
        (colorama.Back.MAGENTA, "magenta")
    ]
}

TIMES = {
    "easy": .5,
    "intermediate": .4,
    "hard": .3
}


class Simon():
    def __init__(self, difficulty : {"easy", "intermediate", "hard"}):
        """
        initializes a `Simon` object
        """

        self.colors = COLORS[difficulty]
        self.time = TIMES[difficulty]

    def game(self):
        """
        starts the game
        """

        colors = list()

        while (True):
            colors.append(random.choice(self.colors))

            for (color, color_name) in colors:
                os.system("cls")
                print("""
                ------------------
                |{0}                {1}|
                |{0}                {1}|
                |{0}                {1}|
                |{0}                {1}|
                |{0}                {1}|
                |{0}                {1}|
                |{0}                {1}|
                ------------------
                """.format(color, colorama.Back.RESET))

                time.sleep(self.time)
            
                os.system("cls")
                print("""
                ------------------
                |                |
                |                |
                |                |
                |                |
                |                |
                |                |
                |                |
                ------------------
                """)

                time.sleep(self.time)

            print()
            
            answer = input("> ").replace(" ", "")
            correct = "".join([color_name[0] for (color, color_name) in colors])

            if (answer != correct):
                break

        print()
        print("you got {0} correct combinations".format(len(colors) - 1))

    def start(self):
        """
        calls `self.game` in a 'would you like to play again?' loop
        """

        choice = "y"
        while (choice.startswith("y")):
            os.system("cls")
            print(pyfiglet.figlet_format("Simon Says"))
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

    game = Simon(difficulty)
    game.start()