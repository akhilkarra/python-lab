import typing

import pytest
from src.aops.week8 import InvalidListLengthError, find_winner, is_jolly, list_add


# Test list_add with given case
@pytest.mark.parametrize("list1, list2, expected", [([1, 2, 3], [5, 8, 11], [6, 10, 14])])
def test_list_add(
    list1: typing.List[int], list2: typing.List[int], expected: typing.List[int]
) -> None:
    assert list_add(list1, list2) == expected


# Test InvalidListLengthError associated with list_add
@pytest.mark.parametrize("list1, list2", [([1, 2], [5, 8, 11])])
def test_la_invalid_list_length_error(list1: typing.List[int], list2: typing.List[int]) -> None:
    with pytest.raises(InvalidListLengthError):
        list_add(list1, list2)


# Test find_winner with variations of the given case in problem 3a
@pytest.mark.parametrize(
    "ttt_list, expected",
    [
        (["O", "O", "X", "O", "X", "X", "X", "O", "O"], "X"),
        (["X", "O", "X", "O", "X", "X", "O", "O", "O"], "O"),
        ([" ", "O", "X", " ", "X", "X", " ", "O", "O"], "No winner"),
    ],
)
def test_find_winner(ttt_list: typing.List[str], expected: str) -> None:
    assert find_winner(ttt_list) == expected


# Test is_jolly with given test cases
@pytest.mark.parametrize("in_list, expected", [([6, 9, 7, 8], True), ([1, 4, 3, 2], False)])
def test_is_jolly(in_list: typing.List[int], expected: bool) -> None:
    assert is_jolly(in_list) == expected
