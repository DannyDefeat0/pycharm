def kth_prime(k):
    primes = [2]
    i = 3
    while len(primes) < k:
        for p in primes:
            if i % p == 0:
                break
            if p == primes[-1]:
                primes.append(i)
        i += 1
    return primes[-1]

print(kth_prime(10001))