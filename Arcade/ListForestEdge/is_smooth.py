"""
LIST FOREST EDGE / IS SMOOTH?

We define the middle of the array arr as follows:

if arr contains an odd number of elements, its middle is the element whose
index number is the same when counting from the beginning of the array and from
its end;
if arr contains an even number of elements, its middle is the sum of the two
elements whose index numbers when counting from the beginning and from the end
of the array differ by one.

An array is called smooth if its first and its last elements are equal to one
another and to the middle. Given an array arr, determine if it is smooth or
not.

Example

    For arr = [7, 2, 2, 5, 10, 7], the output should be
    isSmooth(arr) = true.

    The first and the last elements of arr are equal to 7, and its middle also
    equals 2 + 5 = 7. Thus, the array is smooth and the output is true.

    For arr = [-5, -5, 10], the output should be
    isSmooth(arr) = false.

    The first and middle elements are equal to -5, but the last element equals
    10. Thus, arr is not smooth and the output is false.

Input/Output

    [input] array.integer arr

        The given array.

        Constraints:
        2 ≤ arr.length ≤ 105,
        -109 ≤ arr[i] ≤ 109.

    [output] boolean

        true if arr is smooth, false otherwise.
"""


def isSmooth(arr):
    #fail fast
    if arr[0] != arr[-1]:
        return False

    #now we know the first and last elements are equal, so if the middle
    #equals the first, the array is smooth
    n = len(arr)
    if (n % 2) == 1:
        middle = arr[n/2]
    else:
        middle = arr[n/2 - 1] + arr[n/2]

    return arr[0] == middle
