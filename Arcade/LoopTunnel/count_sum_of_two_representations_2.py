"""
LOOP TUNNEL / COUNT SUM OF TWO REPRESENTATIONS 2

Given integers n, l and r, find the number of ways to represent n as a sum of
two integers A and B such that l ≤ A ≤ B ≤ r.

Example

    For n = 6, l = 2 and r = 4, the output should be
    countSumOfTwoRepresentations2(n, l, r) = 2.

    There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4
    and 6 = 3 + 3.

Input/Output

    [input] integer n

        A positive integer.

        Constraints:
        5 ≤ n ≤ 109.

    [input] integer l

        A positive integer.

        Constraints:
        1 ≤ l ≤ r.

    [input] integer r

        A positive integer.

        Constraints:
        l ≤ r ≤ 109,
        r - l ≤ 106.

    [output] integer
"""


def countSumOfTwoRepresentations2(n, left_bound, right_bound):
    #fail fast
    if left_bound > (n / 2) or right_bound < (n / 2):
        print "left bound too high or right bound too low"
        return 0

    #otherwise, attempt to make sums starting from the left bound
    count = 0
    a = left_bound
    b = n - a
    #print "initial (a, b): ", a, b
    while a <= b <= right_bound:
        #print "(a, b): ", a, b
        count += 1
        a += 1
        b -= 1

    #if that didn't work (meaning the left bound is farther from n/2 than the
    #right bound is) then make sums starting from the right bound
    if count == 0:
        print "trying from the right instead"
        b = right_bound
        a = n - b
        #print "initial (a, b): ", a, b
        while left_bound <= a <= b:
            #print "(a, b): ", a, b
            count += 1
            a += 1
            b -= 1

    return count
