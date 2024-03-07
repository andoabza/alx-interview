#!/usr/bin/python3
'''determine the fewest number of coins needed to meet a given amount total'''


def makeChange(coins, total):
    '''Returns the fewest number of coins'''
    change = [float('inf')] * (total + 1)
    change[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            change[i] = min(change[i], change[i - coin] + 1)
    if change[total] == float('inf'):
        return -1
    return change[total]
