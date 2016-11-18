"""
LIST FOREST EDGE / REMOVE ARRAY PART

Remove a part of a given array between given 0-based indexes l and r
(inclusive).

Example

    For inputArray = [2, 3, 2, 3, 4, 5], l = 2 and r = 4, the output should be
    removeArrayPart(inputArray, l, r) = [2, 3, 5].

Input/Output

    [input] array.integer inputArray

        Constraints:
        2 ≤ inputArray.length ≤ 10,
        -10 ≤ inputArray[i] ≤ 10.

    [input] integer l

        Left index of the part to be removed (0-based).

        Constraints:
        0 ≤ l ≤ r.

    [input] integer r

        Right index of the part to be removed (0-based).

        Constraints:
        l ≤ r < inputArray.length.

    [output] array.integer
"""


def removeArrayPart(array, left_bound, right_bound):
    array[left_bound:right_bound + 1] = []
    return array
