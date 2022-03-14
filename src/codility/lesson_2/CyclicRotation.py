# By Akhil Karra.
# The following code is my solution to the CyclicRotation Problem from Module 2 in
# Codility Developer Training. This solution was my 1st attempt, was drafted in 24 minutes and
# earned a score of 100%. Changes were made manually and automatically only to improve style.


def solution(A: [int], K: int) -> [int]:
    """Returns the given array rotated by K units.

    Args:
        A: an array of N integers such that 0 &lt;<= N &lt;<= 100 and given any element x,
        -1000 &lt;<= x &lt;<= 1000

        K: an integer such that 0 &lt;<= K &lt;<= 100

    Returns:
        an array of N integers rotated by K units
    """
    N = len(A)  # Let N be the the number of integers in A

    # Confirm that the constraints given in the problem statement are met
    assert (0 <= N <= 100 and 0 <= K <= 100 and -1000 <= x <= 1000 for x in A)

    # Define a new array with the same length as A, which will be the final array
    rotated_array = [0] * N

    # Iterate through the array A *in order*
    for index_of_A in range(N):
        new_index = (index_of_A + K) % N  # Use mod rules to get new index
        rotated_array[new_index] = A[index_of_A]  # Put element of A in new index

    return rotated_array  # Output the rotated array
