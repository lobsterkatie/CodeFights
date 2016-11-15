"""
CORNER OF 0S AND 1S / SWAP ADJACENT BITS

You're given an arbitrary 32-bit integer n. Swap each pair of adjacent bits in
its binary representation and return the result as a decimal number.

Example

    For n = 13, the output should be
    swapAdjacentBits(n) = 14.

    1310 = 11012 ~> 11102 = 1410.

    For n = 74, the output should be
    swapAdjacentBits(n) = 133.

    7410 = 010010102 ~> 100001012 = 13310.
    Note the preceding zero written in front of the initial number: since both
    numbers are 32-bit integers, they have 32 bits in their binary
    representation. The preceding zeros in other cases don't matter, so they
    are omitted. Here, however, it does make a difference.

Input/Output

    [input] integer n

        Constraints:
        0 ≤ n < 230.

    [output] integer
"""


def swapAdjacentBits(n):
    #slicing the binary string from 2 on gets rid of the prefix
    #indicating that it's binary, leaving just the 1's and 0's

    #the .rjust() forces the leading zeros to make each string 32 bits

    #the list comprehension is two-digit strings of swapped bits
    return int("".join([bin(n)[2:].rjust(32, "0")[i+1] +
                        bin(n)[2:].rjust(32, "0")[i]
                        for i in range(32)
                        if (i % 2) == 0]),
               2)
