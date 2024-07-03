import euler_functions

primes = euler_functions.sieve_list(1000000)

print(primes)

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

