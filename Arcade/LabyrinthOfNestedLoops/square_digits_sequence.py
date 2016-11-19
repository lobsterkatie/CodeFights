"""
LABYRINTH OF NESTED LOOPS / SQUARE DIGITS SEQUENCE

Consider a sequence of numbers a0, a1, ..., an, in which an element is equal to
the sum of squared digits of the previous element. The sequence ends once an
element that has already been in the sequence appears again.

Given the first element a0, find the length of the sequence.

Example

    For a0 = 16, the output should be
    squareDigitsSequence(a0) = 9.

    Here's how elements of the sequence are constructed:

    a0 = 16
    a1 = 12 + 62 = 37
    a2 = 32 + 72 = 58
    a3 = 52 + 82 = 89
    a4 = 82 + 92 = 145
    a5 = 12 + 42 + 52 = 42
    a6 = 42 + 22 = 20
    a7 = 22 + 02 = 4
    a8 = 42 = 16, which has already occurred before (a0)
    Thus, there are 9 elements in the sequence.

    For a0 = 103, the output should be
    squareDigitsSequence(a0) = 4.

    The sequence goes as follows: 103 -> 10 -> 1 -> 1, 4 elements altogether.

Input/Output

    [input] integer a0

        First element of a sequence, positive integer.

        Constraints:
        1 ≤ a0 ≤ 650.

    [output] integer
"""


def squareDigitsSequence(a0):
    #we don't care about the order of the sequence, just its length, so
    #use a set because it won't add a duplicate - as soon as the size of
    #the set is one less than the number of sequence terms we've added to
    #it, we know we're done

    terms = set()

    #add a0
    terms.add(a0)
    count = 1

    current_term = a0

    while len(terms) == count:
        #find the next term
        squares = [int(digit) ** 2 for digit in str(current_term)]
        next_term = sum(squares)

        #add it to our set and increment the count
        terms.add(next_term)
        count += 1

        #make it the current term
        current_term = next_term

    #if we've come out of the loop, it's because we've hit a duplicate,
    #so we're done
    return count
