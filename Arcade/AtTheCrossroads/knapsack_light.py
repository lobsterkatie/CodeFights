"""
AT THE CROSSROADS / KNAPSACK LIGHT

You found two items in a treasure chest! The first item weighs weight1 and is
worth value1, and the second item weighs weight2 and is worth value2. What is
the total maximum value of the items you can take with you, assuming that your
max weight capacity is maxW and you can't come back for the items later?

Example

    For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 8, the
    output should be
    knapsackLight(value1, weight1, value2, weight2, maxW) = 10.

    You can only carry the first item.

    For value1 = 10, weight1 = 5, value2 = 6, weight2 = 4 and maxW = 9, the
    output should be
    knapsackLight(value1, weight1, value2, weight2, maxW) = 16.

    You're strong enough to take both of the items with you.

Input/Output

    [input] integer value1

        Constraints:
        2 ≤ value1 ≤ 20.

    [input] integer weight1

        Constraints:
        2 ≤ weight1 ≤ 10.

    [input] integer value2

        Constraints:
        2 ≤ value2 ≤ 20.

    [input] integer weight2

        Constraints:
        2 ≤ weight2 ≤ 10.

    [input] integer maxW

        Constraints:
        1 ≤ maxW ≤ 20.

    [output] integer
"""


def knapsackLight(value1, weight1, value2, weight2, maxW):
    #see if you can take both
    if (weight1 + weight2) <= maxW:
        return value1 + value2

    #if not, take the more valuable one, as long as you can carry it

    #if item 1 is more valuable
    elif (value1 > value2):
        #try to take it
        if weight1 <= maxW:
            return value1
        #if it's too heavy, try to take the other item
        elif weight2 <= maxW:
            return value2
        #you're a weakling and get nothing
        else:
            return 0
    #if item 2 is more valuable
    else:
        #try to take it
        if weight2 <= maxW:
            return value2
        #if it's too heavy, try to take the other item
        elif weight1 <= maxW:
            return value1
        #you're a weakling and get nothing
        else:
            return 0
