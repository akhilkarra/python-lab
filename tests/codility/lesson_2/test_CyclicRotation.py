import pytest
from src.codility.lesson_2.CyclicRotation import solution


@pytest.mark.parametrize(
    "A, K, expected",
    [
        ([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]),
        ([0, 0, 0], 1, [0, 0, 0]),
        ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
    ],
)
def test_solution(A: [int], K: int, expected: [int]) -> None:
    assert solution(A, K) == expected
