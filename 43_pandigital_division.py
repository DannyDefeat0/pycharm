import itertools

filtered_permutations = [''.join(p) for p in itertools.permutations("0123456789") if p[0] != '0']

primes = [2, 3, 5, 7, 11, 13, 17]



def prime_property_check(number):
    i = 1
    for prime in primes:
        if int(number[i:i + 3]) % prime != 0:
            return 0
        i += 1
    return int(number)

total = 0


for permutation in filtered_permutations:
    total += prime_property_check(permutation)
print(total)
