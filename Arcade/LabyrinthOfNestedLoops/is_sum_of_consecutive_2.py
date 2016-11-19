"""
LABYRINTH OF NESTED LOOPS / IS SUM OF CONSECUTIVE 2

Find the number of ways to express n as sum of some (at least two) consecutive positive integers.

Example

    For n = 9, the output should be
    isSumOfConsecutive2(n) = 2.

    There are two ways to represent n = 9: 2 + 3 + 4 = 9 and 4 + 5 = 9.

    For n = 8, the output should be
    isSumOfConsecutive2(n) = 0.

    There are no ways to represent n = 8.

Input/Output

    [input] integer n

        A positive integer.

        Constraints:
        1 ≤ n ≤ 25.

    [output] integer
"""


def isSumOfConsecutive2(n):
    count = 0

    #the first addend can't be greater than half of n, since it will be the
    #smallest one
    for first_num in range(1, n/2 + 1):
        sum = first_num
        next_num = first_num + 1

        #as long as our sum hasn't gotten too big, keep trying
        while sum < n:
            #add the next consecutive number
            sum += next_num

            #if we've found a match, increment our count
            #the loop won't run again in this case
            if sum == n:
                count += 1
                continue

            #if we haven't found a match, move to the next consecutive
            #number
            next_num += 1

    #return our count
    return count
