#!/usr/bin/python3
"""prime game trial"""


def isWinner(x, nums):
    """prime game trial"""
    if not nums or x < 1:
        return None

    max_value = max(nums)  # Find the maximum value in nums

    # filtering to mark prime numbers
    sieve = [True] * (max(max_value + 1, 2))  # atleast filter is size 2
    for i in range(2, int(max_value ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_value + 1, i):
                sieve[j] = False

    sieve[0], sieve[1] = False, False  # 0 and 1 are not prime numbers

    # a prime count up to each index
    prime_count = 0
    for i in range(len(sieve)):
        if sieve[i]:
            prime_count += 1
        sieve[i] = prime_count

    maria_wins = 0
    for num in nums:
        # Maria wins when the number of primes up to `num` is odd
        if sieve[num] % 2 == 1:
            maria_wins += 1

    total_rounds = len(nums)

    # Determining the winner
    if maria_wins * 2 == total_rounds:
        return None  # a tie
    elif maria_wins * 2 > total_rounds:
        return "Maria"
    else:
        return "Ben"
