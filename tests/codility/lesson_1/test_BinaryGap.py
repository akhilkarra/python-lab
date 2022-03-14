import pytest
from src.codility.lesson_1.BinaryGap import solution


@pytest.mark.parametrize(
    "n, expected",
    {(9, 2), (529, 4), (1041, 5)},
)
def test_solution(n: int, expected: int) -> None:
    assert solution(n) == expected
