import typing

import pytest
from src.aops.week10 import (
    count_letters,
    dict_reverse,
    highest_scoring_scrabble_word,
    replace_word,
    student_averages,
    translation_dictionary,
    translator,
)


# Test dict_reverse with given test case
@pytest.mark.parametrize(
    "input_dict, expected",
    [({"adam": 80, "betty": 60, "charles": 50}, {80: "adam", 60: "betty", 50: "charles"})],
)
def test_dict_reverse(input_dict: typing.Dict[str, int], expected: typing.Dict[int, str]) -> None:
    assert dict_reverse(input_dict) == expected


# Test student averages with file and given test case
@pytest.mark.parametrize(
    "grades_txt_filepath, expected",
    [
        (
            "tests/aops/test_files/grades.txt",
            {
                "Gilliam": 78.75,
                "Jones": 83.0,
                "Cleese": 85.75,
                "Chapman": 95.0,
                "Idle": 91.0,
                "Palin": 85.0,
            },
        )
    ],
)
def test_student_averages(grades_txt_filepath: str, expected: typing.Dict[str, int]) -> None:
    assert student_averages(grades_txt_filepath) == expected


# Test highest_scoring_scrabble_word given wordlist.txt and answer to Problem 4
@pytest.mark.parametrize(
    "wordlist_path, expected", {("tests/aops/test_files/wordlist.txt", "razzamatazzes")}
)
def test_highest_scoring_scrabble_word(wordlist_path: str, expected: str) -> None:
    assert highest_scoring_scrabble_word(wordlist_path) == expected


# Test count_letters using given test case:
@pytest.mark.parametrize(
    "input_string, expected",
    {
        (
            "I like learning Python at Art of Problem Solving!",
            """a: 3
b: 1
e: 3
f: 1
g: 2
h: 1
i: 4
k: 1
l: 4
m: 1
n: 4
o: 4
p: 2
r: 3
s: 1
t: 3
v: 1
y: 1
""",
        )
    },
)
def test_count_letters(input_string: str, expected: str) -> None:
    assert count_letters(input_string) == expected


# Test replace_word with given test case
@pytest.mark.parametrize(
    "input_string, old_word, new_word, expected",
    {
        (
            """It was Toto that made Dorothy laugh, and saved her from growing as gray as
her other surroundings. Toto was not gray; he was a little black dog, with
long silky hair and small black eyes that twinkled merrily on either side
of his funny, wee nose. Toto played all day long, and Dorothy played with
him, and loved him dearly.""",
            "Toto",
            "Gizmo",
            "It was Gizmo that made Dorothy laugh, and saved her from growing as gray as "
            "her other surroundings. Gizmo was not gray; he was a little black dog, with "
            "long silky hair and small black eyes that twinkled merrily on either side of "
            "his funny, wee nose. Gizmo played all day long, and Dorothy played with him, "
            "and loved him dearly.",
        )
    },
)
def test_replace_word(input_string: str, old_word: str, new_word: str, expected: str) -> None:
    assert replace_word(input_string, old_word, new_word) == expected


# Test translation_dictionary
@pytest.mark.parametrize(
    "dict_file_name, separator, expected",
    [
        (
            "tests/aops/test_files/pirateWords.txt",
            "|",
            {
                "hello": "avast",
                "money": "filthy lucre",
                "you": "ye",
                "your": "ye",
                "steal": "swipe",
            },
        )
    ],
)
def test_translation_dictionary(
    dict_file_name: str, separator: str, expected: typing.Dict[str, str]
) -> None:
    assert translation_dictionary(dict_file_name, separator) == expected


# Test translator using given test case
@pytest.mark.parametrize(
    "dict_file_name, text_file_name, expected",
    {
        (
            "tests/aops/test_files/pirateWords.txt",
            "tests/aops/test_files/myInput.txt",
            """avast i have come to swipe ye filthy lucre
ye filthy lucre or ye life""",
        )
    },
)
def test_translator(dict_file_name: str, text_file_name: str, expected: str) -> None:
    assert translator(dict_file_name, text_file_name) == expected
