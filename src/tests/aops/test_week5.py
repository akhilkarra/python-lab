import typing

import pytest

from src.aops.week5 import (
    InputOneError,
    InvalidNonnegativeIntegerError,
    InvalidPositiveIntegerError,
    InvalidTriangleError,
    OutOfBoundsError,
    assign_letter_grade,
    find_other_taxicab_number,
    find_three_digit_perfect_number,
    is_right_triangle,
    q1_1960_imo,
    sum_of_proper_divs,
)


# Test assign_letter_grade()
@pytest.mark.parametrize(
    "score, expected",
    {
        (98, "A+"),
        (95, "A"),
        (85, "B+"),
        (82, "B"),
        (78, "C+"),
        (70, "C"),
        (67, "D"),
        (51, "F"),
        (21, "I"),
        (0, "I"),
    },
)
def test_assign_letter_grade(score: int, expected: str) -> None:
    assert assign_letter_grade(score) == expected


# Test InvalidNonnegativeIntegerError associated with assign_letter_grade
@pytest.mark.parametrize("score", {-1, -12, -23, -923})
def test_alg_invalid_nonnegative_integer_error(score: int) -> None:
    with pytest.raises(InvalidNonnegativeIntegerError):
        assign_letter_grade(score)


# Test OutOfBoundsError associated with assign_letter_grade
@pytest.mark.parametrize("score", {101, 583, 9238})
def test_alg_out_of_bounds_error(score: int) -> None:
    with pytest.raises(OutOfBoundsError):
        assign_letter_grade(score)


# Test is_right_triangle()
@pytest.mark.parametrize(
    "a, b, c, expected",
    {
        (3, 4, 5, True),
        (4, 5, 3, True),
        (5, 4, 3, True),
        (5, 3, 4, True),
        (3, 11, 12, False),
        (11, 12, 3, False),
    },
)
def test_is_right_triangle(a: int, b: int, c: int, expected: bool) -> None:
    assert is_right_triangle(a, b, c) == expected


# Test InvalidTriangleError associated with is_right_triangle()
@pytest.mark.parametrize("a, b, c", {(3, 4, 45), (123, 2, 3), (2, 1234, 19)})
def test_irt_invalid_triangle_error(a: int, b: int, c: int) -> None:
    with pytest.raises(InvalidTriangleError):
        is_right_triangle(a, b, c)


# Test q1_1960_IMO()
@pytest.mark.parametrize("expected", [[550, 803]])
def test_q1_1960_imo(expected: typing.List[int]) -> None:
    assert q1_1960_imo() == expected


# Test sum_of_proper_divs()
@pytest.mark.parametrize("n, expected", {(12, 16), (6, 6), (28, 28)})
def test_sum_of_proper_divs(n: int, expected: int) -> None:
    assert sum_of_proper_divs(n) == expected


# Test InvalidPositiveIntegerError associated with sum_of_proper_divs()
@pytest.mark.parametrize("n", {0, -2, -53})
def test_sopd_invalid_positive_integer_error(n: int) -> None:
    with pytest.raises(InvalidPositiveIntegerError):
        sum_of_proper_divs(n)


# Test InputOneError associated with sum_of_proper_divs()
@pytest.mark.parametrize("n", {1})
def test_sopd_input_one_error(n: int) -> None:
    with pytest.raises(InputOneError):
        sum_of_proper_divs(n)


# Test find_three_digit_perfect_number()
@pytest.mark.parametrize("expected", {496})
def test_find_three_digit_perfect_number(expected: int) -> None:
    assert find_three_digit_perfect_number() == expected


# Test find_other_taxicab_number()
@pytest.mark.parametrize("expected", {4104})
def test_find_other_taxicab_number(expected: int) -> None:
    assert find_other_taxicab_number() == expected
