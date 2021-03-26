# Python Class 2748
# Week 8
# Author: rt24-p (536532)

import random
import typing


class InvalidListLengthError(RuntimeError):
    """Error given if input lists are not the same length"""


class InvalidListError(RuntimeError):
    """Error given if input lists do not meet conditions required by the function"""


# Problem 1
def list_add(list1: typing.List[int], list2: typing.List[int]) -> typing.List[int]:
    """
    Returns a new list whose entries are the sum of the entries of list1 and list2

    Args:
        :param list1: An integer list with a set length l
        :param list2: An integer list also with set length l

    Raises:
        InvalidListLengthError: if the two input lists do not have the same length

    Returns:
        A new list whose entries are the sum of the entries of list1 and list2
    """
    if len(list1) != len(list2):  # If the two lists do not have the same length:
        print("The lists you have entered are not the same length. Please try again.")
        raise InvalidListLengthError()  # Raise the invalid list length error
    else:
        added_list: typing.List[int] = []  # Create a new integer for the added list

        for i in range(len(list1)):  # For each integer in the lists:
            added_list.append(list1[i] + list2[i])  # Add the corresponding numbers and insert them

        return added_list


# Problem 3a
def print_board(ttt_list: typing.List[str]) -> None:
    """
    Prints a tic-tac-toe board corresponding to tttList

    Args:
        :param ttt_list: A list showing what each of the 9 squares of the Tic Tac Toe board holds

    Raises:
        InvalidListError: if the list given is not a list of 9 elements

    Returns:
        None.
    """
    if len(ttt_list) != 9:
        raise InvalidListError  # Make sure the list is a string list of exactly 9 elements
    else:
        print(
            f"""
        {ttt_list[0]}|{ttt_list[1]}|{ttt_list[2]}
        -+-+-
        {ttt_list[3]}|{ttt_list[4]}|{ttt_list[5]}
        -+-+-
        {ttt_list[6]}|{ttt_list[7]}|{ttt_list[8]}
        """
        )  # Create the board


# Problem 3b
def find_winner(ttt_list: typing.List[str]) -> str:
    """
    Returns the winner (either 'X' or 'O') of the tic-tac-toe game represented by ttt_list, or 'No
    winner' if neither 'X' nor 'O' has won.

    Args:
        :param ttt_list: A list showing what each of the 9 squares of the Tic Tac Toe board holds

    Raises:
        InvalidListError: if the list given is not a list of 9 elements

    Returns:
        Either 'X', 'O', or 'No winner' based on tic-tac-toe rules
    """
    if len(ttt_list) != 9:
        raise InvalidListError  # Make sure the list has 9 elements
    else:
        for row in [0, 3, 6]:  # For each row
            if ttt_list[row] == ttt_list[row + 1] == ttt_list[row + 2]:  # Winner row?
                if ttt_list[row] == "X":  # If there are Xs across this row
                    return "X"  # X is the winner
                elif ttt_list[row] == "O":  # Otherwise
                    return "O"  # O is the winner

        for column in [0, 1, 2]:  # For each column
            if ttt_list[column] == ttt_list[column + 3] == ttt_list[column + 6]:  # Winner column?
                if ttt_list[column] == "X":  # If there are Xs across this column
                    return "X"  # X is the winner
                elif ttt_list[column] == "O":  # Otherwise
                    return "O"  # O is the winner

        if ttt_list[0] == ttt_list[4] == ttt_list[8]:  # Winner top-left to bottom-right diagonal?
            if ttt_list[0] == "X":  # If there are Xs across this diagonal
                return "X"  # X is the winner
            elif ttt_list[0] == "O":  # Otherwise
                return "O"  # O is the winner

        if ttt_list[2] == ttt_list[4] == ttt_list[6]:  # Winner top-right to bottom-left diagonal?
            if ttt_list[2] == "X":  # If there are Xs across this diagonal
                return "X"  # X is the winner
            elif ttt_list[2] == "O":  # Otherwise
                return "O"  # O is the winner

        return "No winner"  # If none of these conditions are met, then there are no winners


# Problem 4
def is_jolly(in_list: typing.List[int]) -> bool:
    """
     Returns True if the input argument is a jolly jumper sequence and False otherwise

    Args:
        :param in_list: The list that holds the possible jolly jumper sequence

    Raises:
        None.

    Returns:
        True if the items in the list correspond to a jolly jumper sequence, and False if not
    """
    absolute_differences = list(range(1, len(in_list)))  # All possible absolute differences

    for i in range(1, len(in_list)):  # For each element (starting at index 1):
        try:  # Find the absolute difference between elements, remove it from absolute_differences
            absolute_differences.remove(abs(in_list[i] - in_list[i - 1]))
        except ValueError:  # If this isn't possible:
            return False  # The entered list does not represent a jolly jumper sequence.

    return True  # If there were no errors raised, then this sequence must be a jolly jumper.


# Problem 6
def simulation_1000_dice_rolls() -> str:
    """
    Simulates rolling two 6-sided dice 1000 times, and keeps track of the frequency of each sum

    Args:
        None.

    Raises:
        None.

    Returns:
        A string with a frequency table of each possible roll
    """
    rolls = tuple[int]()  # Create a tuple for every single roll

    for i in range(1000):  # For 1000 times:
        dice1 = random.randint(1, 6)  # Roll the first dice
        dice2 = random.randint(1, 6)  # Roll the second dice

        rolls += (dice1 + dice2,)  # Add the sum of the rolls to the rolls tuple

    frequency_table = "Roll \tNumber \n---- \t------"  # Create the frequency table

    for roll in range(2, 13):  # For every possible roll:
        frequency_table += f"\n{roll} \t{rolls.count(roll)}"  # Row with the frequency

    return frequency_table  # Give the string back
