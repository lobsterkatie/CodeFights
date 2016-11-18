"""
LOOP TUNNEL / ROUNDERS

We want to turn the given integer into a number that has only one non-zero
digit using a tail rounding approach. This means that at each step we take the
last non 0 digit of the number and round it to 0 or to 10. If it's less than 5
we round it to 0 if it's larger than or equal to 5 we round it to 10 (rounding
to 10 means increasing the next significant digit by 1).

Example

    For value = 15, the output should be
    rounders(value) = 20;

    For value = 1234, the output should be
    rounders(value) = 1000.

    1234 -> 1230 -> 1200 -> 1000.

    For value = 1445, the output should be
    rounders(value) = 2000.

    1445 -> 1450 -> 1500 -> 2000.

Input/Output

    [input] integer value

        A positive integer.

        Constraints:
        1 ≤ value ≤ 108.

    [output] integer

        The rounded number.
"""


def rounders(value):
    #stringify so as to be able to reverse and iterate over the digits
    #easily, then re-int so we can increment digits easily
    digits_reversed = map(int, str(value)[::-1])

    num_zeros = len(digits_reversed) - 1

    #we need to look at all digits which will end up zeros, and
    #increment the next one for any digits 5 and above
    for i in range(num_zeros):
        digit = digits_reversed[i]
        if digit >= 5:
            digits_reversed[i+1] += 1

    #the new digits will be the last digit in digits reversed, plus
    #the necessary number of zeros
    new_digits = [digits_reversed[-1]] + ([0] * num_zeros)

    #stringify again so as to be able to join the digits, then cast
    #back to an int
    new_value = int("".join(map(str, new_digits)))

    return new_value

#Note that it's unclear here what something like 799 is supposed to round to -
#should it be 800 or 1000? (In other words, once we get to 800, are we done,
#or should we round the 8 up to a 10 as our final step?) The given (visible)
#tests don't address this. The current code rounds to 800.
