import pytest
from src.aops.week7 import (
    InvalidCharError,
    english_to_pig_latin,
    make_acronym,
    most_common_letter,
    remove_letter,
    rot13,
)


# Test remove_letter with given cases
@pytest.mark.parametrize(
    "string, letter, expected",
    {
        ("This is a test", "t", "This is a es"),
        ("Hello World!", "l", "Heo Word!"),
        ("I like Python", "q", "I like Python"),
    },
)
def test_remove_letter(string: str, letter: str, expected: str) -> None:
    assert remove_letter(string, letter) == expected


# Test InvalidCharError associated with remove_letter
@pytest.mark.parametrize("string, letter", {("asides", "sef"), ("added", "")})
def test_rl_invalid_char_error(string: str, letter: str) -> None:
    with pytest.raises(InvalidCharError):
        remove_letter(string, letter)


# Test make_acronym with given case
@pytest.mark.parametrize("string, expected", {("Art of Problem Solving", "AoPS")})
def test_make_acronym(string: str, expected: str) -> None:
    assert make_acronym(string) == expected


# Test most_common_letter with given cases
@pytest.mark.parametrize(
    "string, expected",
    {
        ("This is a test of the function I have written", "t"),
        (
            """My dear fellow," said Sherlock Holmes as we sat on either side of the fire in
                his lodgings at Baker Street, "life is infinitely stranger than anything which the
                mind of man could invent. We would not dare to conceive the things which are
                really mere commonplaces of existence.""",
            "e",
        ),
    },
)
def test_most_common_letter(string: str, expected: str) -> None:
    assert most_common_letter(string) == expected


# Test english_to_pig_latin with given cases
@pytest.mark.parametrize("word, expected", {("John", "Ohnjay"), ("john", "ohnjay")})
def test_english_to_pig_latin(word: str, expected: str) -> None:
    assert english_to_pig_latin(word) == expected


# Test rot13 with given cases
@pytest.mark.parametrize("input_str, expected", {("Hello, World!", "Uryyb, Jbeyq!")})
def test_rot13(input_str: str, expected: str) -> None:
    assert rot13(input_str) == expected
