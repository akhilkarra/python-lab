# Python Class 2748
# Final Project
# Author: Akhil Karra

from time import sleep


class ColumnFullError(RuntimeError):
    """Error generated if a given column in the board is full"""


# Function to gather player data --> DONE!
def get_player_data() -> tuple[tuple[str, str], tuple[str, str]]:
    """
    A function that gets the names of the players playing Connect Four and whether they have the X
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


# Function to create the Connect-4 board
def create_board() -> dict[tuple[int, int]: str]:
    """
    Create a dictionary that

    Args:


    Raises:


    Returns:

    """
    return {(0, 0): 1}


# Function to print a given Connect Four board dictionary
def print_board(board: dict[tuple[int, int]: str]):
    """


    Args:


    Raises:


    Returns:

    """
    print(board)


# Function to drop checkers and update board
def drop_checkers(
        board: dict[tuple[int, int]: str],
        column: int,
        checker: str
) -> dict[tuple[int, int]: str]:
    """


    Args:
        board:
        column:
        checker:

    Raises:
        InvalidColumnError:
        InvalidCheckerError:

    Returns:

    """
    board[(column, column)] = checker
    return board


# Function to check for horizontal four-in-a-rows
def check_horizontals(board: dict[tuple[int, int]: str]) -> tuple[bool, str]:
    """


    Args:


    Raises:


    Returns:

    """
    return False, f"{str(board)}"


# Function to check for vertical four-in-a-rows
def check_verticals(board: dict[tuple[int, int]: str]) -> tuple[bool, str]:
    """


    Args:


    Raises:


    Returns:

    """
    return False, f"{str(board)}"


# Function to check for horizontal four-in-a-rows
def check_diagonals(board: dict[tuple[int, int]: str]) -> tuple[bool, str]:
    """


    Args:


    Raises:


    Returns:

    """
    return False, f"{str(board)}"


# Main Connect-4 function
def play_connect_four():
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
                column = int(input("What column do you want to play in? "))  # Get the column no. &
                board = drop_checkers(board, column, current_player[0])  # Drop the checker
            except ValueError:  # If column is not a number:
                pass  # Ask for the column number again
            except ColumnFullError:  # If the specified column is full
                print("Sorry, that column is full!")
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


# PLAY BUTTON
if __name__ == '__main__':
    play_connect_four()
