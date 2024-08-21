#!/usr/bin/python3
"""making coin change using the greedy algorithm"""


def makeChange(coins, total):
    """making coin change using the greedy algorithm"""
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    change = 0

    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
