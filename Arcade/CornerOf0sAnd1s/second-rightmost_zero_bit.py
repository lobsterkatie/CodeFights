"""
CORNER OF 0S AND 1S / SECOND-RIGHTMOST ZERO BIT

Presented with the integer n, find the 0-based position of the second rightmost
zero bit in its binary representation (it is guaranteed that such a bit
exists), counting from right to left.

Return the value of 2position_of_the_found_bit.

Example

    For n = 37, the output should be
    secondRightmostZeroBit(n) = 8.

    3710 = 1001012. The second rightmost zero bit is at position 3 (0-based)
    from the right in the binary representation of n.
    Thus, the answer is 23 = 8.

Input/Output

    [input] integer n

        Constraints:
        4 ≤ n ≤ 230.

    [output] integer
"""


def secondRightmostZeroBit(n):
    #slicing the binary string from 2 on gets rid of the prefix
    #indicating that it's binary, leaving just the 1's and 0's

    #first, reverse the string, since .find() searches from L->R rather than
    #R->L

    #then, figure out where the first zero is, and start a slice right after
    #that, then find the first zero in that slice

    #since .find() is zero-based, a zero one bit beyond the first zero will
    #be at index 0 of the new slice, a zero two beyond will be at index 1, etc

    #this means your overall index will be one short of what it should be, so
    #add 1
    return 2 ** (bin(n)[2:]
                       [::-1]
                       [bin(n)[2:][::-1].find("0") + 1:]
                       .find("0") +
                 bin(n)[2:][::-1].find("0") +
                 1)
