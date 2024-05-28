def num_divisors(powers):
    product = 1
    for power in powers:
        product *= (power + 1)
    return product

#There's a formula for the number of divisors related to prime factorization

def prime_factors_powers(n):
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i in factors:
                factors[i] += 1
            else:
                factors[i] = 1
    if n > 1:
        if n in factors:
            factors[n] += 1
        else:
            factors[n] = 1
    return list(factors.values())

#Find the prime factorization and return the information we need from that

def k_divisors_triangle(target):
    i = 1
    n = 1
    #compute number of divisors until we hit our target
    while num_divisors(prime_factors_powers(i)) < target:
        n += 1
        i += n
        print(i)
    return i

print(k_divisors_triangle(500))