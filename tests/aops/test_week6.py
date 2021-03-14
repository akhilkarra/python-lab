import pytest
from src.aops.week6 import count_letters, first_six_digit_triangular, sum_first_n_primes


# Test first_six_digit_triangular
@pytest.mark.parametrize("expected", {100128})
def test_first_six_digit_triangular(expected: int) -> None:
    assert first_six_digit_triangular() == expected


# Test count_letters
@pytest.mark.parametrize(
    "text, letter, expected",
    {
        ("David Patrick", "a", 2),
        (
            """It's passed on.
        This parrot is no more.
        It has ceased to be.
        It's expired and gone to meet its maker.
        This is a late parrot.
        It's a stiff.
        Bereft of life, it rests in peace.
        If you hadn't nailed it to the perch, it would be pushing up the daisies.
        It's rung down the curtain and joined the choir invisible.
        This is an ex-parrot!""",
            "e",
            29,
        ),
    },
)
def test_count_letters(text: str, letter: str, expected: int) -> None:
    assert count_letters(text, letter) == expected


# Test sum_of_n_primes
@pytest.mark.parametrize("n, expected", {(1, 2), (2, 5), (3, 10), (4, 17), (100, 24133)})
def test_sum_of_n_primes(n: int, expected: int) -> None:
    assert sum_first_n_primes(n) == expected
