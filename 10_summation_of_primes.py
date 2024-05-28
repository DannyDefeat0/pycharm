def sum_of_primes(n):
    primes = [2]
    sum = 2
    i = 3
    for i in range(3,n):
        for p in primes:
            if i % p == 0:
                break
            if p == primes[-1]:
                sum += i
                primes.append(i)
    return sum

print(sum_of_primes(2000000))

