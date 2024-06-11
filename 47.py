#step 1 build list of primes to use for factorization

def prime_sieve(n):
    is_prime = [False, False] + [True] * (n - 1)
    list_of_primes = [2]

    for i in range(3, n + 1, 2):
        if is_prime[i]:
            list_of_primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    print("primes done")
    return list_of_primes


primes = prime_sieve(10000)

#step 2 build a function that checks two consecutive numbers distinct primes
#stop when either a and b share a factor or both have been factorized
#at the end we check if they have the right number of factors


def distinct_prime_factors(a, b, prime_list, num_factors):
    i = 0
    a_factors = set()
    b_factors = set()
    while (a != 1 or b != 1) and i < len(prime_list):
        if a % prime_list[i] != 0 and b % prime_list[i] != 0:
            i += 1
        elif a % prime_list[i] == 0 and b % prime_list[i] == 0:
            return False
        elif a % prime_list[i] == 0:
            a = a // prime_list[i]
            a_factors.add(prime_list[i])
        elif b % prime_list[i] == 0:
            b = b // prime_list[i]
            b_factors.add(prime_list[i])
    return len(a_factors) == num_factors and len(b_factors) == num_factors

#step 3, build a function that records chains of consecutive numbers with a certain number of distinct primes
#each time a comparison works, add it to our set, otherwise we reset the set..
#we don't technically need a set here

def distinct_factor_chain(n, num_factors):
    chain = set()
    i = 2
    while len(chain) < n:
        if distinct_prime_factors(i, i + 1, primes, num_factors):
            chain.update([i, i + 1])
        else:
            chain = {i + 1}
        i += 1
    return chain

#print(distinct_prime_factors(14, 15, primes, 2))
print(distinct_factor_chain(4,4))