#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Generate changes needed to reach total
    """
    if total <= 0:
        return 0
    check = 0
    tmp = 0
    coins.sort(reverse=True)
    for i in coins:
        while check < total:
            check += i
            tmp += 1
        if check == total:
            return tmp
        check -= i
        tmp -= 1
    return -1
