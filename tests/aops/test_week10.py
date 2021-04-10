import pytest
from src.aops.week10 import dict_reverse, student_averages, highest_scoring_scrabble_word


# Test dict_reverse with given test case
@pytest.mark.parametrize(
    "input_dict, expected",
    [({'adam': 80, 'betty': 60, 'charles': 50}, {80: 'adam', 60: 'betty', 50: 'charles'})]
)
def test_dict_reverse(input_dict: dict, expected: dict) -> None:
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
                    "Palin": 85.0
                }
        )
    ]
)
def test_student_averages(grades_txt_filepath: str, expected: dict) -> None:
    assert student_averages(grades_txt_filepath) == expected


# Test highest_scoring_scrabble_word given wordlist.txt and answer to Problem 4
@pytest.mark.parametrize(
    "wordlist_path, expected",
    {("tests/aops/test_files/wordlist.txt", "razzamatazzes")}
)
def test_highest_scoring_scrabble_word(wordlist_path: str, expected: str) -> None:
    assert highest_scoring_scrabble_word(wordlist_path) == expected
