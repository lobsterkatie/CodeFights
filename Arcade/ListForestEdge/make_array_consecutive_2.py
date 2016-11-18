"""
LIST FOREST EDGE / MAKE ARRAY CONSECUTIVE 2

Given an array of integers, we need to find the number of "holes" that need to
be filled such that it contains all the integers from some range.

Example

    For sequence = [6, 2, 3, 8], the output should be
    makeArrayConsecutive2(sequence) = 3.

    We need to add in 4, 5 and 7.

Input/Output

    [input] array.integer sequence

        An array of distinct integers.

        Constraints:
        1 ≤ sequence.length ≤ 10,
        -10 ≤ sequence[i] ≤ 10.

    [output] integer

        The minimal number of integers that need to be added to sequence such
        that it contains every integer from an interval [L, R] (for some L, R)
        and no other integers.
"""


def makeArrayConsecutive2(sequence):
    biggest = max(sequence)
    smallest = min(sequence)

    #add 1 because smallest should be counted in the range
    range_size = biggest - smallest + 1

    return range_size - len(sequence)
