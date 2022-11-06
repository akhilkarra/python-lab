# Python Class 2748
# Week 9
# Author: rt24-p (536532)

import typing
from math import floor
from statistics import mean


# Problem 2
def eight_letter_words(wordlist_path: str) -> int:
    """
    Returns the number of eight-letter words using the wordlist.txt file
    Args:
        :param wordlist_path: The file path of the wordlist.txt

    Raises:
        None.

    Returns:
        The number of eight-letter words in wordlist.txt
    """
    wordlist = open(wordlist_path, "r")  # Open wordlist.txt to read
    count = 0  # Create a counter for the number of eight-letter words

    for line in wordlist:  # For each line in the wordlist:
        if (
            len(line.strip("\n")) == 8
        ):  # Each line has one word, so if the length of line is 8:
            count += 1  # Increment the counter

    wordlist.close()  # Close wordlist.txt

    return count  # Return the number of eight-letter words in wordlist.txt


# Problem 3
def replace_word(filename: str, old_word: str, new_word: str) -> str:
    """
    Prints text in filename and replaces old_word with new_word

    Args:
        :param filename: The path for the file to print contents and replace words
        :param old_word: The word to find all occurrences in the file
        :param new_word: The word to replace all occurrences old_word

    Raises:
        None.

    Returns:
        None.
    """
    file = open(filename, "r")  # Open the file for reading
    new_contents = ""  # Create a variable for the new contents with the replaced lines

    for line in file:  # For each line in the reading file:
        words = line.split()  # Split the line up into individual words

        for i, word in enumerate(words):  # Given the index and word in the words list:
            if word == old_word:  # Check for old_word without punctuation:
                words[i] = new_word  # Replace old_word with new_word

        for punctuation in ",.!?/":  # Given all possible punctuation marks:
            for i, word in enumerate(
                words
            ):  # Given the index and word in the words list:
                if (
                    word == old_word + punctuation
                ):  # Check for old_word with punctuation
                    words[i] = new_word + punctuation  # Replace old_word with new_word

        new_contents += (
            " ".join(words) + "\n"
        )  # Join the list together put it in new_contents

    file.close()

    return new_contents  # Return the contents of the file


# Problem 4
def get_data(filename: str) -> typing.Tuple[int, int, int]:
    """
    Returns (# of lines,# of words,# of chars) in filename

    Args:
        :param filename: The path of the desired file

    Raises:
        None.

    Returns:
        A triple in the form (# of lines,# of words,# of chars)
    """
    lines = 0  # Create a lines counter
    words = 0  # Create a words counter
    chars = 0  # Create a characters counter

    file = open(filename, "r")  # Open the file for reading

    for line in file:  # For each line of the file
        lines += 1  # Increment the line counter
        words += len(
            line.split()
        )  # Count the number of words in the line and add it to words
        chars += len(line)  # Count the number of characters in the line

    file.close()  # Close the file

    return lines, words, chars  # Return the tuple of lines, words, chars


# Problem 5
def largest_4_product_grid(filename: str) -> int:
    """
    Returns the largest product of 4 consecutive numbers vertically or horizontally from a square
    grid of numbers stored in a file

    Args:
        :param filename:  The path of the file with the grid of numbers

    Raises:
        None.

    Returns:
        The largest product of 4 consecutive numbers horizontally or vertically
    """
    grid: typing.List[typing.List[int]] = []  # Create a nested list for the grid

    grid_file = open(filename, "r")  # Open the grid file to read

    for line in grid_file:  # For each line in the grid
        grid.append(
            list(map(int, line.split()))
        )  # Append the list of numbers in the line to grid

    grid_file.close()  # Close the grid file

    largest_product = 0  # Create a variable for the largest product

    for r in range(len(grid)):  # Check for greatest product horizontally
        for c in range(len(grid) - 4):
            if (
                grid[r][c] * grid[r][c + 1] * grid[r][c + 2] * grid[r][c + 3]
                > largest_product
            ):
                largest_product = (
                    grid[r][c] * grid[r][c + 1] * grid[r][c + 2] * grid[r][c + 3]
                )

    for c in range(len(grid)):  # Check for greatest product vertically
        for r in range(len(grid) - 4):
            if (
                grid[r][c] * grid[r + 1][c] * grid[r + 2][c] * grid[r + 3][c]
                > largest_product
            ):
                largest_product = (
                    grid[r][c] * grid[r + 1][c] * grid[r + 2][c] * grid[r + 3][c]
                )

    return largest_product  # Return the largest product found to the user


# Problem 7
def classscores(classgrades_path: str) -> None:
    """
    Read the data from this file and to write a new file classscores.txt such that each line of
    classscores.txt should consist of a student's last name followed by a single space and their
    average score on the assignments, rounded down to the nearest integer.

    Args:
        :param classgrades_path: The path of classgrades.txt

    Raises:
        None.

    Returns:
        None.
    """
    in_file = open(classgrades_path, "r")  # Open the classgrades.txt file for reading
    pupils_scores = [
        line.split() for line in in_file.readlines()
    ]  # Student scores lists
    in_file.close()  # Close classgrades.txt

    out_file = open("classscores.txt", "w")  # Create classscores.txt
    for (
        pupil
    ) in pupils_scores:  # Write out the average of each pupil's grades rounded down
        out_file.write(
            pupil[0] + " " + str(int(floor(mean(list(map(int, pupil[1:])))))) + "\n"
        )
    out_file.close()  # Close classscores.txt
