class InvalidNumberError(RuntimeError):
    """Error generated if input given is not a 4-digit positive integer."""


def flip_4_digit(n: int) -> int:
    """Flip the digits of a 4-digit positive integer

    Args:
        n: A 4-digit positive integer input value.

    Raises:
        InvalidNumberError: If input given is not a 4-digit positive integer.

    Returns:
        An integer with flipped digits.
    """
    if n < 0:
        raise InvalidNumberError(f"n is less than zero: {n}")
    elif n < 1000 or n > 9999:
        raise InvalidNumberError(f"n is not a 4-digit integer: {n}")

    return 1000 * (n % 10) + 100 * ((n // 10) % 10) + 10 * ((n // 100) % 10) + (n // 1000)
