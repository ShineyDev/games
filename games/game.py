"""
/game.py

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

__version_info__      = (1, 0, 0, "alpha", 0)
__version__           = "{0}.{1}.{2}{3}{4}".format(*[str(n)[0] if (i == 3) else str(n) for (i, n) in enumerate(__version_info__)])


import os
import subprocess
import sys

subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

import pyfiglet

from games import (
    connect,
    hangman,
    memory,
    minesweeper,
    simon,
    tictactoe,
    towers,
    uno
)


GAMES = [
    (connect.Connect,          "Connect 4",        None),
    (hangman.Hangman,          "Hangman",          None),
    (memory.Memory,            "Memory",           [("difficulty", {"easy", "intermediate", "hard"})]),
    (minesweeper.Minesweeper,  "Minesweeper",      [("difficulty", {"easy", "intermediate", "hard"})]),
    (simon.Simon,              "Simon Says",       [("difficulty", {"easy", "intermediate", "hard"})]),
    (tictactoe.TicTacToe,      "Tic Tac Toe",      None),
    (towers.Towers,            "Towers of Hanoi",  [("difficulty", {"easy", "intermediate", "hard"})]),
    (uno.Uno,                  "Uno",              [("players", int)])
]


def main_menu():
    os.system("cls")

    print(pyfiglet.figlet_format("Games"))
    print()
    print("[0] - Quit")
    print()

    for (i, (j, k, l)) in enumerate(GAMES, 1):
        print("[{0}] - {1}".format(i, k))
    
    print()

    choice = input("> ")

    try:
        choice = int(choice)
    except (ValueError) as e:
        return 1

    if (choice == 0):
        return 0
    elif (choice not in range(1, len(GAMES) + 1)):
        return 1

    try:
        arguments = []
        if (GAMES[choice - 1][2]):
            for (i, j) in GAMES[choice - 1][2]:
                argument = None

                if (isinstance(j, set)):
                    while (argument not in j):
                        os.system("cls")

                        print(pyfiglet.figlet_format("Games"))
                        print()
                        print("[0] - Quit")
                        print()

                        for (k, (l, m, n)) in enumerate(GAMES, 1):
                            print("[{0}] - {1}".format(k, m))
    
                        print()
                        print("> {0}".format(choice))
                        print()

                        argument = input("{} ({})\n> ".format(i, ", ".join(j))).strip()
                else:
                    while (not isinstance(argument, j)):
                        os.system("cls")

                        print(pyfiglet.figlet_format("Games"))
                        print()
                        print("[0] - Quit")
                        print()

                        for (k, (l, m, n)) in enumerate(GAMES, 1):
                            print("[{0}] - {1}".format(k, m))
    
                        print()
                        print("> {0}".format(choice))
                        print()

                        argument = input("{}\n> ".format(i)).strip()

                        try:
                            argument = j(argument)
                        except (Exception) as e:
                            pass

                arguments.append(argument)

        game = GAMES[choice - 1][0](*arguments)
        game.start()

        return 1
    except (KeyboardInterrupt) as e:
        return 1
    
    return 0


if (__name__ == "__main__"):
    i = 1
    while (i != 0):
        try:
            i = main_menu()
        except (KeyboardInterrupt) as e:
            i = 1