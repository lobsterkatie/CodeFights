"""
INTRO GATES / LARGEST NUMBER

Given an integer n, return the largest number that contains exactly n digits.

Example

    For n = 2, the output should be
    largestNumber(n) = 99.

Input/Output

    [input] integer n

        Constraints:
        1 ≤ n ≤ 7.

    [output] integer

        The largest integer of length n.
"""


def largestNumber(n):
    return int("9" * n)
