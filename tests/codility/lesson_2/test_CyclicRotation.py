import pytest
from src.codility.lesson_2.CyclicRotation import solution


@pytest.mark.parametrize(
    "a, k, expected",
    [
        ([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]),
        ([0, 0, 0], 1, [0, 0, 0]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
    ],
)
def test_solution(a: list[int], k: int, expected: list[int]) -> None:
    assert solution(a, k) == expected
