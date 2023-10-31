from typing import Tuple

import pytest

from src.aops.week9 import (
    eight_letter_words,
    get_data,
    largest_4_product_grid,
    replace_word,
)


# Test eight_letter_words to find the numerical answer
@pytest.mark.parametrize(
    "wordlist_path, expected",
    {("src/tests/aops/test_files/wordlist.txt", 28416)},
)
def test_eight_letter_words(wordlist_path: str, expected: int) -> None:
    assert eight_letter_words(wordlist_path) == expected


# Test replace_word with given test case
@pytest.mark.parametrize(
    "filename, old_word, new_word, expected",
    {
        (
            "src/tests/aops/test_files/dorothy.txt",
            "Toto",
            "Gizmo",
            """It was Gizmo that made Dorothy laugh, and saved her from growing as gray as
her other surroundings. Gizmo was not gray; he was a little black dog, with
long silky hair and small black eyes that twinkled merrily on either side
of his funny, wee nose. Gizmo played all day long, and Dorothy played with
him, and loved him dearly.
""",
        )
    },
)
def test_replace_word(
    filename: str, old_word: str, new_word: str, expected: str
) -> None:
    assert replace_word(filename, old_word, new_word) == expected


# Test get_data with given test case
@pytest.mark.parametrize(
    "filename, expected",
    {("src/tests/aops/test_files/alice.txt", (4, 52, 262))},
)
def test_get_data(filename: str, expected: Tuple[int, int, int]) -> None:
    assert get_data(filename) == expected


# Test largest_4_product_grid using the grid file
@pytest.mark.parametrize(
    "filename, expected",
    {("src/tests/aops/test_files/projecteuler_grid.txt", 51267216)},
)
def test_largest_4_product_grid(filename: str, expected: int) -> None:
    assert largest_4_product_grid(filename) == expected
