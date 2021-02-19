# Python Class 2748
# Week 3
# Author: Akhil Karra


class InvalidPositiveIntegerError(RuntimeError):
    """Error generated if input given is not a positive integer."""


# Problem 2
def factorial(n: int) -> int:
    """Flip the digits of a 4-digit positive integer

    Args:
        n: A positive integer input value.

    Raises:
        InvalidPositiveIntegerError: If input given is not a positive integer.

    Returns:
        The nth factorial
    """
    if n < 0:
        raise InvalidPositiveIntegerError(f"n is less than 0: {n}")
    elif n == 0:
        return 1
    else:
        product = 1
        for i in range(1, n + 1):
            product *= i
        return product


# Answer to Problem 2
print(factorial(16))
