"""
CORNER OF 0S AND 1S / DIFFERENT RIGHTMOST BIT

You're given two integers, n and m. Find position of the rightmost bit in
which they differ in their binary representations (it is guaranteed that such
a bit exists), counting from right to left.

Return the value of 2 ^ position_of_the_found_bit (0-based).

Example

    For n = 11 and m = 13, the output should be
    differentRightmostBit(n, m) = 2.

    1110 = 10112, 1310 = 11012, the rightmost bit in which they differ is the
    bit at position 1 (0-based) from the right in the binary representations.
    So the answer is 21 = 2.

Input/Output

    [input] integer n

        Constraints:
        0 ≤ n ≤ 230.

    [input] integer m

        Constraints:
        0 ≤ m ≤ 230,
        n ≠ m.

    [output] integer
"""


def differentRightmostBit(n, m):
    #n ^ m does an xor, which puts a 1 anywhere the bits differ, and a 0
    #anywhere they're the same

    #slicing the binary string from 2 on gets rid of the prefix
    #indicating that it's binary, leaving just the 1's and 0's

    #reverse the string, since .find() searches from L->R rather than R->L
    return 2 ** (bin(n ^ m)[2:][::-1].find("1"))
