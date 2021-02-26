# Python Class 2748
# Week 4
# Author: Akhil Karra


class InvalidNonnegativeIntegerError(RuntimeError):
    """Error generated if input given is not a nonnegative integer."""


class InvalidPositiveIntegerError(RuntimeError):
    """Error generated if input given is not a positive integer."""


class OutOfBoundsError(RuntimeError):
    """Error generated if input given is out of bounds of what is expected"""


# Problem 3
def convert_to_seconds(hours: int, minutes: int, seconds: int) -> int:
    """Find the number of seconds in a time interval given hours, minutes, and seconds of that interval

    Args:
        :param seconds: a nonnegative integer between 0 and 60 inclusive
        :param minutes: a nonnegative integer between 0 and 60 inclusive
        :param hours: a nonnegative integer

    Raises:
        InvalidNonnegativeIntegerError: If input given is not a nonnegative integer.
        OutOfBoundsError: If minutes or seconds given is greater than 60

    Returns:
        The number of seconds of the specified time interval.
    """
    if (hours < 0) or (minutes < 0) or (seconds < 0):
        raise InvalidNonnegativeIntegerError(
            "Inputs are less than 0."
        )  # Make sure the inputs are all nonnegative
    elif (minutes > 60) or (seconds > 60):
        raise OutOfBoundsError("Inputs are out of bounds.")  # Make sure that inputs make sense
    else:
        return (hours * 3600) + (minutes * 60) + seconds  # 3600s = 1hr , and 60s = 1min


# Problem 4 Part 1
def convert_to_fahrenheit(celsius: float) -> float:
    """Convert a given Celsius temperature to Fahrenheit

    Args:
        The temperature in Celsius

    Raises:
        None.

    Returns:
        The temperature in Fahrenheit
    """
    return 32 + ((9 * celsius) / 5)


# Problem 4 Part 2
def convert_to_celsius(fahrenheit: float) -> float:
    """Convert a given Fahrenheit temperature to Celsius

    Args:
        The temperature in Fahrenheit

    Raises:
        None.

    Returns:
        The temperature in Celsius
    """
    return 5 / 9 * (fahrenheit - 32)


# Problem 6
def letter_square(letter: str, size: int) -> str:
    """Create square of a specified character

    Args:

        :param letter: the character to fill the square with
        :param size: the side length of the letter square

    Raises:
        InvalidPositiveIntegerError: if the size given is not a positive integer

    Returns:
        :rtype: str
        A string that, when printed, results in a size-by-size square of the character
    """
    if size <= 0:
        raise InvalidPositiveIntegerError(
            f"size is less than or equal to 0. {size}"
        )  # Make sure size makes sense
    else:
        square = ""  # Create a variable for the square, which is just an empty string

        for row in range(0, size):  # For each row:
            square += size * letter + "\n"  # Create the line of letters and add a new line

        return square  # Return the completed square string
