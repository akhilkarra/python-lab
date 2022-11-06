# Python Class 2748
# Week 5
# Author: Akhil Karra

import typing


class InvalidNonnegativeIntegerError(RuntimeError):
    """Error generated if input given is not a nonnegative integer."""


class InvalidPositiveIntegerError(RuntimeError):
    """Error generated if input given is not a positive integer."""


class InputOneError(RuntimeError):
    """Error generated if input should not be 1."""


class OutOfBoundsError(RuntimeError):
    """Error generated if input given is out of bounds of what is expected"""


class InvalidTriangleError(RuntimeError):
    """Error generated if inputs do not correspond to a triangle as per the Triangle Inequality"""


# Problem 3
def assign_letter_grade(score: int) -> str:
    """Assign a linear letter grade to a given percentage score

    Args:
        :param score: nonnegative integer from 0-100 that is the percentage score given by the user

    Raises:
        InvalidNonnegativeIntegerError: If input given is not a nonnegative integer.
        OutOfBoundsError: If score is greater than 100

    Returns:
        The letter grade as a string.
    """
    if score < 0:
        raise InvalidNonnegativeIntegerError  # Make sure score is actually a nonnegative integer
    elif score > 100:
        raise OutOfBoundsError  # Make sure score given is not beyond 100
    else:
        if 96 <= score <= 100:
            return "A+"  # A score between 96 and 100 inclusive corresponds to an A+
        elif 88 <= score <= 95:
            return "A"  # A score between 88 and 95 inclusive corresponds to an A
        elif 85 <= score <= 87:
            return "B+"  # A score between 85 and 87 inclusive corresponds to a B+
        elif 80 <= score <= 84:
            return "B"  # A score between 80 and 84 inclusive corresponds to a B
        elif 77 <= score <= 79:
            return "C+"  # A score between 77 and 79 inclusive corresponds to a C+
        elif 70 <= score <= 76:
            return "C"  # A score between 70 and 76 inclusive corresponds to a C
        elif 66 <= score <= 69:
            return "D"  # A score between 66 and 69 inclusive corresponds to a D
        elif 50 <= score <= 65:
            return "F"  # A score between 50 and 65 inclusive corresponds to an F
        else:
            return "I"  # A score lower than a 49 inclusive corresponds to an I


# Problem 5
def is_right_triangle(a: int, b: int, c: int) -> bool:
    """Return boolean of whether the three integers form a right triangle

    Args:
        :param a: an integer corresponding to a side in a triangle
        :param b: an integer corresponding to a side in a triangle
        :param c: an integer corresponding to a side in a triangle

    Raises:
        InvalidTriangleError: If numbers do not correspond to a triangle by the Triangle Inequality

    Returns:
        True / False based on whether the three numbers correspond to the sides of a right triangle
    """
    if c >= (a + b) or b >= (a + c) or a >= (b + c):
        raise InvalidTriangleError  # Make sure inputs correspond to sides on a real triangle
    else:
        if a > b and a > c:
            return b * b + c * c == a * a  # Condition if a is the largest side
        elif b > a and b > c:
            return a * a + c * c == b * b  # Condition if b is the largest side
        else:
            return a * a + b * b == c * c  # Condition if c is the largest side


# Problem 6
def q1_1960_imo() -> typing.List[int]:
    """Returns the two three-digit numbers n such that n is divisible by 11 and (n / 11) is equal
    to the sum of the squares of the digits of n.

    Args:
        None.

    Raises:
        None.

    Returns:
        A list of the two integers in ascending order
    """
    answer = []  # Create the answer list

    for n in range(
        110, 1000, 11
    ):  # Define n to be a three-digit integer divisible by 11
        if n // 11 == (n // 100) ** 2 + ((n // 10) % 10) ** 2 + (n % 10) ** 2:
            answer.append(n)  # Find the qualifying integers and put them in the list

    return answer  # Give the list (should be [550, 803])


# Problem 7 Part (b). i.
def sum_of_proper_divs(n: int) -> int:
    """Returns the sum of the proper divisors of n.

    Args:
        :param n: a positive integer greater than 1

    Raises:
        InvalidPositiveIntegerError: if n is not a positive integer
        InputOneError: if n is equal to 1

    Returns:
        A list of the two integers in ascending order
    """
    if n <= 0:
        raise InvalidPositiveIntegerError  # Make sure that n is a positive integer
    elif n == 1:
        raise InputOneError  # Make sure that n is not equal to 1
    else:
        sum_of_divisors = 0  # Make a variable for the sum

        for i in range(1, n):  # For all integers between 1 and n-1 inclusive,
            if n % i == 0:  # If i is a divisor of n,
                sum_of_divisors += i  # Add i to the sum

        return sum_of_divisors  # Give the sum of proper divisors


# Problem 7 Part (b). ii.
def find_three_digit_perfect_number() -> int:
    """Returns the single three-digit perfect integer.

    Args:
        None.

    Raises:
        None.

    Returns:
        The three digit perfect integer.
    """
    answer = 0  # Make a variable for the answer

    for n in range(100, 1000):  # Define n to be a three digit number
        if (
            sum_of_proper_divs(n) == n
        ):  # If the single three-digit perfect integer is found,
            answer = n  # This is the number!

    return answer


# Problem 8 (challenge time!)
def find_other_taxicab_number() -> int:
    """Returns the other taxicab number (not 1729).

    Args:
        None.

    Raises:
        None.

    Returns:
        The other taxicab number.
    """
    list_of_sums_of_cubes = []  # Create an initial list

    for x in range(1, 23):  # The first 5-digit cube is 22**3 = 10648
        for y in range(
            1, x + 1
        ):  # Same reasoning as above; We want every single 4 digit sum
            if (
                1000 <= (x**3 + y**3) < 10000
            ):  # If the sum of the cubes is a four digit number,
                list_of_sums_of_cubes.append(x**3 + y**3)  # Add it to the list

    list_of_sums_of_cubes.sort()  # Sort in increasing order

    list_of_taxicabs = []  # Create a new list for the 4-digit taxicab numbers

    for i in range(len(list_of_sums_of_cubes)):  # Go through each sum of cubes
        if (
            list_of_sums_of_cubes[i] == list_of_sums_of_cubes[i - 1]
        ):  # If two identical sums of cubes are found,
            list_of_taxicabs.append(
                list_of_sums_of_cubes[i]
            )  # Add it as a taxicab number!

    return list_of_taxicabs[1]  # Return the second 4-digit taxicab number
