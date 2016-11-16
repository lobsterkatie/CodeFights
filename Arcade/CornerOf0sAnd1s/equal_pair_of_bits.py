"""
CORNER OF 0S AND 1S / EQUAL PAIR OF BITS

You're given two integers, n and m. Find position of the rightmost pair of
equal bits in their binary representations (it is guaranteed that such a pair
exists), counting from right to left.

Return the value of 2position_of_the_found_pair (0-based).

Example

    For n = 10 and m = 11, the output should be
    equalPairOfBits(n, m) = 2.

    1010 = 10102, 1110 = 10112, the position of the rightmost pair of equal
    bits is the bit at position 1 (0-based) from the right in the binary
    representations.
    So the answer is 21 = 2.

Input/Output

    [input] integer n

        Constraints:
        0 ≤ n ≤ 230.

    [input] integer m

        Constraints:
        0 ≤ m ≤ 230.

    [output] integer
"""


def equalPairOfBits(n, m):
    #n ^ m does an xor, which puts a 1 anywhere the bits differ, and a 0
    #anywhere they're the same

    #slicing the binary string from 2 on gets rid of the prefix
    #indicating that it's binary, leaving just the 1's and 0's

    #we're looking for the rightmost zero in the result of the xor, but if it's
    #a leading zero, it won't be there, so pad all of the numbers with leading
    #zeros before reversing the binary strings

    #reverse the string, since .find() searches from L->R rather than R->L
    return 2 ** (bin(n ^ m)[2:].rjust(32, "0")[::-1].find("0"))
