#!/usr/bin/python3
"""
0-making_change.py
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount total
    """
    if total < 0:
        return -1

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], 1 + dp[amount - coin])
    return dp[total] if dp[total] != float('inf') else -1
