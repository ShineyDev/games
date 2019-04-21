"""
/games/hangman.py

    Copyright (c) 2019 ShineyDev
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

__authors__           = [("shineydev", "contact@shiney.dev")]
__maintainers__       = [("shineydev", "contact@shiney.dev")]

__version_info__      = (1, 0, 0, "final", 0)
__version__           = "{0}.{1}.{2}{3}{4}".format(*[str(n)[0] if (i == 3) else str(n) for (i, n) in enumerate(__version_info__)])


import os
import random

import pyfiglet


HANGMAN = [
    """
\t-----
\t|   |
\t|
\t|
\t|
\t|
\t|
\t|
\t|
\t--------
    """,
    """
\t-----
\t|   |
\t|   0
\t|
\t|
\t|
\t|
\t|
\t|
\t--------
    """,
    """
\t-----
\t|   |
\t|   0
\t|  -+-
\t|
\t|
\t|
\t|
\t|
\t--------
    """,
    """
\t-----
\t|   |
\t|   0
\t| /-+-
\t|
\t|
\t|
\t|
\t|
\t--------
    """,
    """
\t-----
\t|   |
\t|   0
\t| /-+-\\
\t|
\t|
\t|
\t|
\t|
\t--------
    """,
    """
\t-----
\t|   |
\t|   0
\t| /-+-\\
\t|   |
\t|
\t|
\t|
\t|
\t--------
    """,
    """
\t-----
\t|   |
\t|   0
\t| /-+-\\
\t|   |
\t|   |
\t|
\t|
\t|
\t--------
    """,
    """
\t-----
\t|   |
\t|   0
\t| /-+-\\
\t|   |
\t|   |
\t|  |
\t|
\t|
\t--------
    """,
    """
\t-----
\t|   |
\t|   0
\t| /-+-\\
\t|   |
\t|   |
\t|  |
\t|  |
\t|
\t--------
    """,
    """
\t-----
\t|   |
\t|   0
\t| /-+-\\
\t|   |
\t|   |
\t|  | |
\t|  |
\t|
\t--------
    """,
    """
\t-----
\t|   |
\t|   0
\t| /-+-\\
\t|   |
\t|   |
\t|  | |
\t|  | |
\t|
\t--------
    """
]

try:
    # if this works then the file was run a as standalone
    with open("..\\utils\\hangman\\words.txt") as file_stream:
        WORDS = file_stream.read().split("\n")
except (FileNotFoundError) as e:
    # file was invoked by the launcher
    with open("utils\\hangman\\words.txt") as file_stream:
        WORDS = file_stream.read().split("\n")


class Hangman():
    def __init__(self):
        """
        initializes a `Hangman` object
        """

        pass

    def game(self):
        """
        starts the game
        """

        self.message = ""

        lives = 11

        word = [character.upper() for character in random.choice(WORDS)]
        word_hidden = ["_" for character in word]
        guessed = []

        while ((lives != 0) and ("_" in word_hidden)):
            os.system("cls")

            print(HANGMAN[-lives])
            print()

            if (guessed):
                print(" ".join(guessed))
                print()

            print("".join(word_hidden))
            print()

            if (self.message):
                print(self.message)
                print()

                self.message = ""
            else:
                print("you have {0} attempt{1} remaining".format(lives, "" if lives == 1 else "s"))
                print()

            letter = input("choose a letter;\n> ").upper()
            if (not letter):
                continue
            elif (not len(letter) == 1):
                self.message = "too many letters"
                continue
            elif (not letter.isalpha()):
                self.message = "that is not a letter"
                continue
            elif (letter in guessed):
                self.message = "you've already guessed that letter"
                continue

            guessed.append(letter)

            if (letter not in word):
                lives -= 1
                continue

            for (i) in range(len(word)):
                if (letter == word[i]):
                    word_hidden[i] = letter

        os.system("cls")

        print(HANGMAN[-lives])
        print()

        if (guessed):
            print(" ".join(guessed))
            print()

        print("".join(word_hidden))
        print()

        if (lives == 0):
            print("you lose")
            print("the word was {0}".format("".join(word)))
        else:
            print("you win")

    def start(self):
        """
        calls `self.game` in a 'would you like to play again?' loop
        """

        choice = "y"
        while (choice.startswith("y")):
            os.system("cls")
            print(pyfiglet.figlet_format("Hangman"))
            print()
            input("enter to play\nctrl + c to quit to main menu\n\n")

            self.game()
            choice = input("\nwould you like to play again?\n> ").strip()


if (__name__ == "__main__"):
    game = Hangman()
    game.start()