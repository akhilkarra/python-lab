import pytest
from src.aops.week4 import (
    InvalidNonnegativeIntegerError,
    OutOfBoundsError,
    convert_to_celsius,
    convert_to_fahrenheit,
    convert_to_seconds,
    letter_square,
)


# Test convert_to_seconds using test case in Problem 3 statement
@pytest.mark.parametrize(
    "hours, minutes,seconds, expected",
    [(2, 30, 15, 9015)],
)
def test_convert_to_seconds(hours: int, minutes: int, seconds: int, expected: int) -> None:
    assert convert_to_seconds(hours, minutes, seconds) == expected


# Test InvalidNonnegativeIntegerError in convert_to_seconds
@pytest.mark.parametrize(
    "hours, minutes, seconds",
    {(12, -2, 3), (-12, 3, 2), (13, 42, -3)},
)
def test_cts_invalid_nonnegative(hours: int, minutes: int, seconds: int) -> None:
    with pytest.raises(InvalidNonnegativeIntegerError):
        convert_to_seconds(hours, minutes, seconds)


# Test OutOfBoundsError in convert_to_seconds
@pytest.mark.parametrize(
    "hours, minutes, seconds",
    {(12, 300, 2), (59, 59, 61)},
)
def test_cts_out_of_bounds(hours: int, minutes: int, seconds: int) -> None:
    with pytest.raises(OutOfBoundsError):
        convert_to_seconds(hours, minutes, seconds)


# Test convert_to_celsius using common conversions for 32 degrees F and 212 degrees F
@pytest.mark.parametrize("fahrenheit, expected", {(32.0, 0.0), (212.0, 100.0)})
def test_convert_to_celsius(fahrenheit: float, expected: float) -> None:
    assert convert_to_celsius(fahrenheit) == expected


# Test convert_to_fahrenheit using common conversions for 0 degrees C and 100 degrees C
@pytest.mark.parametrize("celsius, expected", {(0.0, 32.0), (100.0, 212.0)})
def test_convert_to_fahrenheit(celsius: float, expected: float) -> None:
    assert convert_to_fahrenheit(celsius) == expected


# Test letter_square using test case in problem statement
@pytest.mark.parametrize(
    "letter, size, expected", {("x", 5, "xxxxx\nxxxxx\nxxxxx\nxxxxx\nxxxxx\n")}
)
def test_letter_square(letter: str, size: int, expected: str) -> None:
    assert letter_square(letter, size) == expected
