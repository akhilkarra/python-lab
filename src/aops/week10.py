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
    tally: typing.Dict[str, typing.List[float]] = {}  # Create dict to hold names, total, tests

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


# Problem 5
def count_letters(input_string: str) -> str:
    """
    Returns alphabetized letter count of letters in input_string, ignoring case

    Args:
        :param input_string: The string to analyze

    Raises:
        None.

    Returns:
        A string with each line giving a letter in input_string and its frequency in alphabetical
        order.
    """
    input_string = input_string.lower().replace(" ", "")  # Lowercase input, remove all spaces
    for punctuation in ".,;?!":  # For all punctuation marks:
        if punctuation in input_string:  # If the input string contains this punctuation mark:
            input_string = input_string.replace(punctuation, "")  # Delete all instances of it

    letters: typing.Dict[str, int] = {}  # Create a dictionary to hold a count of all letters
    letter_count = ""  # Create an empty string to hold the letter count in string form

    for letter in input_string:  # For letter in the processed input string
        if letter in letters:  # If the letter is already in the letters dictionary
            letters[letter] += 1  # Increment the counter for that letter
        else:  # Otherwise
            letters[letter] = 1  # Create a new entry in the dictionary with frequency 1

    letters_keys_list = list(letters.keys())  # Create a list of all the keys of letters
    letters_keys_list.sort()  # Sort this list in alphabetical order

    for letter in letters_keys_list:  # For each letter in the alphabetical list of letters' keys:
        letter_count += letter + ": " + str(letters[letter]) + "\n"  # Put the count in the string

    return letter_count  # Return the letter count string


# Problem 6
def replace_word(input_string: str, old_word: str, new_word: str) -> str:
    """
    Returns string such that old_word is replaced with new_word in input_string

    Args:
        :param input_string: The string to process
        :param old_word: The word to find all occurrences in the file
        :param new_word: The word to replace all occurrences old_word

    Raises:
        None.

    Returns:
        A string of all the text in input_string such that every instance of old_word is replaced
        with new_word
    """
    words = input_string.split()  # Split the input up into individual words

    for i, word in enumerate(words):  # Given the index and word in the words list:
        if word == old_word:  # Check for old_word without punctuation:
            words[i] = new_word  # Replace old_word with new_word

    for punctuation in ",.!?/":  # Given all possible punctuation marks:
        for i, word in enumerate(words):  # Given the index and word in the words list:
            if word == old_word + punctuation:  # Check for old_word with punctuation
                words[i] = new_word + punctuation  # Replace old_word with new_word

    return " ".join(words)  # Join the list of words together and return this


def translation_dictionary(dict_file_name: str, separator: str) -> typing.Dict[str, str]:
    """
    Reads a dictionary file and returns a dictionary containing the original word as the key and
    the translated word as the value. The dictionary file is made such that each line contains the
    original and translated words separated by the character specified as the separator

    Args:
        :param dict_file_name: The path to the dictionary file
        :param separator: The separator that separates the original and translated words in the
        dictionary file

    Raises:
        None.

    Returns:
        A dictionary such that the key is the original word
    """
    reference: typing.Dict[str, str] = {}  # Create a reference dictionary for translation

    dict_file = open(dict_file_name, "r")  # Open the dictionary file

    for line in dict_file:  # For each line in the dictionary file:
        words = line.strip("\n").split(separator)  # Split the line into a list of two words
        reference[words[0]] = words[1]  # Make an entry with {original: translation}

    dict_file.close()  # Close the dictionary file

    return reference  # Return the reference list


def translator(dict_file_name: str, text_file_name: str) -> str:
    """
    Changes words in input file according to the dictionary file and returns translation in a
    string

    Args:
        :param dict_file_name: The name of the dictionary file
        :param text_file_name: The name of the input text file

    Raises:
        None.

    Returns:
        A string containing the full translation of the input file
    """
    eng_to_pirate = translation_dictionary(dict_file_name, "|")  # Create a translation dictionary
    translation = ""  # Create a variable for the end translation in a string

    original_text = open(text_file_name, "r")  # Open the original text to read

    for line in original_text:  # For each line in the original text:
        for original in eng_to_pirate:  # For each of the original words in the dictionary:
            line = replace_word(line.lower(), original, eng_to_pirate[original])  # Translate!
        translation += line + "\n"  # Add it to the translation string

    original_text.close()  # Close the original text

    return translation.strip("\n")  # Return the translation as a string
