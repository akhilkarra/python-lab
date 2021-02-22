import pytest
from src.aops.week4 import InvalidNonnegativeIntegerError, OutOfBoundsError, convert_to_seconds


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
def test_cts_outofbounds(hours: int, minutes: int, seconds: int) -> None:
    with pytest.raises(OutOfBoundsError):
        convert_to_seconds(hours, minutes, seconds)
