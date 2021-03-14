# Python Class 2748
# Week 6
# Author: Akhil Karra

import math
import random
import time


# Problem 2
def first_six_digit_triangular() -> int:
    """Find the first six-digit triangular number

    Args:
        None.

    Raises:
        None.

    Returns:
        The first six-digit triangular number
    """
    triangular = 0  # Create a variable for the triangular number
    n = 1  # Create a variable with the next positive integer

    while triangular // (10 ** 5) < 1:  # While the triangular is less than six-digits:
        triangular += n  # Add n to get the next triangular number
        n += 1  # Increment n

    return triangular  # Return the triangular number


# Problem 4
def count_letters(text: str, letter: str) -> int:
    """Returns number of times that letter appears in text

    Args:
        text: a string of text
        letter: the character to search

    Raises:
        None.

    Returns:
        An integer of how many times the letter appears in the text
    """
    letter_count = 0  # Create a variable for the letter count
    for character in text:  # For each character in the text:
        if character == letter:  # If the character matches the letter given:
            letter_count += 1  # Increment the letter count.

    return letter_count


# Problem 5
def is_prime(n: int) -> bool:
    """Check if an integer is prime

    Args:
        n: an integer

    Raises:
        None.

    Returns:
        Whether the integer is prime or not
    """
    ans = True  # Make a default answer of True

    for integer in range(2, math.floor(math.sqrt(n)) + 1):  # For each integer from 2 to sqrt(n),
        if n % integer == 0:  # If n is divisible by this integer,
            ans = False  # n is not prime

    return ans


def sum_first_n_primes(n: int) -> int:
    """Find the sum of the first n primes.

    Args:
        n: the number of primes to add

    Raises:
        None.

    Returns:
        The sum of the first n primes.
    """
    sum_of_primes = 2  # Create a variable for the sum of primes
    integer = 3  # Create a variable for each successive odd integer
    n -= 1  # We already have one prime, so we can reduce the number of primes to add by 1

    while n > 0:  # While there are still primes to add,
        if is_prime(integer):  # If the integer is a prime,
            sum_of_primes += integer  # Add the integer to the sum of primes
            n -= 1  # There is now one less prime to add

        integer += 2  # Move on to the next odd integer

    return sum_of_primes  # Once all the primes have been added, give the sum out


# Problem 6a
def backgammon_roll() -> int:
    """Simulate a roll in backgammon and returns the total.

    Args:
        None.

    Raises:
        None.

    Returns:
        Backgammon sum of the two virtual die
    """
    dice_1 = random.randint(1, 6)  # Roll dice 1
    dice_2 = random.randint(1, 6)  # Roll dice 2

    if dice_1 == dice_2:  # If a doubles is rolled
        return 2 * (dice_1 + dice_2)  # Return twice the sum of the numbers shown on the die
    else:
        return dice_1 + dice_2  # Else, return the sum of the numbers shown on the die


# Problem 6b
def backgammon_race() -> None:
    """Create a random backgammon race and print each roll to the user until one player reaches 100
    points.

    Args:
        None.

    Raises:
        None.

    Returns:
        A full suspenseful backgammon race in the console!
    """
    print("Welcome to Backgammon! Presenting: Alex and You!")
    alex = 0  # Create the player Alex
    player = 0  # Create the player for the user
    time.sleep(3)  # Get some suspense going by pausing

    while player < 100:  # While Morgan's score is less than 100 (Alex's case is dealt with below):
        print("\nAlex rolls...")
        alex_roll = backgammon_roll()  # Alex does roll now...
        time.sleep(2)  # Get some suspense going by pausing
        print(str(alex_roll) + "!")  # Let the user know what Alex got.
        alex += alex_roll
        time.sleep(2)  # Pause for a bit
        print("Alex now has a score of " + str(alex) + ".")
        time.sleep(2)  # Pause for a bit

        if alex >= 100:
            break  # End the game if Alex passes 100 points

        print("\nYou roll...")
        player_roll = backgammon_roll()  # Player rolls..
        time.sleep(2)  # Get some suspense going by pausing
        print(str(player_roll) + "!")  # Let the user know what Morgan got.
        player += player_roll
        time.sleep(2)  # Pause for a bit
        print("You now have a score of " + str(player) + ".")
        time.sleep(2)  # Pause for a bit

    if alex >= 100:
        print("\nAlex wins!!!!")
    else:
        print("\nYou win!!!!")


# Problem 7
def guessing_game() -> None:
    """Runs a guessing game where the computer picks a random number from 0 to 100 and the user has
    to guess that exact number

    Args:
        None.

    Raises:
        None.

    Returns:
        The full fun guessing game in the console!
    """
    print("Hey there! It's time for you to have a break and play a guessing game with me!")
    time.sleep(2)

    print("I'm thinking of a number between 0 and 100.")
    number = random.randint(0, 100)  # The computer now has a number
    tries = 0  # The computer is very helpful and it is holding the number of tries taken
    time.sleep(2)

    user = int(input("Try your best and guess my number: "))  # Get the user's guess

    while user != number:  # While the user has not guessed the number correctly
        print("Well...")
        time.sleep(1)  # Suspense time!

        tries += 1  # Increment the number of tries taken to correctly guess the number

        if user > number:
            print("Too high!")
        else:
            print("Too low!")

        user = int(input("Try your best and guess my number: "))  # Get the user's guess again

    print("Well...")
    time.sleep(1)  # Suspense time!
    print("You got it! It was", number)
    time.sleep(1)  # Suspense time!
    print("It took you", tries, "tries. Well done! See you soon <3")
