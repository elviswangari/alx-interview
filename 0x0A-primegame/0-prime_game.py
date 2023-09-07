#!/usr/bin/python3
'''
module to retun winner of a prime game
'''


def isWinner(x, nums):
    '''
    function that  returns the winner
    '''
    if not nums or x < 1:
        return None

    max_num = max(nums)

    # Create a list to mark prime numbers
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    # Sieve of Eratosthenes to mark non-prime numbers
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    # Count the number of prime numbers up to each index
    prime_count = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_count[i] = prime_count[i - 1] + is_prime[i]

    player1 = 0
    for num in nums:
        if prime_count[num] % 2 == 1:
            player1 += 1

    total_players = len(nums)
    if player1 * 2 == total_players:
        return None
    elif player1 * 2 > total_players:
        return "Maria"
    else:
        return "Ben"
