# Python Class 2748
# Week 7
# Author: rt24-p (536532)

import typing


class InvalidCharError(RuntimeError):
    """Error given if input is not a single character"""


# Function to make a list of non-space characters from a string
def string_to_non_space_characters(string: str) -> typing.List[str]:
    """
    Returns a list of non-space characters found in string

    Args:
        :param string: The input string from which to extract all characters

    Raises:
        None.

    Returns:
        A list of all characters in string not including spaces
    """
    words = string.lower().split()  # Make the string lowercase and split it into words
    words_split = [
        list(word) for word in words
    ]  # Split the words up into lists of letters
    return [
        char for word in words_split for char in word
    ]  # Flatten the list and return it


# Function to make a list of all characters from a string
def string_to_characters(string: str) -> typing.List[str]:
    """
    Returns a list of all characters found in string

    Args:
        :param string: The input string from which to extract all characters

    Raises:
        None.

    Returns:
        A list of all characters in string
    """
    words = list(string.lower())  # Make the string lowercase and split it into words
    words_split = [
        list(word) for word in words
    ]  # Split the words up into lists of letters
    return [
        char for word in words_split for char in word
    ]  # Flatten the list and return it


# Problem 2
def remove_letter(string: str, letter: str) -> str:
    """
    Returns the string given with all occurrences of the letter specified removed

    Args:
        :param string: The string to operate on
        :param letter: The letter to remove

    Raises:
        InvalidCharError: if the letter given is not a single character

    Returns:
        An integer of how many times the letter appears in the text.
    """
    if len(letter) != 1:
        raise InvalidCharError()  # Make sure that the letter given is truly a single character
    else:
        return string.replace(
            letter, ""
        )  # Replace the letter with nothing, i.e. delete it


# Problem 3
def make_acronym(string: str) -> str:
    """
    Returns an acronym for string consisting of the first letter of each word in string

    Args:
        :param string: The original string

    Raises:
        None.

    Returns:
        A string with the first letter of each word in string
    """
    words = string.split()  # Split the string into individual words
    acronym = ""  # An empty string to store the acronym

    for word in words:  # For each word
        acronym += word[0]  # Add the first letter of the word to the acronym string

    return acronym  # Give the acronym out


# Problem 4
def most_common_letter(string: str) -> str:
    """
    Returns the lowercase letter that's most common in string.

    Example:
        most_common_letter("This is a test of the function I have written") == "t"

    Args:
        :param string: The original string

    Raises:
        None.

    Returns:
        A string of the lowercase letter that occurs most commonly in string
    """
    letters = string_to_non_space_characters(
        string
    )  # Extract all characters from string
    common = max(
        letters, key=letters.count
    )  # Return the most common letter from all the letters
    return common


# Problem 5
def english_to_pig_latin(word: str) -> str:
    """
    Translates word into Pig Latin

    Args:
        :param word: The English word to translate into Pig Latin

    Raises:
        None.

    Returns:
        The Pig Latin translation as a string
    """
    if word[0] in "aeiou":  # check if the first letter is a vowel
        return word + "way"  # word begins with a consonant

    consonants = ""  # keep track of consonants at start of word

    while len(word) > 0 and word[0] not in "aeiou":
        consonants += word[0]  # add the consonant
        word = word[1:]  # remove the first letter from word

    if consonants[0].isupper():  # Preserve capitalization
        return (word + consonants + "ay")[0].upper() + (word + consonants + "ay")[
            1:
        ].lower()
    else:
        return word + consonants + "ay"


# Problem 6b
def rot13(input_str: str) -> str:
    """
    Returns the rot13-encoding of the input string.

    Example:
        rot13("Hello, World!") == "Uryyb, Jbeyq!"

    Args:
        :param input_str: The plaintext string to encode

    Raises:
        None.

    Returns:
        The ciphertext as a string per the rot13 cipher
    """
    chars = list(input_str)  # Create a list of all characters in the input string
    ciphertext = ""  # Create an empty string for the ciphertext

    for i in range(len(chars)):  # For each character:
        if 97 <= ord(chars[i]) <= 122:  # If the character is a lowercase letter:
            letter_order = (
                ord(chars[i]) - 97
            )  # ASCII code of the letters is now 0-25 inclusive

            rot13_letter_order = (
                letter_order + 13
            ) % 26  # Generate code for letter after rot13

            chars[i] = chr(rot13_letter_order + 97)  # Replace letter after rot13

        elif (
            65 <= ord(chars[i]) <= 90
        ):  # Else, if the character is an uppercase letter:
            letter_order = (
                ord(chars[i]) - 65
            )  # ASCII code of the letters is now 0-25 inclusive

            rot13_letter_order = (
                letter_order + 13
            ) % 26  # Generate code for letter after rot13

            chars[i] = chr(rot13_letter_order + 65)  # Replace letter after rot13

    for char in chars:  # For each encrypted character:
        ciphertext += char  # Add it to the cipher text

    return ciphertext  # Return the cipher text
