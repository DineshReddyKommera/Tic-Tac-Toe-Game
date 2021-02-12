"""
    Tic Tac Toe game designed using python
    @Author Dinesh Reddy Kommera
"""

from enum import Enum


class TicTacToe:

    # States which defines the status of the game at each stage
    class STATES(Enum):
        CROSS_TURN = 0
        NAUGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4
        GAME_IS_ON = 5

    def __init__(self):
        # Game Board
        self.board = [["-", "-", "-"],
                      ["-", "-", "-"],
                      ["-", "-", "-"]]
        # boolean which checks for game continuation
        self.game_still_going = True;
        # Winner of the game
        self.winner = self.STATES.GAME_IS_ON
        # Current Player of the game(X or 0)
        self.current_player = self.STATES.CROSS_TURN

    # Displays the board
    def display_board(self):
        print(self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print(self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print(self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])

    # Play a game of tic tac toe
    def play_game(self):

        # Display initial board
        self.display_board()

        while self.game_still_going:
            # handle a single turn of a arbitary player
            self.handle_turn(self.current_player)

            # check if the game has ended
            self.check_if_game_over()

            # Flip to the other player
            self.flip_player()

        # The game has ended
        if self.winner == self.STATES.CROSS_WON or self.winner == self.STATES.NAUGHT_WON or self.winner == self.STATES.DRAW:
            print(self.winner.name)

    def handle_turn(self, player):
        if player == self.STATES.CROSS_TURN:
            print("X's turn.")
        if player == self.STATES.NAUGHT_TURN:
            print("0's turn.")
        position_row = input("Choose a position row from 1-3: ")
        position_column = input("Choose a position column from 1-3: ")

        valid = False
        while not valid:

            while position_row not in ["1", "2", "3"]:
                position_row = input("Choose a position row from 1-3: ")

            position_row = int(position_row) - 1

            while position_column not in ["1", "2", "3"]:
                position_column = input("Choose a position column from 1-3: ")

            position_column = int(position_column) - 1

            if self.board[position_row][position_column] != "-":
                print("You can't override existing choice")
            else:
                valid = True

        self.place_marker(player, position_row, position_column)
        self.display_board()

    # Marks value on the board
    def place_marker(self, symbol, row, column):
        if symbol == self.STATES.CROSS_TURN:
            self.board[row][column] = "X"
        else:
            self.board[row][column] = "0"

    # Determines whether is game is over or not
    def check_if_game_over(self):
        self.check_for_winner()
        self.check_if_tie()

    # Flips the player turn alternatively
    def flip_player(self):

        if self.current_player == self.STATES.CROSS_TURN:
            self.current_player = self.STATES.NAUGHT_TURN
        elif self.current_player == self.STATES.NAUGHT_TURN:
            self.current_player = self.STATES.CROSS_TURN
        return

    # Check for winner
    def check_for_winner(self):

        # check rows
        row_winner = self.check_rows()
        # check columns
        column_winner = self.check_columns()
        # check diagonals
        diagonal_winner = self.check_diagonals()

        if row_winner:
            self.winner = self.STATES.CROSS_WON if row_winner == "X" else self.STATES.NAUGHT_WON
        elif column_winner:
            self.winner = self.STATES.CROSS_WON if column_winner == "X" else self.STATES.NAUGHT_WON
        elif diagonal_winner:
            self.winner = self.STATES.CROSS_WON if diagonal_winner == "X" else self.STATES.NAUGHT_WON
        else:
            self.winner = self.STATES.GAME_IS_ON
        return

    # Determine whether rows are marked by single player
    def check_rows(self):

        row_1 = self.board[0][0] == self.board[0][1] == self.board[0][2] != "-"
        row_2 = self.board[1][0] == self.board[1][1] == self.board[1][2] != "-"
        row_3 = self.board[2][0] == self.board[2][1] == self.board[2][2] != "-"

        if row_1 or row_2 or row_3:
            self.game_still_going = False
        # Return the winner (X or 0)
        if row_1:
            return self.board[0][0]
        elif row_2:
            return self.board[1][0]
        elif row_3:
            return self.board[2][0]
        return

    # Determine whether columns are marked by single player
    def check_columns(self):

        column_1 = self.board[0][0] == self.board[1][0] == self.board[2][0] != "-"
        column_2 = self.board[0][1] == self.board[1][1] == self.board[2][1] != "-"
        column_3 = self.board[0][2] == self.board[1][2] == self.board[2][2] != "-"

        if column_1 or column_2 or column_3:
            self.game_still_going = False
        # Return the winner (X or 0)
        if column_1:
            return self.board[0][0]
        elif column_2:
            return self.board[0][1]
        elif column_3:
            return self.board[0][2]
        return

    # Determine whether diagonals are marked by single player
    def check_diagonals(self):

        diagonal_1 = self.board[0][0] == self.board[1][1] == self.board[2][2] != "-"
        diagonal_2 = self.board[0][2] == self.board[1][1] == self.board[2][0] != "-"

        if diagonal_1 or diagonal_2:
            self.game_still_going = False
        # Return the winner (X or 0)
        if diagonal_1:
            return self.board[0][0]
        elif diagonal_2:
            return self.board[0][2]
        return

    # Determine whether game lead to draw
    def check_if_tie(self):

        status = ["-" not in list for list in self.board]
        if status[0] and status[1] and status[2]:
            self.game_still_going = False
            self.winner = self.STATES.DRAW
            return


# Object Instance
t_game = TicTacToe()
# Start Game
t_game.play_game()
