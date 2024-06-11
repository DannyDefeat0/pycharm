truncatable_primes = set()

n = 1000000
is_prime = [False, False] + [True] * (n - 1)
primes = [2]

for i in range(3, n + 1, 2):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
print(len(primes))

maximum = 0, 0

for p in range(len(primes)):
    k = p
    total = primes[p]
    while total < 1e6:
        k += 1
        total += primes[k]
        if k-p >= maximum[0] and total in primes:
            print(maximum)
            maximum = k-p, total
    if k-p < maximum[0]:
        #we know past this point all the chains will be shorter
        break
print(maximum)

