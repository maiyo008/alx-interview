#!/usr/bin/python3
"""
0-making_change.py
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount total
    """
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
