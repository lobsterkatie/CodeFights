"""
AT THE CROSSROADS / IS INFINITE PROECESS?

Given integers a and b, determine whether the following pseudocode results in
an infinite loop

while a is not equal to b do
  increase a by 1
  decrease b by 1

Assume that the program is executed on a virtual machine which can store
arbitrary long numbers and execute forever.

Example

    For a = 2 and b = 6, the output should be
    isInfiniteProcess(a, b) = false;
    For a = 2 and b = 3, the output should be
    isInfiniteProcess(a, b) = true.

Input/Output

    [input] integer a

        Constraints:
        0 ≤ a ≤ 20.

    [input] integer b

        Constraints:
        0 ≤ b ≤ 20.

    [output] boolean

        true if the pseudocode will never stop, false otherwise.
"""


def isInfiniteProcess(a, b):
    #a will never equal b (and therefore the machine will never stop) if either
    #a) a starts out above b, or
    #b) the difference between them is odd (in which case they'll get to the
    #point where they're one apart and then swap values and diverge forever)
    return (a > b) or (((b - a) % 2) == 1)
