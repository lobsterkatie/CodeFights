"""
CORNER OF 0S AND 1S / MIRROR BITS

Reverse the order of the bits in a given integer.

Example

    For a = 97, the output should be
    mirrorBits(a) = 67.

    97 equals to 1100001 in binary, which is 1000011 after mirroring, and that
    is 67 in base 10.

    For a = 8, the output should be
    mirrorBits(a) = 1.

Input/Output

    [input] integer a

        Constraints:
        5 ≤ a ≤ 105.

    [output] integer
"""


def mirrorBits(a):
    #slicing the binary string from 2 on gets rid of the prefix
    #indicating that it's binary, leaving just the 1's and 0's
    return int(bin(a)[2:][::-1], 2)
