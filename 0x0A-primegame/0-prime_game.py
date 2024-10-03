#!/usr/bin/python3
'''Study Gaming '''

def isWinner(x, nums):
    '''winner'''
    winnerCounter = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        roundWinner = isRoundWinner(nums[i], x)
        if roundWinner is not None:
            winnerCounter[roundWinner] += 1

    if winnerCounter['Maria'] > winnerCounter['Ben']:
        return 'Maria'
    elif winnerCounter['Ben'] > winnerCounter['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n, x):
    ''' Rounds the winner'''
    list = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        #  current player
        currentPlayer = players[i % 2]
        selectedIdxs = []
        prime = -1
        for idx, num in enumerate(list):
            # if already picked prime num then num is multipl of the prime num
            if prime != -1:
                if num % prime == 0:
                    selectedIdxs.append(idx)
            # else check
            else:
                if isPrime(num):
                    selectedIdxs.append(idx)
                    prime = num
        # if failed to pick then current player lost
        if prime == -1:
            if currentPlayer == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(selectedIdxs):
                del list[val - idx]
    return None


def isPrime(n):
    # even numbers greater than 2 are NOT PRIME
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        # Not prime if divisable by another number
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return "Not prime"
        return True