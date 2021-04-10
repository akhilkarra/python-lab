# Python Class 2748
# Week 10
# Author: rt24-p (536532)

import typing


# Problem 2
def dict_reverse(input_dict: typing.Dict[str, int]) -> typing.Dict[int, str]:
    """
    Returns dict with keys/values of inputDict swapped

    Args:
        :param input_dict: Input dictionary

    Raises:
        None.

    Returns:
        The input dictionary with keys and values swapped
    """
    output_dict = {}  # Create an output dictionary

    for item in input_dict:  # For each item in the input dictionary:
        output_dict[input_dict[item]] = item  # Let value of input_dict = key of output_dict and VV

    return output_dict  # Return the output dictionary


# Problem 3
def student_averages(grades_txt_filepath: str) -> typing.Dict[str, float]:
    """
    Reads in the data from grades.txt, and then returns each student's name and average score.

    Args:
        :param grades_txt_filepath:  The path to grades.txt

    Raises:
        None.

    Returns:
        A dictionary with each student's name and their average score
    """
    tally: typing.Dict[str, list[float]] = {}  # Create dict to hold names, total, number of tests

    grades_file = open(grades_txt_filepath, "r")  # Open the grades.txt file to read

    for line in grades_file:  # For each line in the grades.txt file
        if line.split()[0] in tally:  # If the name already exists in the dictionary:
            tally[line.split()[0]][0] += int(line.split()[1])  # Add the new grade to the total
            tally[line.split()[0]][1] += 1  # Add a new test
        else:  # Otherwise:
            tally[line.split()[0]] = [int(line.split()[1]), 1]  # Create [total, number of tests]

    grades_file.close()  # Close the grades.txt file

    average_scores: typing.Dict[str, float] = {}  # Create the output dictionary

    for student in tally:  # For each student in the tally:
        average_scores[student] = tally[student][0] / tally[student][1]

    return average_scores  # Return the average scores string to the user


# Problem 4
def highest_scoring_scrabble_word(wordlist_path: str) -> str:
    """
    Finds the highest-scoring Scrabble word in wordlist.txt

    Args:
        :param wordlist_path: Path to wordlist.txt

    Raises:
        None.

    Returns:
        String of the word with the highest-scoring Scrabble word
    """
    highest_score: typing.Tuple[int, str] = (0, "")  # Create a tuple to store highest score & word
    values = {
        "A": 1,
        "B": 3,
        "C": 3,
        "D": 2,
        "E": 1,
        "F": 4,
        "G": 2,
        "H": 4,
        "I": 1,
        "J": 8,
        "K": 5,
        "L": 1,
        "M": 3,
        "N": 1,
        "O": 1,
        "P": 3,
        "Q": 10,
        "R": 1,
        "S": 1,
        "T": 1,
        "U": 1,
        "V": 4,
        "W": 4,
        "X": 8,
        "Y": 4,
        "Z": 10,
    }  # Scrabble values

    wordlist = open(wordlist_path, "r")  # Open wordlist.txt for reading

    for word in wordlist:  # For each word in wordlist.txt
        word = word.strip("\n")  # Strip \n
        score = 0  # Initialize the variable for the Scrabble score of the word

        for char in list(word.upper()):  # For each character in the uppercase word:
            score += values[char]  # Add the value of the character to the Scrabble score

        if score > highest_score[0]:  # If the current score is greater than the highest score:
            highest_score = (score, word)  # Make it the new highest score with the word itself

    wordlist.close()  # Close the wordlist file

    return highest_score[1]  # Return the highest scoring Scrabble word
