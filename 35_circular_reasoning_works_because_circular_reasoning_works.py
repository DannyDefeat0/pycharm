
circular_prime_count = 0

n = 1000000

is_prime = [False, False] + [True] * (n - 1)
list_of_primes = [2]

for i in range(3, n + 1, 2):
    if is_prime[i]:
        list_of_primes.append(i)
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
print(list_of_primes)

def circular_prime_check(number):
    number = str(number)
    digits = len(number)
    for digit in range(digits):
        if int(number) not in list_of_primes:
            return False
        number = number[1:] + number[0]
    return True

for prime in list_of_primes:
    if circular_prime_check(prime):
        print(prime)
        circular_prime_count += 1
print(circular_prime_count)