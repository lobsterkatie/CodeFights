"""
CORNER OF 0S AND 1S / RANGE BIT COUNT

You are given two numbers a and b where 0 ≤ a ≤ b. Imagine you construct an
array of all the integers from a to b inclusive. You need to count the number
of 1s in the binary representations of all the numbers in the array.

Example

    For a = 2 and b = 7, the output should be
    rangeBitCount(a, b) = 11.

    Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7]. Converting the
    numbers to binary, we get [10, 11, 100, 101, 110, 111], which contains
    1 + 2 + 1 + 2 + 2 + 3 = 11 1s.

Input/Output

    [input] integer a

        Constraints:
        0 ≤ a ≤ b.

    [input] integer b

        Constraints:
        a ≤ b ≤ 10.

    [output] integer
"""


def rangeBitCount(a, b):
    #slicing the binary string from 2 on gets rid of the prefix
    #indicating that it's binary, leaving just the 1's and 0's
    binary_strs = [bin(x)[2:] for x in xrange(a, b+1)]
    smushed_together = "".join(binary_strs)
    return smushed_together.count("1")
