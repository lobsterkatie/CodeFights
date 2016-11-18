"""
LOOP TUNNEL / LEAST FACTORIAL

Given an integer n, find the minimal k such that

k = m! (where m! = 1 * 2 * ... * m) for some integer m;
k >= n.
In other words, find the smallest factorial which is not less than n.

Example

    For n = 17, the output should be
    leastFactorial(n) = 24.

    17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).

Input/Output

    [input] integer n

        A positive integer.

        Constraints:
        1 ≤ n ≤ 120.

    [output] integer
"""


from math import factorial


def leastFactorial(n):
    #since n is at most 120 (6!), we only need to check these factorial values
    for m in range(6):
        if factorial(m) >= n:
            return factorial(m)
