import pytest

from src.aops.week3 import (
    InvalidPositiveIntegerError,
    InvalidWholeNumberError,
    factorial,
    fibonacci,
)


# Test factorial function and corresponding runtime error.
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
def test_invalid_factorial(n: int) -> None:
    with pytest.raises(InvalidWholeNumberError):
        factorial(n)


# Test Fibonacci function and corresponding runtime error.
@pytest.mark.parametrize(
    "n,expected",
    [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5)],
)
def test_fibonacci(n: int, expected: int) -> None:
    assert fibonacci(n) == expected


@pytest.mark.parametrize(
    "n",
    {0, (-1), (-100)},
)
def test_invalid_fibonacci(n: int) -> None:
    with pytest.raises(InvalidPositiveIntegerError):
        fibonacci(n)
