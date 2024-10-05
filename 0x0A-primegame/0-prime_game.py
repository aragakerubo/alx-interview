#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Prime Game
    Args:
        x (int): number of rounds
        nums (list): list of integers
    Returns:
        str: name of the player that won most rounds
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [True for _ in range(max(n + 1, 2))]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = primes[1] = False
    c = 0
    for i in range(len(primes)):
        if primes[i]:
            c += 1
        primes[i] = c
    players = ['Maria', 'Ben']
    score = [0, 0]
    for i in range(x):
        c = primes[nums[i]] % 2
        if c:
            score[0] += 1
        else:
            score[1] += 1
    if score[0] > score[1]:
        return players[0]
    if score[0] < score[1]:
        return players[1]
    return None
