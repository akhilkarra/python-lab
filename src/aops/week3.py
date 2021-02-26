# Python Class 2748
# Week 3
# Author: Akhil Karra


class InvalidPositiveIntegerError(RuntimeError):
    """Error generated if input given is not a positive integer."""


class InvalidWholeNumberError(RuntimeError):
    """Error generated if input given is not a whole number."""


# Problem 2
def factorial(n: int) -> int:
    """Compute the nth factorial.

    Args:
        n: A positive integer input value.

    Raises:
        InvalidWholeNumberError: If input given is not a whole number.

    Returns:
        The nth factorial
    """
    if n < 0:
        raise InvalidWholeNumberError(f"n is less than 0: {n}")
    elif n == 0:
        return 1
    else:
        product = 1
        for i in range(1, n + 1):
            product *= i
        return product


# Problem 4
def fibonacci(n: int) -> int:
    """Compute the nth Fibonacci number.

    Args:
        n: A positive integer input value.

    Raises:
        InvalidPositiveIntegerError: If input given is not a positive integer.

    Returns:
        The nth Fibonacci
    """
    # Make sure the entered integer is positive.
    if n <= 0:
        raise InvalidPositiveIntegerError(f"n is less than or equal to 0: {n}")

    # If the integer entered is 1 or 2, give the number 1
    elif (n == 1) or (n == 2):
        return 1

    # If the integer entered is three or more:
    else:
        # Let there be three variables for the two previous numbers and a sum
        fib1before = 1
        fib2before = 1
        fibnow = 0

        # For each successive integer (from 1 up to n-1 because there are n-2 of them):
        for i in range(1, n - 1):
            # Find the sum of the two previous Fibonacci numbers
            fibnow = fib1before + fib2before

            # Let the previous Fibonacci number be the second previous Fibonacci number
            fib2before = fib1before

            # Let the current Fibonacci now be the previous Fibonacci number
            fib1before = fibnow

        # Give the current Fibonacci number
        return fibnow
