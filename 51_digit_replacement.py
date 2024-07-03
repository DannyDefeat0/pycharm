import itertools
import euler_functions
from collections import defaultdict

#step 1 make our prime list to look through

primes = euler_functions.sieve(int(1e6))


#step 2 make a function that builds families of primes

def make_families(number):
    #this one is cool, it's dictionary that adds an entry if the key is missing
    families = defaultdict(set)
    for digit in '0123456789':
        for num_replacements in range(1, len(str(number)) + 1):
            # combinations is helping us take every pairing of different digits, not necessarily adjacent
            for indexes in itertools.combinations(range(len(str(number))), num_replacements):
                #no leading 0s
                if indexes[0] == 0 and digit == '0':
                    continue
                new_number_list = list(str(number))
                for index in indexes:
                    new_number_list[index] = digit
                new_number = ''.join(new_number_list)
                families[indexes].add(int(new_number))
    return families


#generate families from our list of primes until one family satisfies our requirement


def liam_neeson(family_size):
    for prime in primes:
        families = make_families(prime)
        for family in families:
            if len(primes.intersection(families[family])) == family_size:
                return prime, families[family]
    return "I will find you"


print(liam_neeson(8))
