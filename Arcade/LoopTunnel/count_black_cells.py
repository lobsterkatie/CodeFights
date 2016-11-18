"""
LOOP TUNNEL / COUNT BLACK CELLS

Imagine a white rectangular grid of n rows and m columns divided into two parts
by a diagonal line running from the upper left to the lower right corner. Now
let's paint the grid in two colors according to the following rules:

A cell is painted black if it has at least one point in common with the
diagonal;
Otherwise, a cell is painted white.
Count the number of cells painted black.

Example

    For n = 3 and m = 4, the output should be
    countBlackCells(n, m) = 6.

    There are 6 cells that have at least one common point with the diagonal and
    therefore are painted black.

    [graphic removed]

    For n = 3 and m = 3, the output should be
    countBlackCells(n, m) = 7.

    7 cells have at least one common point with the diagonal and are painted
    black.

    [graphic removed - note that it showed that all four cells around a lattice
    point count as black]

Input/Output

    [input] integer n

        The number of rows.

        Constraints:
        1 ≤ n ≤ 105.

    [input] integer m

        The number of columns.

        Constraints:
        1 ≤ m ≤ 105.

    [output] integer

        The number of black cells.
"""


from math import floor


def countBlackCells(height, width):
    black_squares = 0

    #the line has to travel through each column in the grid

    #find the height at which the line enters each column (which is also, of
    #course, the height at which it exits the column before) and store them for
    #later use
    entry_heights = []
    for col in range(width):
        #for each unit that it travels horizontally, it will travel
        #rise/run = hieght/width units vertically
        entry_heights.append(col * (float(height) / width))

    #add the height the line exits the last column, which will always be the
    #same as the height of the whole grid
    entry_heights.append(height)

    #for each column, the number of black squares will be the difference in the
    #floors of the entry and exit points for that column, plus
    #2 if the entry point is a lattice point
    #1 otherwise

    #this is because counting the difference doesn't count the square you're on
    #(so always add 1), and taking the floors doesn't account for the square
    #underneath a lattice point (so add 1 more in that case)

    #calculate the black square for each column and add that to our total
    for col in range(width):
        entry_height = entry_heights[col]
        exit_height = entry_heights[col + 1]
        floor_diff = floor(exit_height) - floor(entry_height)

        #check if the entry point is a lattice point, and add 2 if so
        if int(entry_height) == entry_height:
            black_squares += floor_diff + 2
        #otherwise, add 1
        else:
            black_squares += floor_diff + 1

    #this will overcount the number of squares by 2 (the squares directly below
    #the first square and directly above the last square aren't in the grid),
    #so subtract 2
    black_squares -= 2

    return black_squares
