"""
LIST FOREST EDGE / ARRAY REPLACE

Given an array of integers, replace all the occurrences of elemToReplace with
substitutionElem.

Example

    For inputArray = [1, 2, 1], elemToReplace = 1 and substitutionElem = 3, the
    output should be
    arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

Input/Output

    [input] array.integer inputArray

        Constraints:
        2 ≤ inputArray.length ≤ 10,
        0 ≤ inputArray[i] ≤ 10.

    [input] integer elemToReplace

        Constraints:
        0 ≤ elemToReplace ≤ 10.

    [input] integer substitutionElem

        Constraints:
        0 ≤ substitutionElem ≤ 10.

    [output] array.integer
"""


def arrayReplace(array, num_to_replace, substitute_num):
    for i, num in enumerate(array):
        if num == num_to_replace:
            array[i] = substitute_num

    return array
