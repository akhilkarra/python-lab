# Python Class 2748
# Week 4
# Author: Akhil Karra


class InvalidNonnegativeIntegerError(RuntimeError):
    """Error generated if input given is not a nonnegative integer."""


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
        raise InvalidNonnegativeIntegerError  # Make sure the inputs are all nonnegative
    elif (minutes > 60) or (seconds > 60):
        raise OutOfBoundsError  # Make sure that minutes and seconds fit in expected bounds
    else:
        return (
            (hours * 3600) + (minutes * 60) + seconds
        )  # 3600 seconds = 1 hour, and 60 seconds = 1 minute


# Problem 4 Part 1
def convert_to_fahrenheit(celsius: float) -> float:
    """Convert a given Celsius temperature to Fahrenheit

    Args:


    Raises:
        None.

    Returns:
        The temperature in Fahrenheit
    """
    return 32 + ((9 * celsius) / 5)
