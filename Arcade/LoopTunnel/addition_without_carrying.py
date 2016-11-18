"""
LOOP TUNNEL / ADDITION WITHOUT CARRYING

A little boy is studying arithmetics. He has just learned how to add two
integers, written one below another, column by column. But he always forgets
about the important part - carrying.

Given two integers, find the result which the little boy will get.

Note: the boy used this site as the source of knowledge, feel free to check it
out too if you are not familiar with column addition.

Example

    For param1 = 456 and param2 = 1734, the output should be
    additionWithoutCarrying(param1, param2) = 1180.

       456
      1734
    + ____
      1180
    The little boy goes from right to left:

    6 + 4 = 10 but the little boy forgets about 1 and just writes down 0 in the
    last column
    5 + 3 = 8
    4 + 7 = 11 but the little boy forgets about the leading 1 and just writes
    down 1 under 4 and 7.
    There is no digit in the first number corresponding to the leading digit of
    the second one, so the little boy imagines that 0 is written before 456.
    Thus, he gets 0 + 1 = 1.

Input/Output

    [input] integer param1

        A non-negative integer.

        Constraints:
        0 ≤ param1 ≤ 99999.

    [input] integer param2

        A non-negative integer.

        Constraints:
        0 ≤ param2 ≤ 59999.

    [output] integer

        The result that the little boy will get.
"""


def additionWithoutCarrying(top, bottom):

    result_digits_reversed = []

    while top > 0 or bottom > 0:
        #compute and store next result digit
        top_digit = top % 10
        bottom_digit = bottom % 10
        result_digit = (top_digit + bottom_digit) % 10
        result_digits_reversed.append(str(result_digit))

        #move one space to the right
        top = top / 10
        bottom = bottom / 10

    #if top and bottom are both 0, result_digits_reversed will be empty
    if result_digits_reversed:
        result_digits = result_digits_reversed[::-1]
        result = int("".join(result_digits))
    else:
        result = 0

    return result


#alternatively:

# def additionWithoutCarrying(top, bottom):

#     #make the addends the same length (have to stringify to do this)
#     length = max(len(str(top)), len(str(bottom)))
#     top_str = str(top).rjust(length, "0")
#     bottom_str = str(bottom).rjust(length, "0")

#     result_digits = []

#     #compute and store next result digit
#     #since carrying isn't a thing here, L -> R will the the same as R -> L
#     for i, top_digit_char in enumerate(top_str):
#         top_digit = int(top_digit_char)
#         bottom_digit = int(bottom_str[i])
#         result_digit = (top_digit + bottom_digit) % 10
#         result_digits.append(str(result_digit))

#     result = int("".join(result_digits))
#     return result
