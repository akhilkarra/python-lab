# Python Class 2748
# Final Project
# Author: Akhil Karra

from time import sleep
from typing import Dict, Tuple


class ColumnFullError(RuntimeError):
    """Error generated if a given column in the board is full"""


# Function to gather player data --> DONE!
def get_player_data() -> Tuple[Tuple[str, str], Tuple[str, str]]:
    """
    Gets the names of the players playing Connect Four and whether they have the X
    checker or the O checker

    Args:
        None.

    Raises:
        None.

    Returns:
        A two-tuple of string two-tuples of the form (("X", player_x), ("O", player_o) such that
        player_x is a string with the name of the player with the X checker and player_o is a
        string with the name of the player with the O checker
    """
    player_x = input("Player X, please enter your name: ")  # Get the name of player X
    player_o = input("Player O, please enter your name: ")  # Get the name of player O

    return ("X", player_x), ("O", player_o)  # Give out the player data


# Function to create the Connect-4 board --> DONE!
def create_board() -> Dict[Tuple[int, int], str]:
    """
    Create a dictionary that corresponds to a Connect Four board

    Args:
        None.

    Raises:
        None.

    Returns:
        A 36-entry dictionary with each entry having a key (a,b) corresponding to the column (from
        left to right) and row (from the bottom up) of the space and a value "." denoting an empty
        space
    """
    board: Dict[Tuple[int, int], str] = {}  # Create the board dictionary

    for column in range(0, 7):  # For each column:
        for row in range(0, 7):  # And each row:
            board[(column, row)] = "."  # Create an empty space

    return board  # Give the empty board out


# Function to print a given Connect Four board dictionary --> DONE!
def print_board(board: Dict[Tuple[int, int], str]) -> None:
    """
    Print the given Connect Four board to the console.

    Args:
        board: A 36-entry dictionary with entries of the form {(a,b): "C"} corresponding to a
        Connect Four board

    Raises:
        None.

    Returns:
        None.

    """
    board_string = ""  # Create a string representing the board

    for column in range(0, 7):  # For each column number:
        board_string += str(column) + "  "  # Add the column numbers

    board_string += "\n"  # Add a new line

    for b in range(6, -1, -1):  # For each row from index 6 to 0 (top to bottom)
        for a in range(0, 7):  # For each column:
            board_string += board[(a, b)] + "  "  # Add the respective spot
        board_string += "\n"  # Add a new line

    print(board_string)  # Give the board string out


# Function to drop checkers and update board --> DONE!
def drop_checkers(
    board: Dict[Tuple[int, int], str], column: int, checker: str
) -> Dict[Tuple[int, int], str]:
    """
    Simulates dropping a checker in a Connect Four board
    Args:
        board: A 36-entry dictionary with entries of the form {(a,b): "C"} corresponding to a
        Connect Four board
        column: The column number to put the checker
        checker: The checker to place; either "X" or "O"

    Raises:
        ColumnFullError: Raised if the column specified is full

    Returns:
        The board dictionary with the checker placed in the designated column
    """
    row = 0  # Start on the bottommost row

    try:  # Try to:
        while board[(column, row)] != ".":
            row += 1  # Go up the rows while the space is not free
    except KeyError:  # If row exceeds 6:
        raise ColumnFullError  # The column must be full! Report it as so

    board[(column, row)] = checker  # Once the row is found, replace

    return board


# Function to check for horizontal four-in-a-rows
def check_horizontals(board: Dict[Tuple[int, int], str]) -> Tuple[bool, str]:
    """
    Checks for horizontal four-in-a-rows in a Connect Four board dictionary.

    Args:
        board: A 36-entry dictionary with entries of the form {(a,b): "C"} corresponding to a
        Connect Four board

    Raises:
        None.

    Returns:
        A tuple of a bool and a string, in the form (bool, "A"), where "A" represents the checker
        that lies four-in-a-row horizontally, i.e., the winning checker
    """
    for column in range(0, 4):  # For columns 0 through 3 inclusive:
        for row in range(0, 7):  # And for all rows:
            if (
                board[(column, row)]
                == board[(column + 1, row)]
                == board[(column + 2, row)]
                == board[(column + 3, row)]
            ):  # If there is a horizontal four-in-a-row:
                return True, board[(column, row)]  # Say so and give the winning checker

    return False, ""  # Otherwise, report False and give an empty string


# Function to check for vertical four-in-a-rows
def check_verticals(board: Dict[Tuple[int, int], str]) -> Tuple[bool, str]:
    """
    Checks for vertical four-in-a-rows in a Connect Four board dictionary.

    Args:
        board: A 36-entry dictionary with entries of the form {(a,b): "C"} corresponding to a
        Connect Four board

    Raises:
        None.

    Returns:
        A tuple of a bool and a string, in the form (bool, "A"), where "A" represents the checker
        that lies four-in-a-row vertically, i.e., the winning checker
    """
    for row in range(0, 4):  # For rows 0 through 3 inclusive:
        for column in range(0, 7):  # And for all columns:
            if (
                board[(column, row)]
                == board[(column, row + 1)]
                == board[(column, row + 2)]
                == board[(column, row + 3)]
            ):  # If there is a vertical four-in-a-row:
                return True, board[(column, row)]  # Say so and give the winning checker

    return False, ""  # Otherwise, report False and give an empty string


# Function to check for horizontal four-in-a-rows
def check_diagonals(board: Dict[Tuple[int, int], str]) -> Tuple[bool, str]:
    """


    Args:


    Raises:


    Returns:

    """
    return False, f"{str(board)}"


# Main Connect-4 function
def play_connect_four() -> None:
    """
    Plays a game of Connect-4 in a console.

    Args:
        None.

    Raises:
        None.

    Returns:
        None.
    """
    # SETUP
    print("Welcome to Connect Four!")  # Introduce the game
    sleep(3.0)  # Wait 3 seconds

    players = get_player_data()  # Learn names, which player has X, and which player has O
    current_player = players[0]  # Let the player with X go first
    winner = False  # Keep track of whether there is a winner or not
    ended = False  # Create a variable to show True if the game has ended and False if not

    board = create_board()  # Create the Connect Four board
    print_board(board)  # Print out the empty board
    sleep(3.0)  # Wait 3 seconds

    # MAIN GAME
    while not ended:  # While the game has not ended
        print(str(current_player[1]) + ", you're " + current_player[0])  # Remind player of checker
        sleep(2.0)  # Wait 2 seconds

        column = 7  # Initialize the variable to for which column to in which to put the checker

        while column not in range(0, 7):  # While the column number is invalid:
            try:  # Try to:
                column = int(input("What column do you want to play in? "))  # Get the column no.
                board = drop_checkers(board, column, current_player[0])  # Drop the checker
            except ValueError:  # If column is not a number:
                pass  # Ask for the column number again
            except ColumnFullError:  # If the specified column is full
                print("Sorry, that column is full!")  # Say so
                pass  # Ask for the column number again

        print_board(board)  # Give the board to the user
        sleep(3.0)  # Wait 3 seconds for some suspense!

        # If there is a four-in-a-row:
        if check_horizontals(board)[0] or check_verticals(board)[0] or check_diagonals(board)[0]:
            ended = True  # The game is over,
            winner = True  # And there is a winner!
        elif "." not in board.values():  # If there are no spaces available
            ended = True  # The game is over,
            winner = False  # But there is no winner!
        else:  # If there are no four-in-a-rows and there are still spaces to fill:
            if current_player == players[0]:  # If X's turn finished
                current_player = players[1]  # It is O's turn to play!
            else:  # Otherwise:
                current_player = players[0]  # It's X's turn to play!

    # WRAP UP
    if winner:  # If the current player won:
        print("Congratulations, " + current_player[1] + ", you won!")  # Congratulate
    else:  # If the game ended in a tie
        print("It's a tie! Well played " + players[0][1] + " and " + players[1][1] + "!")  # Say so

    print("Thank you for playing Connect Four!")  # Thank the users for playing


"""
# PLAY BUTTON
if __name__ == "__main__":
    play_connect_four()
"""
