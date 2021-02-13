from aops.lib import InvalidNumberError, flip_4_digit
import pytest


@pytest.mark.parametrize(
    "n,expected",
    [(1728, 8271), (2400, 42), (2004, 4002), (1000, 1), (9999, 9999)],
)
def test_flip_4_digit(n: int, expected: int) -> None:
    assert flip_4_digit(n) == expected


@pytest.mark.parametrize(
    "n",
    {(-1), (-100), 10, 245, 95863},
)
def test_invalid_flip_4_digits(n: int) -> None:
    with pytest.raises(InvalidNumberError):
        flip_4_digit(n)
