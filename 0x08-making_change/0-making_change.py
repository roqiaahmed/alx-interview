#!/usr/bin/python3

"""
make Change method
"""


def makeChange(coins, total):
    """make Change method"""
    if total <= 0:
        return 0
    num_coins = 0
    i = len(coins) - 1

    sorted_coins = sorted(coins)

    while i >= 0:
        while sorted_coins[i] <= total:
            num_coins += 1
            total -= sorted_coins[i]
        if total == 0:
            return num_coins
        i -= 1
    return -1
