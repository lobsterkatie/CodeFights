"""
CORNER OF 0S AND 1S / ARRAY PACKING

You are given an array of up to four non-negative integers, each less than 256.

Your task is to pack these integers into one number M in the following way:

The first element of the array occupies the first 8 bits of M;
The second element occupies next 8 bits, and so on.
Return the obtained integer M.

Note: the phrase "first bits of M" refers to the least significant bits of M -
the right-most bits of an integer. For further clarification see the following
example.

Example

    For a = [24, 85, 0], the output should be
    arrayPacking(a) = 21784.

    An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.
    After packing these into one number we get 00000000 01010101 00011000
    (spaces are placed for convenience), which equals to 21784.

Input/Output

    [input] array.integer a

        Constraints:
        1 ≤ a.length ≤ 4,
        0 ≤ a[i] < 256.

    [output] integer
"""


def arrayPacking(decimal_array):
    #slicing the binary string from 2 on gets rid of the prefix
    #indicating that it's binary, leaving just the 1's and 0's
    binary_array_backwards = (
        [bin(x)[2:].rjust(8, "0") for x in decimal_array][::-1])

    final_binary_str = ""

    for binary_str in binary_array_backwards:
        final_binary_str += binary_str

    return int(final_binary_str, 2)
