import itertools

import euler_functions
from itertools import combinations

primes = euler_functions.sieve(100000)
combinations = itertools.combinations(primes, 5)



def all_pairs(numbers):
    str_numbers = set([str(number) for number in numbers])
    combinations = itertools.combinations(str_numbers, 2)
    return set([int(a + b) for a, b in combinations])


print(all_pairs((2,3,5,7,11)))


def five_prime(primes):
    for nums in combinations:
        combo_pairs = all_pairs(nums)
        Failed = False
        for pair in combo_pairs:
            if pair not in primes:
                Failed = True
                break
        if Failed == False:
            print(combo_pairs)
            print(sum(nums), " - ", nums)
            return sum(nums)
    return "Mission Failed"


print(five_prime(primes))
