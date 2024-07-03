import requests

def open_txt(url):
    return requests.get(url).text.splitlines()

#generate a set of prime numbers up to n

def sieve(n):
    is_prime = [False, False] + [True] * (n - 1)
    primes = {2}
    for i in range(3, n + 1, 2):
        if is_prime[i]:
            primes.add(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes


def sieve_list(n):
    is_prime = [False, False] + [True] * (n - 1)
    primes = [2]
    for i in range(3, n + 1, 2):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes