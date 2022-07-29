import typing

from codility.OddOccurrences import solution
import pytest


@pytest.mark.parametrize(
    "a, expected",
    [([9, 3, 9, 3, 9, 7, 9], 7)],
)
def test_solution(a: typing.List[int], expected: int) -> None:
    assert solution(a) == expected
