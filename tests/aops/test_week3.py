from aops.week3 import InvalidPositiveIntegerError, factorial
import pytest


@pytest.mark.parametrize(
    "n,expected",
    [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24)],
)
def test_factorial(n: int, expected: int) -> None:
    assert factorial(n) == expected


@pytest.mark.parametrize(
    "n",
    {(-1), (-100)},
)
def test_invalid_flip_4_digits(n: int) -> None:
    with pytest.raises(InvalidPositiveIntegerError):
        factorial(n)
