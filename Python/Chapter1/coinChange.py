# MINIMUM NUMBER OF COINS USING GREEDY ALGORITHM
"""
Given a value V, if we want to make a change for V Rs, and we have 
an infinite supply of each of the denominations in Indian currency, 
i.e., we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 
500, 1000} valued coins/notes, what is the minimum number of coins 
and/or notes needed to make the change?
"""


def min_coins(target, coins):
    coins.sort(reverse=True)
    change = []
    total = 0
    for coin in coins:
        times = (target - total) // coin
        total += times * coin
        change += [coin] * times
    return change


if __name__ == '__main__':
    n = 93
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    print(min_coins(n, coins))
