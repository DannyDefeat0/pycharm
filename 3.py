ants = 600851475143

def largest_prime_factor(number):
    target = number
    primes = [2]
    duds = []
    i = 3
    if number < 2:
        return -1
    while target != 1:
        if i not in primes and i not in duds:
            for p in primes:
                if i % p == 0:
                    duds.append(i)
                    break
                elif p == primes[-1]:
                    primes.append(i)
        if i in primes:
            if target % i == 0:
                target = target // i
                if target == 1:
                    return i
                i = 1
        i += 1

    return i


print(largest_prime_factor(ants))