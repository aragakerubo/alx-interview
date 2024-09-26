#!/usr/bin/python3
"""
Given a pile of coins of different values, determine
the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine
    the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    n = len(coins)
    count = 0
    i = 0
    while total > 0 and i < n:
        if coins[i] <= total:
            total -= coins[i]
            count += 1
        else:
            i += 1
    if total != 0:
        return -1
    return count
