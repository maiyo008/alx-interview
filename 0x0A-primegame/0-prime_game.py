#!/usr/bin/python3
"""
0-prime_game.py
"""


def generate_primes(limit):
    """
    Generate primes
    """
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False

    return [i for i in range(limit + 1) if primes[i]]

def isWinner(x, nums):
    """
    Check for the winner
    """
    def play_game(n):
        primes = generate_primes(n)
        return len(primes) % 2 == 0  # If there are even primes, Ben wins

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
