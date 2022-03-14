import pytest
from src.codility.lesson_1.BinaryGap import solution


@pytest.mark.parametrize(
    "N, expected",
    {(9, 2), (529, 4), (1041, 5)},
)
def test_solution(N: int, expected: int) -> None:
    assert solution(N) == expected
