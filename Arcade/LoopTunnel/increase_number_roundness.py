"""
LOOP TUNNEL / INCREASE NUMBER ROUNDNESS

Define an integer's roundness as the number of trailing zeroes in it.

Given an integer n, check if it's possible to increase n's roundness by
swapping some pair of its digits.

Example

    For n = 902200100, the output should be
    increaseNumberRoundness(n) = true.

    One of the possible ways to increase roundness of n is to swap digit 1 with
    digit 0 preceding it: roundness of 902201000 is 3, and roundness of n is 2.

    For instance, one may swap the leftmost 0 with 1.

    For n = 11000, the output should be
    increaseNumberRoundness(n) = false.

    Roundness of n is 3, and there is no way to increase it.

Input/Output

    [input] integer n

        A positive integer.

        Constraints:
        100 ≤ n ≤ 109.

    [output] boolean

        true if it's possible to increase n's roundness, false otherwise.
"""


def increaseNumberRoundness(n):
    n_str = str(n)

    zero_found = False
    roundness_increasable = False

    for digit in n_str:
        print "examining", digit

        #we're still looking for our first zero
        if not zero_found and digit == "0":
            print "zero found"
            zero_found = True
            continue

        #we've already found a zero and here's a non-zero to swap
        #it with, so we *can* increase the roundness
        if zero_found and digit != "0":
            print "found something to swap"
            roundness_increasable = True
            break

    return roundness_increasable
