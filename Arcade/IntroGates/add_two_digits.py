"""
INTRO GATES / ADD TWO DIGITS

You are given a two-digit integer n. Return the sum of its digits.

Example

    For n = 29, the output should be
    addTwoDigits(n) = 11.

Input/Output

    [input] integer n

        A positive two-digit integer.

        Constraints:
        10 ≤ n ≤ 99.

    [output] integer

        The sum of the first and second digits of the input number.
"""


def addTwoDigits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)

    return sum
