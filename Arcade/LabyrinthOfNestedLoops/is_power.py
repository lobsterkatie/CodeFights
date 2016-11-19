"""
LABYRINTH OF NESTED LOOPS / IS POWER?

Determine if the given number is a power of some non-negative integer.

Example

    For n = 125, the output should be
    isPower(n) = true;
    For n = 72, the output should be
    isPower(n) = false.

Input/Output

    [input] integer n

        A positive integer.

        Constraints:
        1 ≤ n ≤ 350.

    [output] boolean

        true if n can be represented in the form a^b (a to the power of b)
        where a and b are some non-negative integers and b ≥ 2, false
        otherwise.
"""


from math import floor, log, sqrt, ceil


def isPower(n):
    #handle the special case of 1 separately (it doesn't grow with
    #successive powers, so it would put us into an infinite loop)
    if n == 1:
        return True

    #if n is a^b, then log base a or n will be b

    #so, take the log of n with successive bases and see if any come out
    #to be a whole number

    #the biggest a could be is n^.5, so we only need to check bases up
    #to floor(n^.5) (check one more in case n is equal to a square)
    for a in range(2, int(ceil(sqrt(n))) + 1):
        log_base_a = log(n, a)
        print a, log_base_a - floor(log_base_a)
        #we have to test the difference being teeny rather than the log
        #actually equaling its floor because of the imprecision of floats
        if (log_base_a >= 2 and
            log_base_a - floor(log_base_a) < .00000000001):
            return True

    #if we've gotten to here without finding an answer, there isn't one
    return False


#the above solution is O(n^.5)
#alternatively, we could do the below, which is O(n^.5 * lg n)

# def isPower(n):
#     #handle the special case of 1 separately (you can't take log base 1)
#     if n == 1:
#         return True
#
#     #the biggest a could be is n^.5, so we only need to check bases up
#     #to floor(n^.5) (check one more in case n is equal to a square)
#     for a in range(2, int(ceil(sqrt(n))) + 1):
#         b = 2
#         #keep trying powers of a until we find a match or get too big
#         while True:
#             print a, b, a ** b
#             if (a ** b) == n:
#                 return True
#             elif (a ** b) > n:
#                 break
#             else:
#                 b += 1
#
#     #if we've gotten to this point and haven't found a match, there is
#     #none
#     return False
