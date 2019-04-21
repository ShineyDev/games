"""
/games/tictactoe.py

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

import pyfiglet


class Board():
    def __init__(self):
        """
        initializes a `Board` class derived from `object`
        """

        self.board = [" "] * 9

    def format(self) -> str:
        """
        returns `self.board` in a readable, printable format

        returns:
            board :: str :: the formatted board
        """

        board = """
         {0} | {1} | {2}
        -----------
         {3} | {4} | {5}
        -----------
         {6} | {7} | {8}
        """.format(*self.board)

        return board.strip("\n")

    def is_free(self, position : int) -> bool:
        """
        checks whether a `position` on `self.board` is free

        arguments:
            position :: int  :: the position to check

        returns:
                     :: bool :: whether a `position` on `self.board` is free
        """

        if (self.board[position - 1] == " "):
            return True
        return False

    def is_full(self) -> bool:
        """
        checks whether `self.board` is full

        returns:
            :: bool :: whether the `self.board` is full
        """

        if (" " in self.board):
            return False
        return True

    def print(self):
        """
        prints the return value of `self.format()` to sys.stdout
        """

        print(self.format())

    def reset(self):
        """
        resets `self.board`
        """

        self.board = [" "] * 9

    def set(self, position : int, symbol : str):
        """
        sets a `position` on `self.board` to `symbol`

        arguments:
            position :: int :: the `position` on `self.board` to set
            symbol   :: str :: the string to set the value at `position` as
        """

        self.board[position - 1] = symbol

class Player():
    def __init__(self, name : str, symbol : str, board : Board):
        """
        initializes a `Player` class derived from `object` with `name`, `symbol` and `board`
        """

        self.name = name
        self.symbol = symbol
        self.board = board

    def is_winner(self) -> bool:
        """
        checks whether `self` has won the game

        returns:
            :: bool :: whether `self` has won the game
        """

        if (self.board.board[0] == self.board.board[1] == self.board.board[2] == self.symbol):
            # won in first row
            return True
        elif (self.board.board[3] == self.board.board[4] == self.board.board[5] == self.symbol):
            # won in second row
            return True
        elif (self.board.board[6] == self.board.board[7] == self.board.board[8] == self.symbol):
            # won in third row
            return True
        elif (self.board.board[0] == self.board.board[3] == self.board.board[6] == self.symbol):
            # won in first column
            return True
        elif (self.board.board[1] == self.board.board[4] == self.board.board[7] == self.symbol):
            # won in second column
            return True
        elif (self.board.board[2] == self.board.board[5] == self.board.board[8] == self.symbol):
            # won in third column
            return True
        elif (self.board.board[0] == self.board.board[4] == self.board.board[8] == self.symbol):
            # won in left-right diagonal
            return True
        elif (self.board.board[2] == self.board.board[4] == self.board.board[6] == self.symbol):
            # won in right-left diagonal
            return True
        return False

class TicTacToe():
    def __init__(self):
        """
        initializes a `TicTacToe` class derived from `object`
        """

        pass

    def game(self):
        """
        starts the game
        """

        self.board = Board()
        self.player_one = Player("player one", "X", self.board)
        self.player_two = Player("player two", "O", self.board)

        self.current_player = self.player_one

        self.message = ""

        while ((not self.player_one.is_winner()) and (not self.player_two.is_winner()) and (not self.board.is_full())):
            os.system("cls")

            print()
            self.board.print()

            if (self.message):
                print()
                print(self.message)

                self.message = ""

            print()

            try:
                position = int(input("{0}, where would you like to place your {1}?\n> ".format(self.current_player.name, self.current_player.symbol)).strip())
            except (ValueError) as e:
                self.message = "position should be an integer in range 1 - 9"
                continue

            if (not position in range(1, 10)):
                self.message = "position should be an integer in range 1 - 9"
                continue
            
            if (not self.board.is_free(position)):
                self.message = "that space isn't empty!"
                continue

            self.board.set(position, self.current_player.symbol)

            # set `current_player` to the other player for the next turn :)
            if (self.current_player == self.player_one):
                self.current_player = self.player_two
            else:
                self.current_player = self.player_one

        os.system("cls")
        print()
        self.board.print()
        print()

        if (self.player_one.is_winner()):
            print("player one wins!")
        elif (self.player_two.is_winner()):
            print("player two wins!")
        else:
            # board filled -> tie
            print("it's a tie!")

    def start(self):
        """
        calls `self.game` in a 'would you like to play again?' loop
        """

        choice = "y"
        while (choice.startswith("y")):
            os.system("cls")
            print(pyfiglet.figlet_format("Tic Tac Toe"))
            print()
            input("enter to play\nctrl + c to quit to main menu\n\n")

            self.game()
            choice = input("\nwould you like to play again?\n> ").strip()

if (__name__ == "__main__"):
    game = TicTacToe()
    game.start()