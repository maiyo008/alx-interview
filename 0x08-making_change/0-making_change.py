#!/usr/bin/python3
"""
0-making_change.py
"""


def makeChange(coins, total):
    if total < 0:
        return -1

    # Initialize a list with total+1 elements, all set to float('inf')
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed for total of 0
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    return dp[total] if dp[total] != float('inf') else -1
