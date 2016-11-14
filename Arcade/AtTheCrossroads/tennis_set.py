"""
AT THE CROSSROADS / TENNIS SET

In tennis, a set is finished when one of the players wins 6 games and the other
one wins less than 5, or, if both players win at least 5 games, until one of
the players win 7 games.

Determine if it is possible for a tennis set to be finished with the score
score1 : score2.

Example

    For score1 = 3 and score2 = 6, the output should be
    tennisSet(score1, score2) = true;
    For score1 = 8 and score2 = 5, the output should be
    tennisSet(score1, score2) = false;
    For score1 = 6 and score2 = 5, the output should be
    tennisSet(score1, score2) = false.

Input/Output

    [input] integer score1

        Number of games won by the 1st player, non-negative integer.

        Constraints:
        0 ≤ score1 ≤ 10.

    [input] integer score2

        Number of games won by the 2nd player, non-negative integer.

        Constraints:
        0 ≤ score2 ≤ 10.

    [output] boolean

        true if score1 : score2 represents a possible score for an ended set,
        false otherwise.
"""


def tennisSet(score1, score2):
    higher = max(score1, score2)
    lower = min(score1, score2)

    return (((higher == 6) and (lower <= 4)) or
            ((higher == 7) and (lower in [5, 6])))
